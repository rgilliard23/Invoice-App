<template>
  <div class="clear">
    <b-container class="clear m-0 p-0 fullHeight" fluid>
      <b-navbar
        style="height:10vh;"
        class="clear"
        toggleable="lg"
        type="dark"
        variant="info"
      >
        <b-navbar-brand class="margin" tag="h1" href="#">
          <b-row>
            <router-link to="/" class="text-white">
              <h1 style="margin: 0 15px;" v-if="!edit">
                <b-icon-arrow-left> </b-icon-arrow-left>
              </h1>
            </router-link>

            <h1 class="navMargin" v-if="!edit">Create Invoice</h1>
            <h1 v-else>Edit Invoice</h1></b-row
          >
        </b-navbar-brand>

        <!-- //* Invoice Table -->

        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-dropdown
              class="exportDropdown"
              variant="danger"
              size="lg"
              :disabled="InvoiceIncomplete"
              text="Export"
            >
              <b-dropdown-item href="#">
                <JsonExcel :disabled="InvoiceIncomplete" :data="items">
                  Excel
                </JsonExcel></b-dropdown-item
              >
              <b-dropdown-item
                href="#"
                v-b-modal.InvoiceTemplate
                >PDF</b-dropdown-item
              >
            </b-dropdown>

            <!-- <b-button
              :disabled="InvoiceIncomplete"
              v-b-modal.InvoiceTemplate
              class="margin"
              size="lg"
              variant="danger"
              >Invoice Pdf</b-button
            >
            <b-button
              :disabled="InvoiceIncomplete"
              class="margin"
              size="lg"
              variant="success"
            >
             
            </b-button> -->
            <b-button
              v-if="!edit"
              v-on:click="saveInvoice"
              :disabled="InvoiceIncomplete"
              class="margin text-light"
              size="lg"
              variant="success"
              >Save Invoice</b-button
            >
            <b-button
              v-else
              v-on:click="updateInvoice"
              :disabled="InvoiceIncomplete"
              class="margin text-light"
              size="lg"
              variant="success"
              >Update Invoice</b-button
            >
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <div style="height: 10px;"></div>

      <b-row
        align-h="center"
        class="margin w-100"
        style="height: 15vh; max-height: 20vh;"
      >
        <b-col lg="6" class="my-1">
          <b-form-group
            label="Date Created:"
            label-cols-lg="3"
            label-align-sm="right"
            label-for="sortBySelect"
            class="mb-0"
          >
            <b-form-datepicker
              v-model="createdDate"
              size="lg"
              id="example-datepicker"
              class="mb-2"
            ></b-form-datepicker>
          </b-form-group>
        </b-col>

        <b-col lg="6" class="my-1">
          <b-form-group
            label="Date Due:"
            label-cols-lg="3"
            label-align-sm="right"
            label-for="initialSortSelect"
            class="mb-0"
          >
            <b-form-datepicker
              size="lg"
              id="example-datepicker"
              v-model="dateDue"
              class="mb-2"
            ></b-form-datepicker>
          </b-form-group>
        </b-col>

        <b-col lg="6" class="my-1">
          <b-form-group
            label="Add Products:"
            label-cols-lg="3"
            label-align-sm="right"
            label-for="filterInput"
            class="mb-0"
          >
            <b-button v-b-modal.productsModal block variant="success"
              >Add Products</b-button
            >
          </b-form-group>
        </b-col>

        <b-col lg="6" class="my-1">
          <b-form-group
            label="Select Customer:"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="filterInput"
            class="mb-0"
          >
            <b-button v-b-modal.customerModal block variant="outline-success">
              <span v-if="customer.name != null">{{ customer.name }}</span>
              <span v-else>Select Customer</span>
            </b-button>
          </b-form-group>
        </b-col>
        <b-pagination
          class="w-100"
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
          align="fill"
        ></b-pagination>
      </b-row>
      <div style="height: 2vh;"></div>
      <b-container fluid>
        <b-table
          small
          striped
          fixed
          :currentPage="currentPage"
          sticky-header="50vh"
          :items="items"
          :perPage="perPage"
          :key="index"
          :fields="invoiceFields"
        >
          <template v-slot:cell(id)="data">
            <b-form-input
              readonly
              type="number"
              v-model="data.item.id"
              read-only
              placeholder="Id"
            ></b-form-input>
          </template>
          <template v-slot:cell(name)="data">
            <b-form-input
              type="text"
              v-model="data.item.name"
              read-only
              placeholder="Name"
            ></b-form-input>
          </template>
          <template v-slot:cell(price)="data">
            <b-form-input
              @change="inLineTotal"
              type="number"
              step="1"
              v-model="data.item.price"
              read-only
            ></b-form-input>
          </template>
          <template v-slot:cell(quantity)="data">
            <b-form-input
              type="number"
              @change="inLineTotal"
              v-model="data.item.quantity"
              read-only
            ></b-form-input>
          </template>
          <template v-slot:cell(total)="data">
            <b-form-input
              readonly
              type="number"
              :value="lineTotal(data.item)"
              read-only
            ></b-form-input>
          </template>
          <template v-slot:cell(actions)="data">
            <b-button variant="danger" @click="deleteRow(data.item.uniqueId)"
              >Remove</b-button
            >
          </template>
          <template v-slot:custom-foot>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Sub Total:</td>
              <td>${{ subTotal.toLocaleString() }}</td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Tax:</td>
              <td>
                <b-input-group append="%">
                  <b-form-input
                    append="%"
                    min="0"
                    v-model="tax"
                    type="number"
                  ></b-form-input>
                </b-input-group>
              </td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Discount:</td>
              <td>
                <b-input-group append="%">
                  <b-form-input
                    min="0"
                    v-model="discount"
                    type="number"
                  ></b-form-input>
                </b-input-group>
              </td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Grand Total:</td>
              <td>${{ grandTotal.toLocaleString() }}</td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td>
                <b-button @click="addRow" variant="primary">Add Row</b-button>
              </td>
              <td></td>
            </tr>
          </template>
        </b-table>

        <b-form-group label="Invoice Notes:">
          <b-form-textarea
            id="textarea"
            v-model="notes"
            placeholder="Notes.."
            rows="6"
            max-rows="6"
          ></b-form-textarea>
        </b-form-group>
      </b-container>
      <b-modal
        hide-footer
        title="Invoice"
        size="xl"
        id="InvoiceTemplate"
        ref="InvoiceTemplate"
      >
        <InvoiceTemplate
          ref="content"
          v-bind:transactions="items"
          v-bind:dateDue="dateDue"
          v-bind:createdDate="createdDate"
          class="overflow"
        />
      </b-modal>
      <b-modal
        hide-footer
        centered
        size="lg"
        id="productsModal"
        ref="productsModal"
        title="Add Products"
      >
        <keep-alive>
          <ProductsModal
            @closeProductModal="closeProductModal"
            v-bind:transactions="items"
          />
        </keep-alive>
      </b-modal>

      <b-modal
        hide-footer
        ref="customerModal"
        centered
        size="lg"
        id="customerModal"
        title="Select Customer"
      >
        <keep-alive>
          <CustomerModal @selectCustomer="selectCustomer" />
        </keep-alive>
      </b-modal>
    </b-container>
  </div>
