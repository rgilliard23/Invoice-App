<template>
  <div>
    <line-chart v-if="loaded" :chartData="chartData" :options="options" />
    <div v-else class="text-center"><h1>No Data</h1></div>
  </div>
</template>

<script>
import LineChart from "./Chart";
import axios from "axios";
var moment = require("moment"); // require
export default {
  props: { invoicesRevenue: { type: Array } },
  components: { LineChart },
  data() {
    return {
      data: [],
      dates: [],
      loaded: false,
      chartData: null,
      revenueTotal: 0
    };
  },
  async mounted() {
    // try{
    // this.loaded = false;
    // this.data = [];
    // await this.invoicesRevenue.forEach(invoice => {
    //   alert(invoice)
    //   if (invoice.completed) {
    //     this.data.push({ x: invoice.date_due, y: invoice.total });
    //     this.revenueTotal += invoice.total;
    //   }
    // });
    // alert(this.data[0].x);
    // const responseData = [
    //   {
    //     label: "Total",
    //     backgroundColor: "green",
    //     data: this.data
    //   }
    // ];

    // this.chartData = {
    //   datasets: responseData,
    //   // labels: response.data.invoices.map(item => item.date_due)
    //   labels: this.data.map(item => moment(item.x, "YYYYMMDD").format("MMM YYYY"))
    //   // labels: dates
    // };
    // this.loaded = true;
    // this.$emit("revenue", this.revenueTotal);

    // } catch(e){
    //   console.log(e);
    // }

    try {
      await axios.get(`http://localhost:5000/api/invoice`).then(response => {
        // let data = [];
        // let dates = [];
        this.revenueTotal = 0;
        this.data = [];
        if (this.invoicesRevenue !== null) {
          this.data = [];
          if (this.invoicesRevenue.length > 0) {
            this.invoicesRevenue.forEach(invoice => {
              alert(invoice.completed);
              if (invoice.completed) {
                this.data.push({ x: invoice.date_due, y: invoice.total });
                this.revenueTotal += invoice.total;
                this.dates.push(
                  moment(invoice.date_due, "YYYYMMDD").format("MMM YYYY")
                );
              }
            });
            this.loaded = true;
          } else {
            this.loaded = false;
          }
        } else {
          response.data.invoices.forEach(invoice => {
            if (invoice.completed) {
              this.data.push({ x: invoice.date_due, y: invoice.total });
              this.revenueTotal += invoice.total;
              this.dates.push(
                moment(invoice.date_due, "YYYYMMDD").format("MMM YYYY")
              );
            }
          });
          this.loaded = true;
        }

        const responseData = [
          {
            label: "Total",
            backgroundColor: "green",
            data: this.data
          }
        ];
        // this.chartData = {
        //   labels: responseData.map((item) => Object.keys(item)[2]),
        //   datasets: [
        //     {
        //       label: "Date Due",
        //       data: responseData.map((item) => item.total)
        //     },
        //   ],
        // };
        this.chartData = {
          datasets: responseData,
          // labels: response.data.invoices.map(item => item.date_due)
          labels: this.data.map(item =>
            moment(item.x, "YYYYMMDD").format("MMM YYYY")
          )
          // labels: dates
        };

        this.$emit("revenue", this.revenueTotal);
      });
    } catch (e) {
      console.log(e);
    }
  },
  watch: {
    invoicesRevenue: function() {
      try {
        axios.get(`http://localhost:5000/api/invoice`).then(response => {
          // let data = [];
          // let dates = [];
          this.revenueTotal = 0;
          this.data = [];
          if (this.invoicesRevenue !== null) {
            this.data = [];
            alert(this.invoicesRevenue > 0);
            if (this.invoicesRevenue.length > 0) {
              this.invoicesRevenue.forEach(invoice => {
                alert(invoice.completed);
                if (invoice.completed) {
                  this.data.push({ x: invoice.date_due, y: invoice.total });
                  this.revenueTotal += invoice.total;
                  this.dates.push(
                    moment(invoice.date_due, "YYYYMMDD").format("MMM YYYY")
                  );
                }
              });
              this.loaded = true;
            } else {
              this.loaded = false;
            }
          } else {
            response.data.invoices.forEach(invoice => {
              if (invoice.completed) {
                this.data.push({ x: invoice.date_due, y: invoice.total });
                this.revenueTotal += invoice.total;
                this.dates.push(
                  moment(invoice.date_due, "YYYYMMDD").format("MMM YYYY")
                );
              }
            });
            this.loaded = true;
          }

          const responseData = [
            {
              label: "Total",
              backgroundColor: "green",
              data: this.data
            }
          ];
          // this.chartData = {
          //   labels: responseData.map((item) => Object.keys(item)[2]),
          //   datasets: [
          //     {
          //       label: "Date Due",
          //       data: responseData.map((item) => item.total)
          //     },
          //   ],
          // };
          this.chartData = {
            datasets: responseData
            // labels: response.data.invoices.map(item => item.date_due)
            // labels: this.data.map(item =>
            //   moment(item.x, "YYYYMMDD").format("MMM YYYY")
            // )
            // labels: dates
          };

          this.$emit("revenue", this.revenueTotal);
        });
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
