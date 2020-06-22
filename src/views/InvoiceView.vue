<template>
  <div class="noMargin w-100" style="height: 100vh; overflow: hidden;">
    <b-container fluid>
      <b-navbar style="height:10vh;" class="navBAR" type="light">
        <b-navbar-brand>
          <h1 class="text-dark">Invoices</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <router-link class="noMargin routerLink" to="/createinvoice">
              <v-btn large flat color="success">New Invoice</v-btn>
            </router-link>
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <b-row class="w-100">
        <b-col>
          <b-row>
            <b-col>
              <b-card
                bg-variant="success"
                text-variant="white"
                class="text-center cardShadow"
              >
                <b-col class="text-left text-uppercase">
                  <b-row align-h="between"
                    ><div>
                      <h1 class="overviewCardText">
                        ${{ invoicesComplete.toLocaleString() }}
                      </h1>
                      <h3 class="overviewCardHeader">completed</h3>
                    </div>
                    <div style="font-size: 4rem;">
                      <b-icon-check-circle
                        class="font-size: 50px;"
                      ></b-icon-check-circle>
                    </div>
                  </b-row>

                  <h1 class="float-right"></h1>
                </b-col>
              </b-card>
            </b-col>
            <b-col>
              <b-card
                bg-variant="danger"
                text-variant="white"
                class="text-center cardShadow"
              >
                <b-col class="text-left text-uppercase">
                  <b-row align-h="between"
                    ><div>
                      <h1 class="overviewCardText">
                        ${{ invoicesOutstanding.toLocaleString() }}
                      </h1>
                      <h3 class="overviewCardHeader">Outstanding</h3>
                    </div>
                    <div style="font-size: 4rem;">
                      <b-icon-exclamation-circle
                        class="font-size: 50px;"
                      ></b-icon-exclamation-circle>
                    </div>
                  </b-row>
                  <h1 class="float-right"></h1>
                </b-col>
              </b-card>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <v-card class="my-2" elevation="0">
        <v-card-title class="">
          <v-container class="p-0" fluid>
            <v-row justify="space-between" class=" cardTitle">
              <v-autocomplete
                clearable
                v-model="customer"
                :items="customersFiltered"
                :search-input.sync="searchCustomers"
                cache-items
                item-value="name"
                item-text="name"
                class="mx-2 filterItems"
                return-object
                hide-details
                label="Search For Customer"
                justify="between"
                outlined
                rounded
              ></v-autocomplete>
              <v-select
                clearable
                placeholder="All Statuses"
                label="Status"
                outlined
                :items="status"
                v-model="Status"
                :menu-props="{ bottom: true, offsetY: true }"
                class="filterItems"
                rounded
              >
                <template v-slot:item="data">
                  <div>
                    {{data.title}}
                  </div>
                </template>
              </v-select>

              <v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    clearable
                    v-model="fromDate"
                    label="From"
                    rounded
                    append-icon="mdi-calendar"
                    v-on="on"
                    class="filterItems mx-2"
                    outlined
                  ></v-text-field>
                </template>
                <v-date-picker v-model="fromDate" scrollable> </v-date-picker>
              </v-menu>
              <v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                class="filterItems"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    clearable
                    rounded
                    v-model="toDate"
                    label="To"
                    append-icon="mdi-calendar"
                    v-on="on"
                    class="filterItems mx-2"
                    outlined
                  ></v-text-field>
                </template>
                <v-date-picker v-model="toDate" scrollable> </v-date-picker>
              </v-menu>
            </v-row>
          </v-container>
          <v-spacer></v-spacer>
        </v-card-title>
        <v-data-table
          :headers="tableHeaders"
          :items="invoices"
          :search="searchInvoices"
        >
          <template v-slot:item.actions="{ item }">
            <div>
              <v-icon small class="mr-2" @click="viewInvoice(item)">
                mdi-eye
              </v-icon>
              <v-icon small class="mr-2" @click="editInvoice(item)">
                mdi-pencil
              </v-icon>

              <v-icon small @click="deleteInvoice(item)">
                mdi-delete
              </v-icon>
            </div>
          </template>
          <template v-slot:item.completed="{ item }">
            <div>
              <v-btn
                v-if="!item.completed"
                readonly
                style="width: 40%;"
                color="error"
                >Unpaid</v-btn
              >
              <v-btn color="success" readonly style="width: 40%;" v-else
                >Completed</v-btn
              >
            </div>
          </template>
        </v-data-table>
      </v-card>
    </b-container>
    <b-modal title="Invoice" hide-footer size="xl" ref="invoice">
      <keep-alive>
        <InvoiceTemplate
          :transactions="transactions"
          :dateDue="invoice.date_due"
          :createdDate="invoice.date_created"
        />
      </keep-alive>
    </b-modal>
    <b-modal hide-footer size="xl" ref="editInvoice">
      <keep-alive>
        <Invoice
          v-bind:invoiceCustomer="customer"
          v-bind:edit="true"
          v-bind:invoice="invoice"
        />
      </keep-alive>
    </b-modal>
  </div>
