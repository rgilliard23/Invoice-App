<template>
  <div>
    <b-row>
      <b-col>
        <b-list-group>
          <b-list-group-item v-for="product in products" :key="product">
            <b-row class="w-100" align-h="around">
              {{product.name}}
              <b-button variant="primary">Select Quantity</b-button>
            </b-row>
          </b-list-group-item>
        </b-list-group>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: "InvoiceProductsModal",
  data: function() {
    return {
      products: [{ name: " Nails", price: 12.54, description: "Long Nails" },{ name: " Nails", price: 12.54, description: "Long Nails" }]
    };
  }
};
</script>

<style>
</style>