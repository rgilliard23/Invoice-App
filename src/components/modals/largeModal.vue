<template>
  <div>
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-list-item-title color="dark" dark v-bind="attrs" v-on="on">
          PDF
        </v-list-item-title>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2">
          Privacy Policy
        </v-card-title>
        <v-container>
          <InvoiceTemplate></InvoiceTemplate>
        </v-container>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import InvoiceTemplate from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/InvoiceTemplate.vue";

export default {
  name: "largeModal",
  components: {
    InvoiceTemplate
  }
};
</script>
