<template>
  <div class="noMargin h-100 w-100">
    <b-container fluid class="noMargin">
      <b-navbar style="height:10vh;" type="dark" variant="info">
        <b-navbar-brand>
          <h1>Invoices</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <router-link class="noMargin" to="/newinvoice"
              ><b-button size="lg" variant="success">New Invoice</b-button>
            </router-link>
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <b-row style="padding: 10px;" class="w-100">
        <b-col>
          <b-row>
            <b-col>
              <!-- <b-card
                header-bg-variant="white"
                header-tag="header"
                footer-tag="footer"
                bg-variant="success"
              >
                <template v-slot:header>
                  <h3 class="mb-0 text-success">Completed</h3>
                </template>
                <b-card-text class="text-white"><h4>$ 45,000.00</h4></b-card-text>
              </b-card> -->
              <b-card
                bg-variant="success"
                text-variant="white"
                class="text-center"
              >
                <template v-slot:header>
                  <h4 class="mb-0">Completed</h4>
                </template>
                <b-card-text
                  ><h5>$ {{ invoicesComplete }}</h5></b-card-text
                >
              </b-card>
            </b-col>
            <b-col>
              <!-- <b-card
                header-bg-variant="white"
                header-tag="header"
                footer-tag="footer"
              >
                <template v-slot:header>
                  <h3 class="mb-0">Outstanding</h3>
                </template>
                <b-card-text><h4>$ 15,000.00</h4></b-card-text>
              </b-card> -->
              <b-card
                bg-variant="danger"
                text-variant="white"
                class="text-center"
              >
                <template v-slot:header>
                  <h4 class="mb-0">Outstanding</h4>
                </template>
                <b-card-text
                  ><h5>$ {{ invoicesOutstanding }}</h5></b-card-text
                >
              </b-card>
            </b-col>
          </b-row>
          <b-input-group>
            <b-input
              class="columnItem"
              v-model="filter"
              placeholder="Search"
              type="text"
            ></b-input>
          </b-input-group>
          <b-row>
            <b-col>
              <b-form-group
                label="Per page"
                label-cols-sm="6"
                label-cols-md="4"
                label-cols-lg="3"
                label-align-sm="right"
                label-size="sm"
                label-for="perPageSelect"
                class="mb-0"
              >
                <b-form-select v-model="perPage" id="perPageSelect" size="sm">
                  <!-- These options will appear after the ones from 'options' prop -->
                  <b-form-select-option value="5">5</b-form-select-option>
                  <b-form-select-option value="10">10</b-form-select-option>
                  <b-form-select-option value="15"
                    >15</b-form-select-option
                  ></b-form-select
                >
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group
                label="Sort"
                label-cols-sm="3"
                label-align-sm="right"
                label-size="sm"
                label-for="sortBySelect"
                class="mb-0"
              >
                <b-input-group size="sm">
                  <b-form-select
                    v-model="sortBy"
                    id="sortBySelect"
                    class="w-75"
                  >
                    <template v-slot:first>
                      <option value="">-- none --</option>
                    </template>
                    <b-form-select-option value="name"
                      >Name</b-form-select-option
                    >
                    <b-form-select-option value="date_due"
                      >Due Date</b-form-select-option
                    >
                    <b-form-select-option value="created_date"
                      >Created Date</b-form-select-option
                    >
                  </b-form-select>
                  <b-form-select
                    v-model="sortDesc"
                    size="sm"
                    :disabled="!sortBy"
                    class="w-25"
                  >
                    <option :value="false">Ascending</option>
                    <option :value="true">Descending</option>
                  </b-form-select>
                </b-input-group>
              </b-form-group>
            </b-col>
          </b-row>
        </b-col>
      </b-row>

      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        align="fill"
        aria-controls="my-table"
      ></b-pagination>
      <b-table
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :filter="filter"
        :current-page="currentPage"
        :per-page="perPage"
        borderless
        sticky-header="61vh"
        style="height: 61vh;"
        :fields="invoiceTableFields"
        small
        :items="invoices"
      >
        <template v-slot:cell(list)="data">
          <b-list-group-item>
            <b-row class="w-100" align-h="between">
              <b-col>
                <div>Customer:</div>
                <div>{{ data.item.customer.name }}</div>
              </b-col>
              <b-col>
                <div>INV-00{{ data.item.id }}</div>
              </b-col>
              <b-col>
                <b-button
                  variant="primary"
                  @click="markInvoice(false, data.item)"
                  v-if="data.item.completed"
                  >Mark As Incomplete</b-button
                >
                <b-button
                  variant="primary"
                  @click="markInvoice(true, data.item)"
                  v-else
                  >Mark As Complete</b-button
                >
                <div>
                  {{ data.item.date_due }}
                </div>
              </b-col>
              <b-col>
                <div>Total:</div>
                <div>{{ data.item.total | currency }}</div>
              </b-col>
              <b-col>
                <b-dropdown
                  variant="primary"
                  no-caret
                  id="dropdown-1"
                  text="Options"
                  class="m-md-2 bg-transparent"
                >
                  <template v-slot:button-content>
                    <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
                  </template>
                  <b-dropdown-group id="dropdown-group-1">
                    <b-dropdown-item @click="viewInvoice(data.item)"
                      >View</b-dropdown-item
                    >
                    <b-dropdown-item @click="editInvoice(data.item)"
                      >Edit</b-dropdown-item
                    >

                    <b-dropdown-item @click="deleteInvoice(data.item)"
                      >Delete</b-dropdown-item
                    >
                  </b-dropdown-group>
                  <!-- <b-button variant="warning" block @click="addProduct(data.item,true)">Edit</b-button>
            <b-button variant="danger" block @click="deleteProduct(data.item)">Delete</b-button>-->
                </b-dropdown>
              </b-col>
            </b-row>
          </b-list-group-item>
        </template>
      </b-table>
      <!-- <JwPagination
            class="w-100"
            align="fill"
            :pageSize="8"
            :items="invoices"
            @changePage="onChangePage"
            :labels="customLabels"
          ></JwPagination>
          <b-list-group>
            <b-list-group-item
              v-for="(invoice, index) in pageOfItems"
              :key="index"
            >
              <b-row class="w-100" align-h="between">
                <b-col>
                  <div>Customer:</div>
                  <div>{{ invoice.customer.name }}</div>
                </b-col>
                <b-col>
                  <div>INV-00{{ invoice.id }}</div>
                </b-col>
                <b-col>
                  <b-button variant="primary">Mark As Completed</b-button>
                  <div>{{ invoice.date_due | moment("MMMM Do YYYY") }}</div>
                </b-col>
                <b-col>
                  <div>Total:</div>
                  <div>{{ invoice.total | currency }}</div>
                </b-col>
              </b-row>
            </b-list-group-item>
          </b-list-group> -->
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
  </div>
