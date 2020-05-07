<template>
  <div>
    <b-row>
      <b-col>
        <b-list-group>
          <b-list-group-item v-for="product in products" :key="product">
            <b-row class="w-100" align-h="between">
              <div>{{product.name}}</div>

              <b-button v-b-modal.selectQuantity variant="primary">Select Quantity</b-button>
            </b-row>
          </b-list-group-item>
        </b-list-group>
        <b-button style="margin-top: 2vh;" variant="info" v-b-modal.addProductModal>Add Product</b-button>
        <b-modal centered id="addProductModal" ref="addProductModal" title="Add Product">
          <AddProduct />
        </b-modal>
        <b-modal centered id="selectQuantity" title="Quantity">
          <b-row>
            <b-col>
              <b-input-group prepend="Select Quantity">
                <b-input type="number" min="0" placeholder="0"></b-input>
              </b-input-group>
            </b-col>
          </b-row>
        </b-modal>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import AddProduct from "/Users/ronaldgilliard/invoice-app-electron/src/components/Products/AddProduct.vue";
export default {
  name: "InvoiceProductsModal",
  components: {
    AddProduct
  },
  data: function() {
    return {
      products: [
        { name: " Nails", price: 12.54, description: "Long Nails" },
        { name: " Nails", price: 12.54, description: "Long Nails" }
      ]
    };
  }
};
</script>

<style>
</style>