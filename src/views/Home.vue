<template>
  <div class="bg-light h-100">
    <b-navbar style="height:10vh;" type="dark" variant="info">
      <b-navbar-brand class="text-center">
        <h1>Home</h1>
      </b-navbar-brand>
    </b-navbar>
    <b-col>
      <b-row class="noMargin w-100" align-h="between">
        <b-col>
          <b-card
            style="margin-top: 2vh;"
            border-variant="primary"
            header="Overview"
            class="cardShadow"
            header-bg-variant="primary"
            header-text-variant="white"
            align="center"
          >
            <b-row align-h="around"
              ><b-card
                bg-variant="primary"
                class="cardShadow overviewCard"
                text-variant="white"
              >
                <b-col class="text-left text-uppercase">
                  <!-- <b-row>
                    <div class="cardText">Total Customers:</div>
                    <div>{{ customers.length }}</div>
                  </b-row> -->
                  <b-row align-h="between"
                    ><div>
                      <h5 class="overviewCardHeader">Customers</h5>
                      <h2 class="overviewCardText">{{ customers.length }}</h2>
                    </div>
                    <div style="font-size: 4rem;">
                      <b-icon-people class="font-size: 50px;"></b-icon-people>
                    </div>
                  </b-row>

                  <h1 class="float-right"></h1> </b-col
              ></b-card>
              <b-card
                class="productCard overviewCard cardShadow"
                text-variant="white"
              >
                <b-col class="text-left text-uppercase">
                  <b-row align-h="between"
                    ><div>
                      <h5 class="overviewCardHeader">Products</h5>
                      <h1 class="overviewCardText">{{ products.length }}</h1>
                    </div>
                    <div style="font-size: 4rem;">
                      <b-icon-layers></b-icon-layers>
                    </div>
                  </b-row> </b-col
              ></b-card>
              <b-card
                bg-variant="success"
                class="cardShadow overviewCard"
                text-variant="white"
              >
                <b-col class="text-left text-uppercase">
                  <b-row align-h="between">
                    <div>
                      <h5 class="overviewCardHeader">Completed</h5>
                      <h1 class="overviewCardText">
                        ${{ invoicesComplete.toLocaleString() }}
                      </h1>
                    </div>
                    <div style="font-size: 4rem;">
                      <b-icon-check-circle></b-icon-check-circle>
                    </div>
                  </b-row> </b-col
              ></b-card>
              <b-card
                bg-variant="danger"
                class="cardShadow overviewCard"
                text-variant="white"
              >
                <b-col class="text-left text-uppercase">
                  <b-row align-h="between">
                    <div>
                      <h5 class="overviewCardHeader">Outstanding</h5>
                      <h1 class="overviewCardText">
                        ${{ invoicesOutstanding.toLocaleString() }}
                      </h1>
                    </div>
                    <div style="font-size: 4rem;">
                      <b-icon-exclamation-circle></b-icon-exclamation-circle>
                    </div>
                  </b-row> </b-col></b-card
            ></b-row>
          </b-card>
        </b-col> </b-row
      ><b-card
        style="margin-top: 2vh;"
        header="Revenue"
        border-variant="primary"
        header-bg-variant="primary"
        header-text-variant="white"
        class="cardShadow"
        align="center"
        ><b-col>
          <b-select @change="filterRevenueChart($event, false)">
            <b-select-option value="1">Week</b-select-option>
            <b-select-option value="2">Month</b-select-option>
            <b-select-option value="3">Year</b-select-option>
          </b-select>
          <b-row style="margin-top: 1vh;">
            <b-col
              ><b-input-group size="lg" prepend="From:">
                <b-form-datepicker
                  v-on:input="filterRevenueChart(event, true)"
                  id="datepicker-dateformat1"
                  v-model="date1"
                  :max="date2"
                  ref="date1"
                  :date-format-options="{
                    year: 'numeric',
                    month: 'short',
                    day: '2-digit',
                    weekday: 'short'
                  }"
                  locale="en"
                ></b-form-datepicker> </b-input-group
            ></b-col>
            <b-col
              ><b-input-group size="lg" prepend="To:">
                <b-form-datepicker
                  v-on:input="filterRevenueChart(event, true)"
                  id="datepicker-dateformat1"
                  :min="date1"
                  v-model="date2"
                  :date-format-options="{
                    year: 'numeric',
                    month: 'short',
                    day: '2-digit',
                    weekday: 'short'
                  }"
                  locale="en"
                ></b-form-datepicker> </b-input-group></b-col
          ></b-row>
        </b-col>
        <b-row
          ><b-col>
            <RevenueChart
              :invoicesRevenue="invoicesRevenue"
              @revenue="revenueTotal"
              class="revenueChart"
            ></RevenueChart></b-col
          ></b-row
        >
      </b-card>
    </b-col>
  </div>