</template>

<script>
import "axios";
import ProductsModal from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/ProductsModal.vue";
import CustomerModal from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/CustomerModal.vue";
import InvoiceTemplate from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/InvoiceTemplate.vue";
// import JwPagination from "jw-vue-pagination";
import JsonExcel from "vue-json-excel";
import { BIconArrowLeft } from "bootstrap-vue";

const axios = require("axios");
const productPath = "http://localhost:5000/api/product";
const customerPath = "http://localhost:5000/api/customer";
const invoicePath = "http://localhost:5000/api/invoice";
const transactionPath = "http://localhost:5000/api/transaction";

export default {
  name: "Invoice",
  components: {
    CustomerModal,
    ProductsModal,
    InvoiceTemplate,
    BIconArrowLeft,
    // JwPagination,
    JsonExcel,
  },
  props: {
    invoiceCustomer: { type: Object, default: null },
    edit: { type: Boolean, default: false },
    invoice: { type: Object, default: null },
  },
  data: function() {
    return {
      GrandTotal: 0,
      transactions: [],
      createdDate: null,
      dateDue: null,
      customer: {
        id: null,
        name: null,
        address: null,
      },
      customers: [],
      currentPage: 1,
      products: [],
      invoices: [],
      perPage: 5,
      tax: 0,
      discount: 0,
      notes: "",
      pageOfItems: [],
      excelFields: ["name", "price", "quantity", "total"],
      invoiceFields: [
        { key: "id", label: "Id" },
        { key: "name", label: "Name" },
        { key: "price", label: "Price" },
        { key: "quantity", label: "Quantity" },
        { key: "total", label: "Total" },
        { key: "actions", label: "" },
      ],
      customLabels: {
        first: "<<",
        last: ">>",
        previous: "<",
        next: ">",
      },
      items: [
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300,
        },
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300,
        },
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300,
        },
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300,
        },
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300,
        },
      ],
    };
  },
  computed: {
    subTotal() {
      let temp = 0;

      this.items.forEach((transaction) => {
        temp += transaction.price * transaction.quantity;
      });
      return temp;
    },
    grandTotal() {
      let grandTotal = this.subTotal;
      let discount = grandTotal * (this.discount / 100);
      grandTotal = this.subTotal - discount;
      let tax = grandTotal * (this.tax / 100);
      grandTotal += tax;
      return Number(grandTotal.toFixed(2));
    },
    InvoiceIncomplete() {
      if (
        this.customer.name !== null &&
        this.items.length > 0 &&
        this.createdDate !== null &&
        this.dateDue !== null
      ) {
        return false;
      } else {
        return true;
      }
    },
    rows() {
      return this.items.length;
    },
  },
  methods: {
    onChangePage(pageOfItems) {
      // update page of items
      this.pageOfItems = pageOfItems;
    },
    addRow() {
      this.inLineTotal();
      let temp = 0;
      if (this.items.length > 0) {
        temp = this.items[this.items.length - 1].uniqueId + 1;
      } else {
        temp = 0;
      }

      this.items.push({
        uniqueId: temp,
        id: 0,
        name: "",
        quantity: Number(1),
        price: Number(0),
        total: 0,
      });

      this.currentPage = Math.ceil(this.items.length / this.perPage);
    },
    closeProductModal() {
      this.inLineTotal();
      this.$refs["productsModal"].hide();
    },
    deleteRow(index) {
      this.inLineTotal();
      this.items.splice(index, 1);
    },
    lineTotal(product) {
      return Number((product.price * product.quantity).toFixed(2));
    },
    inLineTotal() {
      let count = 0;
      this.items.forEach((element) => {
        element.uniqueId = count;
        element.total = Number((element.price * element.quantity).toFixed(2));
        element.price = Number(element.price);
        element.quantity = Number(element.quantity);
        count++;
      });
    },
    selectCustomer(customer) {
      this.customer.id = customer.id;
      this.customer.name = customer.name;
      this.customer.address = customer.address;
      this.$refs["customerModal"].hide();
    },
    getProducts() {
      axios
        .get(productPath)
        .then((res) => {
          this.products = res.data.products;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getCustomers() {
      axios
        .get(customerPath)
        .then((res) => {
          this.customers = res.data.customers;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    updateInvoice() {
      let temp = {
        date_created: this.createdDate,
        date_due: this.dateDue,
        notes: this.notes,
        customer_id: this.customer.id,
        total: this.grandTotal,
      };

      axios
        .put(invoicePath + "/" + this.invoice.id, temp)
        .then((res) => {
          alert("Invoice Updated");
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
          console.log("Invoice Error");
        });

      var invoiceId = 0;

      axios
        .get(invoicePath)
        .then((res) => {
          this.invoices = res.data.invoices;
          console.log(typeof this.invoices);
        })
        .catch((err) => {
          console.log(err);
        });

      setTimeout(1000);
      invoiceId = 1;

      if (this.invoices.length > 0) {
        invoiceId = this.invoices[this.invoices.length - 1].id;
      }

      this.items.forEach((item) => {
        let temp2 = {
          date_created: this.createdDate,
          quantity: Number(item.quantity),
          invoice_id: invoiceId,
          product_id: item.id,
        };
        console.log(temp2);
        axios
          .put(transactionPath + "/" + item.id, temp2)
          .then((res) => {
            alert("howdy");
            console.log(res);
          })
          .catch((err) => {
            console.log(err);
            console.log("Transaction Error");
          });
      });
    },
    saveInvoice() {
      let temp = {
        date_created: this.createdDate,
        date_due: this.dateDue,
        notes: this.notes,
        customer_id: this.customer.id,
        total: this.grandTotal,
      };

      axios.post(invoicePath, temp).then((res) => {
        alert("Invoice Saved");
        console.log(res);

        var invoiceId = 1;

        setTimeout(1000);

        axios
          .get(invoicePath)
          .then((res) => {
            this.invoices = res.data.invoices;

            console.log("howdyyyyyy" + this.invoices);

            alert(this.invoices.length);

            if (this.invoices.length > 0) {
              alert("invoice");
              invoiceId = this.invoices[this.invoices.length - 1].id;
            }

            console.log(this.invoices[this.invoices.length - 1].id);

            this.items
              .forEach((item) => {
                let temp2 = {
                  date_created: this.createdDate,
                  quantity: item.quantity,
                  invoice_id: invoiceId,
                  product_id: item.id,
                };

                console.log(temp2);

                axios
                  .post(transactionPath, temp2)
                  .then((res) => {
                    alert("howdy");
                    console.log(res);
                  })
                  .catch((err) => {
                    console.log(err);
                    console.log("Transaction Error");
                  });
              })
              .catch((err) => {
                console.log(err);
                console.log("Invoice Error");
              });
          })
          .catch((err) => {
            console.log(err);
          });
      });
    },
    viewInvoice(invoice) {
      this.invoice = invoice;
      this.$refs["viewInvoice"].show();
    },
  },
  filters: {
    currency(value) {
      return Number(value.toFixed(2));
    },
  },
  created() {
    if (this.invoice !== null) {
      this.createdDate = this.invoice.date_created;
      this.dateDue = this.invoice.date_due;
      this.customer = this.invoiceCustomer;
      this.items = [];
      this.invoice.transactions.forEach((element) => {
        this.items.push({
          id: element.product.id,
          name: element.product.name,
          quantity: element.quantity,
          price: element.product.price,
        });
      });
    }
  },
};
</script>

<style scoped>
.exportDropdown {
  font-size: 20px;
}

.margin {
  margin-left: 10px;
  margin-right: 10px;
}
.overflow {
  overflow: scroll;
  max-height: 85vh;
  height: 85vh;
}
.navMargin {
  margin: 0 5px;
}
</style>
