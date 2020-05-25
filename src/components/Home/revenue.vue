<template>
  <div>
    <line-chart
      v-if="loaded"
      v-bind:chartdata="chartdata"
      v-bind:options="options"
    ></line-chart>
  </div>
</template>

<script>
import { Bar, mixins } from "vue-chartjs";
import axios from "axios";

export default {
  mixins: [mixins.reactiveData],
  data() {
    return {
      chartData: "",
    };
  },
  extends: Bar,
  mounted() {
    this.renderChart(this.chartData);
  },
  created() {
    axios
      .get(`http://localhost:5000/api/invoice`)
      .then((response) => {
        // JSON responses are automatically parsed.
        const responseData = response.data;
        this.chartData = {
          labels: responseData.map((item) => item.date_due),
          datasets: [
            {
              label: "Daily Students",
              data: responseData.map((item) => item.total),
            },
          ],
        };
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
// import LineChart from "./Chart.vue";
// // import Axios from "axios";
// const invoicePath = "http://localhost:5000/api/invoice";

// export default {
//   name: "RevenueChart",
//   components: { LineChart },
//   data: () => ({
//     loaded: false,
//     chartdata: null,
//     options: {
//       responsive: true,
//       maintainAspectRatio: false,
//     },
//   }),
//   async mounted() {
//     this.loaded = false;
//     try {
//       // await Axios.get(invoicePath).then((res) => {
//       //   console.log("lfhwfehfheohfelh");
//       //   console.log(res.data.invoices);
//       //   this.chartdata = res.data.invoices;
//       //   this.loaded = true;
//       // });
//       const { userlist } = await fetch(invoicePath)
//       this.chartdata = userlist
//       this.loaded = true
//     } catch (e) {
//       console.error(e);
//     }
//   },

// };
</script>
