<template>
  <div style=" overflow: auto">
    <b-navbar style="height:10vh;" type="light" variant="white">
      <b-navbar-brand class="text-center">
        <h1>Home</h1>
      </b-navbar-brand>
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <!-- <v-text-field
                  class="navSearch"
                  label="Search"
                  v-model="searchCustomer"
                  solo
                  hide-details
                ></v-text-field> -->
          <!-- <v-btn
                  @click="showCustomer(null, false)"
                  class="navLinks navButton navButtonMargin"
                  block
                  color="success"
                  >Add Customer
                </v-btn> -->
          <v-container align-center class="m-0 p-0" id="dropdown-example-1">
            <v-row class="m-0 p-0">
              <v-tooltip left>
                <template v-slot:activator="{ on }">
                  <div v-on="on">
                    <v-btn
                      class="mt-5 mr-1 ml-2"
                      v-on:click="saveInvoice"
                      :disabled="InvoiceIncomplete"
                      color="success"
                      >Save Invoice</v-btn
                    >
                  </div>
                </template>
                <span>Left tooltip</span>
              </v-tooltip>
              <v-select
                :disabled="InvoiceIncomplete"
                style="max-width:50%"
                background-color="error"
                dark
                offset-y
                class="mt-5 p-0 ml-auto"
                :items="exportItems"
                label="Export"
                v-model="download"
                solo
                @input="downloadFiles"
                dense
              >
                <template v-slot:selection>
                  <span style="max-width:25%" class="text-white">
                    Export
                  </span>
                </template>
              </v-select>
            </v-row>
          </v-container>

          <!-- <b-button
              @click="showCustomer(null, false)"
              class="margin navLinks navButtonMargin"
              size="lg"
              variant="success"
              >Add Customer</b-button
            > -->
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
    <v-col>
      <v-row>
        <v-col cols="12" md="6">
          <v-menu
            ref="menu1"
            v-model="menu1"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date_created"
                label="Invoice Date"
                hint="MM/DD/YYYY format"
                rounded
                clearable
                outlined
                append-icon="mdi-calendar"
                v-bind="attrs"
                @blur="date = parseDate(dateFormatted)"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date_created"
              no-title
              @input="menu1 = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="12" md="6">
          <v-menu
            ref="menu1"
            v-model="menu2"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date_due"
                label="Date Due"
                clearable
                hint="MM/DD/YYYY format"
                rounded
                outlined
                append-icon="mdi-calendar"
                v-bind="attrs"
                @blur="date = parseDate(date_due)"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date_due"
              no-title
              @input="menu2 = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col>
          <v-card>
            <v-card-title>
              <v-row justify="space-around">
                <v-row class="w-50 m-0 p-0">
                  <v-text-field
                    v-model="search"
                    class="mb-0 mt-2 m-0 px-4 py-0 "
                    clearable
                    label="Search"
                    single-line
                    hide-details
                  ></v-text-field>
                </v-row>

                <v-row class="p-0 m-0 w-25" justify="space-around"
                  ><v-autocomplete
                    clearable
                    class="mb-0 mt-2 m-0 mx-6 py-0"
                    label="Add Customer"
                    item-value="name"
                    return-object
                    hide-details
                    v-model="customer"
                    item-text="name"
                    :items="customers"
                    flat
                  >
                  </v-autocomplete>
                  <AddCustomer
                    :create="true"
                    :edit="edit"
                    :dialog="dialog"
                    :customer="customer"
                    @addedCustomer="addedCustomer(customer)"
                    class="mt-2 navLinks navButton navButtonMargin"
                  ></AddCustomer
                ></v-row>
              </v-row>
            </v-card-title>
            <v-data-table :headers="headers" :items="items" :search="search">
              <template v-slot:item.quantity="{ item }">
                <v-col align-content-center id="detailsMenu" class="m-0 p-0">
                  <v-text-field
                    class="m-0 p-0"
                    outlined
                    type="number"
                    v-model="item.quantity"
                  ></v-text-field>
                </v-col>
              </template>
              <template v-slot:item.name="{ item }">
                <v-col align-content-center class="m-0 p-0">
                  <v-text-field
                    v-if="!item.product"
                    class="m-0 p-0"
                    outlined
                    type="text"
                    v-model="item.name"
                  ></v-text-field>
                  <div v-else>{{ item.name }}</div>
                </v-col>
              </template>
              <template v-slot:item.price="{ item }">
                <div>
                  <v-text-field
                    outlined
                    type="number"
                    v-model="item.price"
                  ></v-text-field>
                </div>
              </template>
              <template v-slot:item.total="{ item }">
                <div>${{ item.total.toLocaleString() }}</div>
              </template>
              <template v-slot:item.actions="{ item }">
                <span
                  ><v-icon @click="deleteItem(item)">
                    mdi-delete
                  </v-icon></span
                >
              </template>
              <template v-slot:body.append>
                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td>
                    <v-text-field
                      append-icon="mdi-percent-outline"
                      v-model="tax"
                      max="100"
                      label="Tax"
                      type="number"
                      class="mt-2"
                      outlined
                    ></v-text-field>
                  </td>
                  <td></td>
                </tr>
                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td>
                    <AddItem @addItem="addItem" :products="products"></AddItem>
                  </td>
                  <td></td>
                </tr>
                <tr>
                  <td></td>
                  <td></td>
                  <td class="text-right">Subtotal:</td>
                  <td>${{ subTotal.toLocaleString() }}</td>
                  <td></td>
                </tr>

                <tr>
                  <td></td>
                  <td></td>
                  <td class="text-right">Grand Total:</td>
                  <td>${{ grandTotal.toLocaleString() }}</td>
                  <td></td>
                </tr>
              </template>
            </v-data-table> </v-card
          ><v-container fluid>
            <v-textarea
              id="notes"
              name="input-7-1"
              label="Notes"
              v-model="notes"
              outlined
              ows="2"
              row-height="15"
              auto-grow
            ></v-textarea>
          </v-container>
        </v-col>
      </v-row>
    </v-col>
  </div>
