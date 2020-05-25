<template>
  <div class="bg-light h-100">
    <b-col>
      <b-row class="noMargin w-100" align-h="between">
        <b-col>
          <b-row>
            <b-col>
              <b-card
                border-variant="primary"
                header="Number Of Customers"
                header-bg-variant="primary"
                header-text-variant="white"
                align="center"
              >
                <b-card-text>{{ customers.length }}</b-card-text>
              </b-card>
              <b-card
                border-variant="primary"
                header="Number Of Invoices"
                header-bg-variant="primary"
                header-text-variant="white"
                align="center"
              >
                <b-card-text>{{ invoices.length }}</b-card-text>
              </b-card></b-col
            >
            <b-col>
              <b-card
                border-variant="primary"
                header="Number Of Prpducts"
                header-bg-variant="primary"
                header-text-variant="white"
                align="center"
              >
                <b-card-text>{{ products.length }}</b-card-text>
              </b-card>
              <b-card
                border-variant="primary"
                header="Primary"
                header-bg-variant="primary"
                header-text-variant="white"
                align="center"
              >
                <b-card-text
                  >Lorem ipsum dolor sit amet, consectetur adipiscing
                  elit.</b-card-text
                >
              </b-card></b-col
            >
          </b-row>
        </b-col>
        <b-col>
          <b-card
            border-variant="primary"
            header="Primary"
            header-bg-variant="primary"
            header-text-variant="white"
            align="center"
          >
            <RevenueChart></RevenueChart>
          </b-card>
        </b-col>
      </b-row>
    </b-col>
  </div>
</template>

<script>
const axios = require("axios");
const productPath = "http://localhost:5000/api/product";
const customerPath = "http://localhost:5000/api/customer";
const invoicePath = "http://localhost:5000/api/invoice";
const transactionPath = "http://localhost:5000/api/transaction";
import RevenueChart from "../components/Home/revenue.vue";
import Chart from "chart.js";
import planetChartData from "../data/revenue-data.js";

export default {
  name: "Home",
  data: function() {
    return {
      planetChartData,
      customers: [],
      invoices: [],
      products: [],
      transactions: [],
    };
  },
  components: { RevenueChart },
  mounted() {
    this.createChart("planet-chart", this.planetChartData);
  },
  methods: {
    getCustomers() {
      axios
        .get(customerPath)
        .then((res) => {
          console.log(res.data);
          this.customers = res.data.customers;
        })
        .catch((err) => {
          console.log(err.data);
        });
    },
    getProducts() {
      axios
        .get(productPath)
        .then((res) => {
          console.log(res.data);
          this.products = res.data.products;
        })
        .catch((err) => {
          console.log(err.data);
        });
    },
    getInvoices() {
      axios
        .get(invoicePath)
        .then((res) => {
          console.log(res);
          this.invoices = res.data.invoices;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getTransactions() {
      axios
        .get(transactionPath)
        .then((res) => {
          console.log(res.data);
          this.transactions = res.data.transactions;
        })
        .catch((err) => {
          console.log(err.data);
        });
    },
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId);
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
      });
      console.log(myChart);
    },
  },
  computed() {},
  created() {
    this.getCustomers();
    this.getProducts();
    this.getInvoices();
    this.getTransactions();
  },
};
</script>

<style>
.noMargin {
  margin: 0;
  padding: 0;
}
</style>
