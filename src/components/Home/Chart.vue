<script>
import { Line, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;
export default {
  mixins: [reactiveProp],
  extends: Line,
  data: function() {
    return {
      options: {
        responsive: false,
        scales: {
          xAxes: [
            {
              type: "time",
              time: {
                displayFormats: {
                        quarter: 'MMM YYYY'
                    }
              },
              // tooltipFormat: "MMMM YYYY",
              offset: true,
              // distribution: "linear"
            }
          ],
          // yAxes: [
          //   {
          //     type: "linear",
          //     ticks: {
          //       reverse: false,
          //       beginAtZero: true
          //     }
          //   }
          // ]
        }
      }
    };
  },
  mounted() {
    this.renderChart(this.chartData, this.options);
  }
};
</script>

<style></style>
