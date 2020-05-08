<template>
  <div>
    <b-row>
      <b-col>
        <b-input-group prepend="Search">
          <b-input type="text" v-model="searchProduct" placeholder="Search Product"></b-input>
        </b-input-group>

        <b-list-group class="list-group-overflow" style="margin-top: 10px;">
          <b-list-group-item v-for="product in filterProductList" :key="product">
            <b-row class="w-100" align-h="between">
              <div>{{product.name}}</div>
              <b-button
                v-model="quantity"
                v-b-modal.selectQuantity
                variant="primary"
              >Select Quantity</b-button>
            </b-row>
          </b-list-group-item>
        </b-list-group>
        <b-list-item>
          <b-button style="margin-top:10px;" block variant="primary">
            View Product List
            <b-badge variant="light">4</b-badge>
          </b-button>
        </b-list-item>
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
      searchProduct: "",
      productList: [],
      product: {
        name: "",
        description: "",
        price: 0,
        uniqueId: 0
      },
      quantity: 0,
      products: [
        { name: " Nails", price: 12.54, description: "Long Nails" },
        { name: " Nails", price: 12.54, description: "Long Nails" }
      ]
    };
  },
  methods: {
    addToProductList(product) {
      var temp;
      if (this.productList.length > 0) {
        let count = 0;
        this.products.forEach(element => {
          element.uniqueId = count;
          count++;
        })
        temp = this.productList[this.productList.length - 1].uniqueId + 1;
      } else{
        temp = 0;
      }
        this.productList.push({
          uniqueId: temp,
          quantity: this.quantity,
          name: product.name,
          price: product.price,
          description: product.description
        });
    }
  },
  computed: {
    filterProductList() {
      return this.products.filter(item => {
        return this.searchProduct
          .toLowerCase()
          .split(" ")
          .every(v => item.name.toLowerCase().includes(v));
      });
    }
  }
};
</script>

<style>
.list-group-overflow {
  overflow: scroll;
  max-height: 60vh;
  min-height: 30vh;
}
</style>