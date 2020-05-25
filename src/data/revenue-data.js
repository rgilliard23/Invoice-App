//**** Data for chart on Home Page displaying the amount earned per month ****/

const invoicePath = "http://localhost:5000/api/invoice";
const axios = require("axios");
import Vue from 'vue'
export var invoices = [
    
];

new Vue({
    data: function(){
        return {
            invoices: []
        }
    },
    methods: {
        getInvoices(){
            axios.get(invoicePath).then(res => {
                this.invoices = res.data.invoices
            }).catch(err => {
                console.log(err.data);
            });
        }
    },
})

export const planetChartData = {
  type: "line",
  data: {
    labels: [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "November",
      "December",
    ],
    datasets: [
      {
        // one line graph
        label: "Number of Moons",
        data: [0, 0, 1, 2, 67, 62, 27, 14, 10, 7],
        backgroundColor: [
          "rgba(54,73,93,.5)", // Blue
          "rgba(54,73,93,.5)",
          "rgba(54,73,93,.5)",
          "rgba(54,73,93,.5)",
          "rgba(54,73,93,.5)",
          "rgba(54,73,93,.5)",
          "rgba(54,73,93,.5)",
          "rgba(54,73,93,.5)",
        ],
        borderColor: [
          "#36495d",
          "#36495d",
          "#36495d",
          "#36495d",
          "#36495d",
          "#36495d",
          "#36495d",
          "#36495d",
        ],
        borderWidth: 3,
      },
      {
        // another line graph
        label: "Planet Mass (x1,000 km)",
        data: [4.8, 12.1, 12.7, 6.7, 139.8, 116.4, 50.7, 49.2, 50, 9],
        backgroundColor: [
          "rgba(71, 183,132,.5)", // Green
        ],
        borderColor: ["#47b784"],
        borderWidth: 3,
      },
    ],
  },
  options: {
    responsive: true,
    lineTension: 1,
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
            padding: 25,
          },
        },
      ],
    },
  },
};

export default planetChartData;
