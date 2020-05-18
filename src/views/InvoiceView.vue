<template>
  <div>
    <b-col>
      <b-navbar style="height:10vh;" type="dark" variant="info">
        <b-navbar-brand>
          <h1>Invoices</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-button size="lg" variant="success">New</b-button>
            <b-button class="margin" size="lg" variant="success"
              >Add Customer</b-button
            >
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <b-input-group>
        <b-input
          v-model="searchInvoices"
          placeholder="Search"
          type="text"
        ></b-input>
      </b-input-group>
      <JwPagination
        :pageSize="8"
        :items="invoices"
        @changePage="onChangePage"
        :labels="customLabels"
      ></JwPagination>
      <b-list-group>
        <b-list-group-item v-for="(invoice, index) in pageOfItems" :key="index">
          <b-row class="w-100" align-h="between">
            <b-col>
              <div>Customer:</div>
              <div>{{ invoice.customer.name }}</div>
            </b-col>
            <b-col>
              <div>INV-00{{ invoice.id }}</div>
            </b-col>
            <b-col>
              <b-button variant="success">Mark As Completed</b-button>
              <div>{{ invoice.date_due | moment("MMMM Do YYYY") }}</div>
            </b-col>
            <b-col>
              <div>Total:</div>
              <div>{{ invoice.total | currency }}</div>
            </b-col>
          </b-row>
        </b-list-group-item>
      </b-list-group>
    </b-col>
  </div>
</template>

<script>
import JwPagination from "jw-vue-pagination";
const invoicePath = "http://localhost:5000/api/invoice";
const axios = require("axios");

export default {
  name: "InvoiceView",
  components: { JwPagination },
  data: function() {
    return {
      invoices: [],
      searchInvoices: "",
      pageOfItems: [],
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
    filterInvoiceList() {
      return this.invoices.filter(item => {
        return this.searchInvoices
          .toLowerCase()
          .split(" ")
          .every(v => 
            item.customer.name.toLowerCase().includes(v)
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

<style></style>
