<template>
  <v-col>
    <v-card class="elevation-2">
      <h1 class="text-center mt-2 headline">Overview</h1>
      <v-card-text>
        <v-row justify="space-around">
          <v-col>
            <h3>Customer:</h3>
            <h3 class="text-primary">{{ invoice.customer.name }}</h3>
          </v-col>
          <v-col>
            <h4>
              Status:
            </h4>
            <div v-if="invoice.completed">
              <v-btn text color="success" x-large>Completed</v-btn>
            </div>
            <div v-else>
              <v-btn text color="error" x-large>Unpaid</v-btn>
            </div>
          </v-col>
          <v-col>
            <h4>
              Total:
            </h4>
            <h4>${{ invoice.total.toLocaleString() }}</h4>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
    <v-timeline>
      <v-timeline-item color="primary" large>
        <template v-slot:icon>
          <v-avatar>
            <v-icon color="white">mdi-pencil</v-icon>
          </v-avatar>
        </template>
        <v-card class="elevation-2">
          <v-card-text>
            <v-row justify="">
              <v-col cols="7" class="p-0 m-0">
                <h3 class="headline">Created:</h3>
                <h4>{{ invoice.date_created | moment("MMM Do YYYY") }}</h4>
              </v-col>
              <v-col cols="5" align-center
                ><v-btn color="success" class="m-0" @click="editInvoice"
                  >Edit Invoice</v-btn
                >
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-timeline-item>
      <v-timeline-item color="primary" large>
        <template v-slot:icon>
          <v-avatar>
            <v-icon color="white">mdi-send</v-icon>
          </v-avatar>
        </template>
        <v-card class="elevation-2">
          <v-card-text>
            <h3>Send Invoice</h3>
            <v-btn color="success" class="mt-3" @click="sendInvoice"
              >Send Invoice</v-btn
            >
          </v-card-text>
        </v-card>
      </v-timeline-item>
      <v-timeline-item color="primary" large>
        <template v-slot:icon>
          <v-avatar>
            <v-icon color="white">mdi-download</v-icon>
          </v-avatar>
        </template>
        <v-card class="elevation-2">
          <v-card-text>
            <h3>Download</h3>
            <v-btn color="success" class="mt-3" @click="editInvoice"
              >Export Invoice</v-btn
            >
          </v-card-text>
        </v-card>
      </v-timeline-item>
    </v-timeline>
  </v-col>
</template>
<script>
export default {
  name: "ViewInvoice",
  props: {
    invoice: {
      type: Object,
      default: null,
    },
  },
  data: function() {
    return {};
  },
  methods: {
    editInvoice() {
      this.$router.push({
        name: "Create Invoice",
        params: { invoice: this.invoice },
      });
    },
  },
};
</script>