</template>

<script>
const invoicePath = "http://localhost:5000/api/invoice";
const customerPath = "http://localhost:5000/api/customer";
// const productPath = "http://localhost:5000/api/product";
const axios = require("axios");
import InvoiceTemplate from "../components/Invoice/InvoiceTemplate.vue";
import Invoice from "../components/Invoice/Invoice";
export default {
  name: "InvoiceView",
  components: {
    InvoiceTemplate,
    Invoice
  },
  data: function() {
    return {
      invoices: [],
      invoice: [],
      searchInvoices: "",
      searchCustomers: "",
      transactions: [],
      totalRows: 1,
      filter: null,
      fromDate: "",
      toDate: "",
      perPage: 6,
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      customer: null,
      customers: [],
      customersFiltered: [],
      currentPage: 1,
      pageOfItems: [],
      tableHeaders: [
        { text: "Id", value: "id", sortable: true },
        { text: "Status", value: "completed", sortable: true },
        {
          text: "Due",
          sortable: true,
          value: "date_due"
        },

        { text: "Created", value: "date_created" },
        { text: "Actions", value: "actions", sortable: false }
      ],
      invoiceTableFields: [
        { key: "status", label: "Status" },
        { key: "date_due", label: "Due", formatter: {} },
        { key: "id", label: "Id", sortable: true },
        { key: "customer", label: "Customer" },
        { key: "date_created", label: "Date" },
        {
          key: "total",
          label: "Total",
          formatter: value => {
            return "$" + value.toLocaleString();
          }
        },
        { key: "actions", label: "Actions" }
      ],
      status: [
        { title: "Completed", value: true },
        { title: "Unpaid", value: false }
      ],
      Status: null,
      customLabels: {
        first: "<<",
        last: ">>",
        previous: "<",
        next: ">"
      }
    };
  },
  methods: {
    getCustomers() {
      axios
        .get(customerPath)
        .then(res => {
          this.customers = res.data.customers;
          this.customersFiltered = this.customers;
        })
        .catch(e => {
          console.log(e);
        });
    },
    querySelections(v) {
      // Simulated ajax query
      setTimeout(() => {
        this.customersFiltered = this.customers.filter(e => {
          return (
            (e.name || "").toLowerCase().indexOf((v || "").toLowerCase()) > -1
          );
        });
      }, 100);
    },
    markInvoice(bool, invoice) {
      let temp = {
        date_created: invoice.date_created,
        date_due: invoice.date_due,
        notes: invoice.notes,
        customer_id: invoice.customer.id,
        completed: bool,
        total: invoice.total
      };

      axios
        .put(invoicePath + "/" + invoice.id, temp)
        .then(res => {
          console.log(res.data);
          alert("Invoice Marked");
          this.getInvoices();
        })
        .catch(err => {
          console.log(err.data);
        });
    },
    onChangePage(pageOfItems) {
      // update page of items
      this.pageOfItems = pageOfItems;
    },
    getInvoices() {
      axios
        .get(invoicePath)
        .then(res => {
          console.log(res);
          this.invoices = res.data.invoices;
          this.customer = res.data.invoices.customer;
          this.transactions = res.data.invoices.transactions;
        })
        .catch(err => {
          console.log(err);
        });
    },
    viewInvoice(invoice) {
      this.invoice = invoice;

      this.transactions = [];

      this.invoice.transactions.forEach(element => {
        this.transactions.push({
          price: element.product.price,
          name: element.product.name,
          quantity: element.quantity
        });
      });
      this.$router.push({
        name: "View Invoice",
        params: { invoice: this.invoice }
      });
      // this.$refs["viewInvoice"].show();
    },
    async deleteInvoice(invoice) {
      if (confirm("Are You Sure You Want To Delete This Invoice")) {
        axios
          .delete(invoicePath + "/" + invoice.id)
          .then(res => {
            alert("Invoice Deleted");
            this.getInvoices();
            console.log(res.data);
            axios
              .get(customerPath + "/" + this.customer.id)
              .then(res => {
                this.customer = res.data.customer;
                // this.invoices = res.data.customer.invoices;
              })
              .catch(err => {
                console.log(err.data);
              });
          })
          .catch(err => {
            console.log(err.data);
          });
      }
    },
    editInvoice(invoice) {
      this.invoice = invoice;
      this.customer = invoice.customer;
      this.$router.push({
        name: "Create Invoice",
        params: { invoice: this.invoice }
      });
      // this.$refs["editInvoice"].show();
    }
  },
  filters: {
    currency(number) {
      let temp = Number(number.toFixed(2));
      return temp.toLocaleString();
    }
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter(f => f.sortable)
        .map(f => {
          return { text: f.label, value: f.key };
        });
    },
    invoicesComplete() {
      let temp = 0;
      this.invoices.forEach(element => {
        if (element.completed) {
          temp += element.total;
        }
      });
      return temp;
    },
    invoicesOutstanding() {
      let temp = 0;
      this.invoices.forEach(element => {
        if (!element.completed) {
          temp += element.total;
        }
      });
      return temp;
    },
    rows() {
      return this.invoices.length;
    },
    filterInvoiceList() {
      //   return this.searchInvoices
      //     .toLowerCase()
      //     .split(" ")
      //     .every(
      //       v => item.customer.name.toLowerCase().includes(v)
      //     );
      // }

      let invoices = this.invoices;

      if (this.customer != null) {
        invoices = invoices.filter(
          x =>
            JSON.stringify(x.customer.id) === JSON.stringify(this.customer.id)
        );
        alert(JSON.stringify(this.invoices[0].customer));
      }

      if (this.Status != null) {
        invoices.filter(x => x == this.Status);
      }
      return invoices;
    },
    filterInvoices() {
      let result = [];

      return result;
    }
  },

  watch: {
    searchCustomers(val) {
      val && val !== this.select && this.querySelections(val);
    }
  },
  async created() {
    await this.getInvoices();
    await this.getCustomers();
  }
};
</script>

<style scoped>
.filterItems {
  max-width: 22% !important;
  min-width: 5% !important;
}
.overviewCardHeader {
  font-family: Arial, Helvetica, sans-serif;
  color: rgba(255, 255, 255, 0.87) !important;
}
.overviewCard {
  width: 23%;
}
.overviewCardText {
  color: white;
  text-shadow: horizontal-shadow vertical-shadow blur color;
}
.columnItem {
  margin-top: 5px;
  margin-bottom: 5px;
}
.noMargin {
  margin: 0;
  padding: 0;
}
.routerLink {
  text-decoration: none;
}
</style>