</template>

<script>
import AddItem from "../components/Invoice/AddItem.vue";
import AddCustomer from "../components/Customer/AddCustomer";

const axios = require("axios");
const productPath = "http://localhost:5000/api/product";
const customerPath = "http://localhost:5000/api/customer";
const invoicePath = "http://localhost:5000/api/invoice";
const transactionPath = "http://localhost:5000/api/transaction";

export default {
  name: "CreateInvoice",
  components: {
    AddItem,
    AddCustomer
  },
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    date_created: null,
    date_due: null,
    exportItems: ["Pdf", "Excel"],
    details: false,
    download: "Download",
    menu1: false,
    title: "Create Customer",
    menu2: false,
    edit: false,
    dialog: false,
    GrandTotal: 0,
    transactions: [],
    createdDate: null,
    dateDue: null,
    customer: {
      id: null,
      name: null,
      address: null
    },
    customers: [],
    currentPage: 1,
    products: [],
    product: {},
    invoices: [],
    perPage: 5,
    tax: 0,
    search: "",
    discount: 0,
    notes: null,
    pageOfItems: [],
    excelFields: ["name", "price", "quantity", "total"],
    headers: [
      { text: "Name", value: "name" },
      { text: "Price", value: "price" },
      { text: "Quantity", value: "quantity" },
      { text: "Total", value: "total" },
      { text: "", value: "actions", sortable: false }
    ],
    items: [
      {
        uniqueId: 0,
        product: true,
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
  }),

  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
    subTotal() {
      let temp = 0;

      this.items.forEach(transaction => {
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
        this.date_created !== null &&
        this.date_due !== null &&
        this.customer != null
      ) {
        return false;
      } else {
        return true;
      }
    },
    rows() {
      return this.items.length;
    }
  },

  watch: {
    date() {
      this.dateFormatted = this.formatDate(this.date);
    }
  },

  methods: {
    async addedCustomer() {
      await this.getCustomers();

      this.customer = this.customers[this.customers.length - 1];
    },

    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${month}/${day}/${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },
    addItem(product) {
      let temp = 0;
      if (this.items.length > 0) {
        temp = this.items[this.items.length - 1].uniqueId + 1;
      } else {
        temp = 0;
      }
      if (product === null) {
        this.inLineTotal();

        this.items.push({
          uniqueId: temp,
          product: false,
          id: 0,
          name: "",
          quantity: 1,
          price: Number(0),
          total: 0
        });
      } else {
        this.items.push({
          uniqueId: temp,
          id: product.id,
          product: true,
          name: product.name,
          quantity: 1,
          price: product.price,
          total: product.price
        });
      }

      this.currentPage = Math.ceil(this.items.length / this.perPage);
    },
    closeProductModal() {
      this.inLineTotal();
      this.$refs["productsModal"].hide();
    },
    deleteItem(item) {
      const index = this.items.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.items.splice(index, 1);
      this.inLineTotal();
    },
    lineTotal(product) {
      return Number((product.price * product.quantity).toFixed(2));
    },
    inLineTotal() {
      let count = 0;
      this.items.forEach(element => {
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
        .then(res => {
          this.products = res.data.products;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
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
    updateInvoice() {
      let temp = {
        date_created: this.createdDate,
        date_due: this.dateDue,
        notes: this.notes,
        customer_id: this.customer.id,
        total: this.grandTotal
      };

      axios
        .put(invoicePath + "/" + this.invoice.id, temp)
        .then(res => {
          alert("Invoice Updated");
          console.log(res);
        })
        .catch(err => {
          console.log(err);
          console.log("Invoice Error");
        });

      var invoiceId = 0;

      axios
        .get(invoicePath)
        .then(res => {
          this.invoices = res.data.invoices;
          console.log(typeof this.invoices);
        })
        .catch(err => {
          console.log(err);
        });

      setTimeout(1000);
      invoiceId = 1;

      if (this.invoices.length > 0) {
        invoiceId = this.invoices[this.invoices.length - 1].id;
      }

      this.items.forEach(item => {
        let temp2 = {
          date_created: this.date_due,
          quantity: item.quantity,
          invoice_id: invoiceId,
          product_id: item.id
        };
        console.log(temp2);
        axios
          .put(transactionPath + "/" + item.id, temp2)
          .then(res => {
            alert("howdy");
            console.log(res);
          })
          .catch(err => {
            console.log(err);
            console.log("Transaction Error");
          });
      });
    },
    saveInvoice() {
      let temp = {
        date_created: this.date_created,
        date_due: this.date_due,
        notes: this.notes,
        customer_id: this.customer.id,
        total: this.grandTotal
      };

      if (this.notes === null) {
        if (confirm("Do you want to add notes")) {
          window.location.hash = "notes";
          return;
        }
      }

      axios.post(invoicePath, temp).then(res => {
        alert("Invoice Saved");
        console.log(res);

        var invoiceId = 1;

        setTimeout(1000);

        axios
          .get(invoicePath)
          .then(res => {
            this.invoices = res.data.invoices;

            console.log("howdyyyyyy" + this.invoices);

            alert(this.invoices.length);

            if (this.invoices.length > 0) {
              alert("invoice");
              invoiceId = this.invoices[this.invoices.length - 1].id;
            }

            console.log(this.invoices[this.invoices.length - 1].id);

            this.items
              .forEach(item => {
                let temp2 = {
                  date_created: this.createdDate,
                  quantity: item.quantity,
                  invoice_id: invoiceId,
                  product_id: item.id
                };

                console.log(temp2);

                axios
                  .post(transactionPath, temp2)
                  .then(res => {
                    alert("howdy");
                    console.log(res);
                  })
                  .catch(err => {
                    console.log(err);
                    console.log("Transaction Error");
                  });
              })
              .catch(err => {
                console.log(err);
                console.log("Invoice Error");
              });
          })
          .catch(err => {
            console.log(err);
          });
      });
    },
    viewInvoice(invoice) {
      this.invoice = invoice;
      this.$refs["viewInvoice"].show();
    }
  },
  created() {
    this.getProducts();
    this.getCustomers();
  }
};
</script>

<style scoped>
.tableHeaderField {
  max-width: 30%;
}
.tax {
  width: 6fvw;
  margin: 0;
  padding: 0;
}
.input-btn-font-family {
  padding: 0;
}
</style>
