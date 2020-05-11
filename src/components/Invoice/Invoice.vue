<template>
  <div class="clear">
    <b-container class="clear fullHeight" fluid>
      <b-navbar style="height:10vh;" class="clear" toggleable="lg" type="dark" variant="info">
        <b-navbar-brand class="margin" tag="h1" href="#">
          <h1>Create Invoice</h1>
        </b-navbar-brand>

        <!-- //* Invoice Table -->

        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-button
              :disabled="InvoiceIncomplete"
              v-b-modal.InvoiceTemplate
              class="margin"
              size="lg"
              variant="danger"
            >Invoice Pdf</b-button>
            <b-button
              :disabled="InvoiceIncomplete"
              class="margin"
              size="lg"
              variant="secondary"
            >Export To Excel</b-button>
            <b-button
              :disabled="InvoiceIncomplete"
              class="margin"
              size="lg"
              variant="success"
            >Save Invoice</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <div style="height: 10px;"></div>
      <b-row class="margin" style="height: 10vh;">
        <b-col lg="6" class="my-1">
          <b-form-group
            label="Date Created:"
            label-cols-lg="3"
            label-align-sm="right"
            label-for="sortBySelect"
            class="mb-0"
          >
            <b-form-datepicker v-model="createdDate" size="lg" id="example-datepicker" class="mb-2"></b-form-datepicker>
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
            <b-form-datepicker size="lg" id="example-datepicker" v-model="dateDue" class="mb-2"></b-form-datepicker>
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
            <b-button v-b-modal.productsModal block variant="success">Add Products</b-button>
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
              <span v-if="customer.name != null">{{customer.name}}</span>
              <span v-else>Select Customer</span>
            </b-button>
          </b-form-group>
        </b-col>
      </b-row>
      <div style="height: 2vh;"></div>
      <b-container fluid>
        <b-table
          small
          striped
          fixed
          sticky-header="50vh"
          :items="items"
          :key="index"
          :fields="invoiceFields"
        >
          <template v-slot:cell(id)="data">
            <b-form-input readonly type="number" v-model="data.item.id" read-only placeholder="Id"></b-form-input>
          </template>
          <template v-slot:cell(name)="data">
            <b-form-input type="text" v-model="data.item.name" read-only placeholder="Name"></b-form-input>
          </template>
          <template v-slot:cell(price)="data">
            <b-form-input
              @change="inLineTotal"
              type="number"
              v-model="data.item.price"
              read-only
              placeholder="Price"
            ></b-form-input>
          </template>
          <template v-slot:cell(quantity)="data">
            <b-form-input
              type="number"
              @change="inLineTotal"
              v-model="data.item.quantity"
              read-only
              placeholder="Quantity"
            ></b-form-input>
          </template>
          <template v-slot:cell(total)="data">
            <b-form-input readonly type="number" v-model="data.item.total" read-only></b-form-input>
          </template>
          <template v-slot:cell(actions)="data">
            <b-button variant="danger" @click="deleteRow(data.item.uniqueId)">Remove</b-button>
          </template>
          <template v-slot:custom-foot>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Sub Total:</td>
              <td>${{subTotal.toLocaleString()}}</td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Tax:</td>
              <td>
                <b-input-group append="%">
                  <b-form-input append="%" min="0" v-model="tax" type="number"></b-form-input>
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
                  <b-form-input min="0" v-model="discount" type="number"></b-form-input>
                </b-input-group>
              </td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Grand Total:</td>
              <td>${{grandTotal.toLocaleString()}}</td>
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
      <b-modal hide-footer title="Invoice" size="xl" id="InvoiceTemplate" ref="InvoiceTemplate">
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
          <ProductsModal @closeProductModal="closeProductModal" v-bind:transactions="items" />
        </keep-alive>
      </b-modal>

      <b-modal
        hide-footer
        ref="customerModal"
        centered
        size="lg"
        id="customerModal"
        title="Add Customer"
      >
        <keep-alive>
          <CustomerModal @selectCustomer="selectCustomer" />
        </keep-alive>
      </b-modal>
      <!-- <b-table-simple fixed sticky-header="60vh">
        <b-thead>
          <b-tr>
            <b-th>Country</b-th>
            <b-th>City</b-th>
            <b-th>Trousers</b-th>
            <b-th>Skirts</b-th>
            <b-th>Dresses</b-th>
            <b-th>Bracelets</b-th>
            <b-th>Rings</b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr>
            <b-td>
              <b-form-input class="w-100" v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
          </b-tr>
        </b-tbody>
        <b-tfoot>
          <b-tr>
            <b-td colspan="7" class="text-right">
              Total Rows:
              <b>5</b>
            </b-td>
          </b-tr>
        </b-tfoot>
      </b-table-simple>-->
    </b-container>
  </div>
</template>

<script>
import "axios";
import ProductsModal from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/ProductsModal.vue";
import CustomerModal from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/CustomerModal.vue";
import InvoiceTemplate from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/InvoiceTemplate.vue";
const axios = require("axios");
const productPath = "http://localhost:5000/api/product";
const customerPath = "http://localhost:5000/api/customer";

export default {
  name: "Invoice",
  components: {
    CustomerModal,
    ProductsModal,
    InvoiceTemplate
  },
  data: function() {
    return {
      GrandTotal: 0,
      transactions: [],
      createdDate: null,
      dateDue: null,
      customer: {
        name: null,
        address: null
      },
      customers: [],
      products: [],
      tax: 0,
      discount: 0,
      notes: "",
      invoiceFields: [
        { key: "id", label: "Id" },
        { key: "name", label: "Name" },
        { key: "price", label: "Price" },
        { key: "quantity", label: "Quantity" },
        { key: "total", label: "Total" },
        { key: "actions", label: "" }
      ],
      items: [
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300
        },
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300
        },
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300
        },
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300
        },
        {
          uniqueId: 0,
          id: 1,
          name: "Ronald",
          quantity: 1,
          price: 300,
          total: 300
        }
      ]
    };
  },
  computed: {
    subTotal() {
      let subTotal = 0;
      this.items.forEach(element => {
        subTotal += element.total;
      });
      return Number(subTotal.toFixed(2));
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
    }
  },
  methods: {
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
        quantity: 1,
        price: 0,
        total: 0
      });
    },
    closeProductModal() {
      this.inLineTotal();
      this.$refs["productsModal"].hide();
    },
    deleteRow(index) {
      this.inLineTotal();
      this.items.splice(index, 1);
    },
    inLineTotal() {
      let count = 0;
      this.items.forEach(element => {
        element.uniqueId = count;
        element.total = Number((element.price * element.quantity).toFixed(2));
        count++;
      });
    },
    selectCustomer(customer) {
      this.customer.name = customer.name;
      this.customer.address = customer.address;
      this.$refs["customerModal"].hide();
    },
    getProducts() {
      axios
        .get(productPath)
        .then(res => {
          this.products = res.data.products;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  getCustomers() {
    axios
      .get(customerPath)
      .then(res => {
        this.customers = res.data.customers;
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  filters: {
    currency(value) {
      return Number(value.toFixed(2));
    }
  }
};
</script>

<style scoped>
.margin {
  margin-left: 10px;
  margin-right: 10px;
}
.overflow {
  overflow: scroll;
  max-height: 70vh;
  height: 70vh;
}
</style>