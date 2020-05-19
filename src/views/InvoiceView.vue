<template>
  <div class="noMargin w-100">
    <b-container fluid class="noMargin">
      <b-navbar style="height:10vh;" type="dark" variant="info">
        <b-navbar-brand>
          <h1>Invoices</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <router-link class="noMargin" to="/newinvoice"
              ><b-button size="lg" variant="success"
                >New Invoice</b-button
              ></router-link
            >
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <b-row style="padding: 10px;" class="w-100">
        <b-col>
          <b-row>
            <b-col>
              <b-card
                header-bg-variant="white"
                border-variant="success"
                header-tag="header"
                footer-tag="footer"
              >
                <template v-slot:header>
                  <h3 class="mb-0">Completed</h3>
                </template>
                <b-card-text><h4>$ 45,000.00</h4></b-card-text>
              </b-card>
            </b-col>
            <b-col>
              <b-card
                header-bg-variant="white"
                border-variant="danger"
                header-tag="header"
                footer-tag="footer"
              >
                <template v-slot:header>
                  <h3 class="mb-0">Outstanding</h3>
                </template>
                <b-card-text><h4>$ 15,000.00</h4></b-card-text>
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
                <b-form-select
                  v-model="perPage"
                  id="perPageSelect"
                  size="sm"
                  :options="pageOptions"
                >
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
                      <b-form-select-option value="name">Name</b-form-select-option>
                      <b-form-select-option value="date_due">Due Date</b-form-select-option>
                      <b-form-select-option value="created_date">Created Date</b-form-select-option>
                    </b-form-select>
                    <b-form-select
                      v-model="sortDesc"
                      size="sm"
                      :disabled="!sortBy"
                      class="w-25"
                    >
                      <option :value="false">Asc</option>
                      <option :value="true">Desc</option>
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
        sticky-header="60vh"
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
                <b-button variant="primary">Mark As Completed</b-button>
                <div>
                  {{ data.item.date_due }}
                </div>
              </b-col>
              <b-col>
                <div>Total:</div>
                <div>{{ data.item.total | currency }}</div>
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
  </div>
</template>

<script>
const invoicePath = "http://localhost:5000/api/invoice";
const axios = require("axios");

export default {
  name: "InvoiceView",

  data: function() {
    return {
      invoices: [],
      searchInvoices: "",
      totalRows: 1,
      filter: null,
      perPage: 6,
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      currentPage: 1,
      pageOfItems: [],
      invoiceTableFields: [
        {
          key: "list",
          label: "",
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
        })
        .catch(err => {
          console.log(err);
        });
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