</template>

<script>
const invoicePath = "http://localhost:5000/api/invoice";
const customerPath = "http://localhost:5000/api/customer";
// const productPath = "http://localhost:5000/api/product";
const axios = require("axios");
import InvoiceTemplate from "../components/Invoice/InvoiceTemplate.vue";

export default {
  name: "InvoiceView",
  components: {
    InvoiceTemplate
  },
  data: function() {
    return {
      invoices: [],
      invoice: [],
      searchInvoices: "",
      transactions: [],
      totalRows: 1,
      filter: null,
      perPage: 6,
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      customer: {},
      currentPage: 1,
      pageOfItems: [],
      invoiceTableFields: [
        {
          key: "list",
          label: "Invoices",
          sortable: true
        }
      ],
      customLabels: {
        first: "<<",
        last: ">>",
        previous: "<",
        next: ">"
      }
    };
  },
  methods: {
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
      // this.$refs["viewInvoice"].show();
      this.$refs["invoice"].show();
    },
    deleteInvoice(invoice) {
      if (confirm("Are You Sure You Want To Delete This Invoice")) {
        axios
          .delete(invoicePath + "/" + invoice.id)
          .then(res => {
            alert("Invoice Deleted");
            console.log(res.data);
            axios
              .get(customerPath + "/" + this.customer.id)
              .then(res => {
                this.customer = res.data.customer;
                this.invoices = res.data.customer.invoices;
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
      this.$refs["editInvoice"].show();
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
      return this.invoices.filter(item => {
        return this.searchInvoices
          .toLowerCase()
          .split(" ")
          .every(
            v => item.customer.name.toLowerCase().includes(v)
            // item.date_cue.toLowerCase().includes(v)
            // item.customer.name.toLowerCase().includes(v);
          );
      });
    }
  },
  created() {
    this.getInvoices();
  }
};
</script>

<style scoped>
.columnItem {
  margin-top: 5px;
  margin-bottom: 5px;
}
.noMargin {
  margin: 0;
  padding: 0;
}
</style>
