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
              <b-button @click="selectProduct(product)" variant="primary">Select Quantity</b-button>
            </b-row>
          </b-list-group-item>
        </b-list-group>
        <b-list-item>
          <b-button @click="showProductList" style="margin-top:10px;" block variant="primary">
            View Product List
            <b-badge variant="light">{{productList.length}}</b-badge>
          </b-button>
          <b-button @click="addToInvoice" block variant="success">Add Products To Invoice</b-button>
        </b-list-item>
        <b-button style="margin-top: 2vh;" variant="info" v-b-modal.addProductModal>Add Product</b-button>
        <b-modal centered id="addProductModal" ref="addProductModal" title="Add Product">
          <AddProductInvoice @addToProductList="addToProductList"/>
        </b-modal>

        <b-modal ref="productListModal" centered id="productListModal" title="Product List">
          <b-list-group>
            <b-list-group-item v-for="(product, index) in productList" :key="index">{{product.name}}</b-list-group-item>
          </b-list-group>
        </b-modal>
        <b-modal
          @ok="addToProductList(product)"
          ref="selectQuantity"
          centered
          id="selectQuantity"
          title="Quantity"
        >
          <b-row>
            <b-col>
              <b-input-group prepend="Select Quantity">
                <b-input v-model="quantity" type="number" min="0" placeholder="0"></b-input>
              </b-input-group>
            </b-col>
          </b-row>
        </b-modal>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import AddProductInvoice from "/Users/ronaldgilliard/invoice-app-electron/src/components/Products/AddProductInvoice.vue";
export default {
  name: "InvoiceProductsModal",
  components: {
    AddProductInvoice
  },
  props: {
    transactions: Array
  },
  data: function() {
    return {
      searchProduct: "",
      productList: [],
      product: {
        name: "",
        description: "",
        price: 0,
        total: 0,
        quantity: 0,
        uniqueId: 0
      },
      quantity: 0,
      products: [
        {
          name: " Nails",
          price: 12.54,
          description: "Long Nails",
          quantity: 0
        },
        { name: " Nails", price: 12.54, description: "Long Nails", quantity: 0 }
      ]
    };
  },
  methods: {
    showProductList() {
      this.$refs["productListModal"].show();
    },
    selectProduct(product) {
      this.product.name = product.name;
      this.product.address = product.address;
      this.product.description = product.description;
      this.product.price = product.price;
      this.$refs["selectQuantity"].show();
    },
    addToInvoice() {
      if (this.productList.length > 0) {
        this.productList.forEach(element => {
          this.transactions.push({
            name: element.name,
            price: element.price,
            description: element.description,
            quantity: element.quantity,
            total: element.total
          });
        });
        this.$emit("closeProductModal");
      }
    },
    addToProductList(product) {
      var temp;
      if (this.productList.length > 0) {
        let count = 0;
        this.products.forEach(element => {
          element.uniqueId = count;
          count++;
        });
        temp = this.productList[this.productList.length - 1].uniqueId + 1;
      } else {
        temp = 0;
      }
      if(product.quantity === 0){
        product.quantity = this.quantity;
      }
      
      this.productList.push({
        uniqueId: temp,
        quantity: product.quantity,
        name: product.name,
        price: product.price,
        description: product.description,
        total: product.quantity * product.price,
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