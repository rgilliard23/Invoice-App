<template>
  <div>
    <b-container class="clear fullHeight" fluid>
      <b-navbar style="height:10vh;" type="dark" variant="info">
        <b-navbar-brand>
          <h1>Products</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-input type="text" v-model="searchProduct" placeholder="Search"></b-input>
            <b-button
              @click="addProduct(null,false)"
              addProduct
              class="margin"
              size="lg"
              variant="success"
            >Add Product</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <b-table fixed :fields="productFields" :items="filterProductList">
        <template v-slot:cell(actions)="data">
          <b-dropdown no-caret id="dropdown-1" text="Options" class="m-md-2">
            <template v-slot:button-content variant="link">
              <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
            </template>
            <b-dropdown-group id="dropdown-group-1" >
              <b-dropdown-item @click="addProduct(data.item,true)">Edit</b-dropdown-item>
              <b-dropdown-item @click="deleteProduct(data.item)">Delete</b-dropdown-item>
            </b-dropdown-group>
            <!-- <b-button variant="warning" block @click="addProduct(data.item,true)">Edit</b-button>
            <b-button variant="danger" block @click="deleteProduct(data.item)">Delete</b-button>-->
          </b-dropdown>
        </template>
        <template v-slot:custom-foot v-if="filterProductList.length === 0">
          <tr>
            <td></td>
            <td></td>
            <td>
              <h1>No Data</h1>
            </td>
            <td></td>
          </tr>
        </template>
      </b-table>
      <b-modal :title="modalName" centered ref="addProduct" id="addProduct">
        <keep-alive>
          <AddProduct @addedProduct="addedProduct" v-bind:edit="edit" v-bind:product="product" />
        </keep-alive>
      </b-modal>
    </b-container>
  </div>
</template>

<script>
const axios = require("axios");
const path = "http://localhost:5000/api/product";
import AddProduct from "/Users/ronaldgilliard/invoice-app-electron/src/components/Products/AddProduct.vue";
import { BIconThreeDotsVertical } from "bootstrap-vue";

export default {
  name: "ProductView",
  components: {
    AddProduct,
    BIconThreeDotsVertical
  },
  data: function() {
    return {
      edit: false,
      products: [],
      searchProduct: "",
      product: {
        id: 0,
        name: "",
        price: 0,
        description: ""
      },
      productFields: [
        { key: "id", label: "Id" },
        { key: "name", label: "Name" },
        { key: "price", label: "Price" },
        { key: "actions", label: "" }
      ]
    };
  },
  methods: {
    addedProduct() {
      this.getProducts();
      this.$refs["addProduct"].hide();
    },
    addProduct(product, edit) {
      this.product = product;
      this.edit = edit;
      this.$refs["addProduct"].show();
    },
    getProducts() {
      axios
        .get(path)
        .then(res => {
          this.products = res.data.products;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    submitProduct() {
      if (this.edit) {
        axios
          .put(path + "/" + this.product.id, this.product)
          .then(res => {
            console.log(res.data);
          })
          .catch(error => {
            console.log(error.data);
          });
        this.$emit("currentTab", "Product");
        console.log("Submitted Product");
        this.edit = false;
      } else {
        axios
          .post(path, this.product)
          .then(res => {
            console.log(res.data);
          })
          .catch(error => {
            console.log(error.data);
          });
        this.$emit("currentTab", "Product");
        console.log("Submitted Product");
      }
    },
    editProduct(product) {
      this.product = product;
      this.edit = true;
    },
    deleteProduct: function(product) {
      if (confirm("Are You Sure You Want To Delete This Product")) {
        axios
          .delete(path + "/" + product.id)
          .then(res => {
            console.log(res.data);
            this.getProducts();
          })
          .catch(error => {
            console.log(error.data);
          });
      }
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
    },
    modalName() {
      if (this.edit) {
        return "Edit Product";
      }
      return "Add Product";
    }
  },
  created() {
    this.getProducts();
  }
};
</script>

<style>
</style>