</template>

<script>
const axios = require("axios");
const productPath = "http://localhost:5000/api/product";
const customerPath = "http://localhost:5000/api/customer";
const invoicePath = "http://localhost:5000/api/invoice";
const transactionPath = "http://localhost:5000/api/transaction";
var moment = require("moment"); // require

import RevenueChart from "../components/Home/revenue.vue";
import Chart from "chart.js";
import planetChartData from "../data/revenue-data.js";

export default {
  name: "Home",
  data: function() {
    return {
      revenue: 0,
      invoicesRevenue: null,
      planetChartData,
      date1: null,
      date2: null,
      customers: [],
      invoices: [],
      products: [],
      transactions: []
    };
  },
  components: { RevenueChart },
  mounted() {
    this.createChart("planet-chart", this.planetChartData);
    this.$refs["date1"]
      .datepicker()
      .on("changeDate", this.filterRevenueChart(null, true));
  },
  methods: {
    getCustomers() {
      axios
        .get(customerPath)
        .then(res => {
          console.log(res.data);
          this.customers = res.data.customers;
        })
        .catch(err => {
          console.log(err.data);
        });
    },
    getProducts() {
      axios
        .get(productPath)
        .then(res => {
          console.log(res.data);
          this.products = res.data.products;
        })
        .catch(err => {
          console.log(err.data);
        });
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
    },
    filterRevenueChart(event, bool) {
      if (!bool) {
        this.date1 = null;
        this.date2 = null;
        this.invoicesRevenue = null;
      }
      if (this.date1 != null && this.date2 != null) {
        this.invoicesRevenue = [];
        this.invoices.forEach(element => {
          // alert(moment(element.date_due).isBetween(this.date1, this.date2));
          if (moment(element.date_due).isBetween(this.date1, this.date2)) {
            this.invoicesRevenue.push(element);
          }
        });
      } else {
        switch (Number(event)) {
          case 1:
            alert("1");
            break;
          case 2:
            break;
          case 3:
            break;
          default:
            break;
        }
      }
    },
    revenueTotal(total) {
      this.revenue = total;
    },

    getTransactions() {
      axios
        .get(transactionPath)
        .then(res => {
          console.log(res.data);
          this.transactions = res.data.transactions;
        })
        .catch(err => {
          console.log(err.data);
        });
    },
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId);
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options
      });
      console.log(myChart);
    }
  },
  computed: {
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
          temp = +element.total;
        }
      });
      return temp;
    }
  },
  watch: {
    date1() {
      this.filterRevenueChart(null, true);
    },
    date2() {
      this.filterRevenueChart(null, true);
    }
  },
  created() {
    this.getCustomers();
    this.getProducts();
    this.getInvoices();
    this.getTransactions();
  }
};
</script>

<style>
.overviewCard {
  width: 23%;
}
.overviewCardHeader {
  font-family: Arial, Helvetica, sans-serif;
  color: rgba(255, 255, 255, 0.87) !important;
}
.overviewCardText {
  color: white;
  text-shadow: horizontal-shadow vertical-shadow blur color;
}
.productCard {
  background-color: darkturquoise;
}
.customerCard {
  background-color: gold;
}
.cardText {
  margin: 0 5px;
}
.revenue {
  margin: auto;
}
.noMargin {
  margin: 0;
  padding: 0;
}
.revenueChart {
  max-width: 100%;
  max-height: 50%;
}
</style>
