<template>
  <div class="bg-light" style="height: 100vh; overflow: hidden;">
    <b-container class="clear m-0 p-0" fluid>
      <b-navbar class="navigation bg-white" type="light" variant="info">
        <b-navbar-brand>
          <h1>Products</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <v-row>
              <AddProduct
                @close="close"
                :dialog="dialog"
                @addedProduct="addedProduct"
                v-bind:edit="edit"
                v-bind:product="product"
              />
            </v-row>
            <!-- <b-input
              type="text"
              style="width: 45%"
              class="margin navButtonMargin navLinks"
              v-model="searchProduct"
              placeholder="Search"
            ></b-input>
            <b-button
              @click="addProduct(null, false)"
              addProduct
              class="navButtonMargin navLinks"
              size="lg"
              variant="success"
              >Add Product</b-button
            > -->
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <v-column style="height: 90vh">
        <v-card style="height: 90vh; overflow: auto;">
          <v-flex style="overflow: auto;" class="w-100">
            <v-card-title>
              <v-text-field
                v-model="searchProduct"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table
              :headers="tableHeaders"
              :items="products"
              :search="searchProduct"
            >
              <template v-slot:item.actions="{ item }">
                <div>
                  <v-icon small class="mr-2" @click="showProduct(item, true)">
                    mdi-pencil
                  </v-icon>
                  <v-icon small @click="deleteCustomer(item)">
                    mdi-delete
                  </v-icon>
                </div>
              </template>
            </v-data-table>
          </v-flex>
        </v-card>
      </v-column>
      <div v-if="filterProductList == 0"><h1>No Data</h1></div>
      <b-modal
        hide-footer
        title="Product Details"
        centered
        ref="viewProduct"
        size="md"
      >
        <keep-alive>
          <ViewProduct :product="product" />
        </keep-alive>
      </b-modal>
      <b-modal
        hide-footer
        :title="modalName"
        centered
        ref="addProduct"
        id="addProduct"
      >
        <keep-alive>
          <AddProduct
            @addedProduct="addedProduct"
            v-bind:edit="edit"
            v-bind:product="product"
          />
        </keep-alive>
      </b-modal>
    </b-container>
  </div>
</template>

<script>
const axios = require("axios");
const path = "http://localhost:5000/api/product";
import AddProduct from "../components/Products/AddProduct";
// import { BIconThreeDotsVertical } from "bootstrap-vue";
import ViewProduct from "../components/Products/ViewProduct";
export default {
  name: "ProductView",
  components: {
    AddProduct,
    ViewProduct
  },
  data: function() {
    return {
      edit: false,
      dialog: false,
      products: [],
      searchProduct: "",
      product: {
        id: null,
        name: null,
        price: null,
        description: null
      },
      tableHeaders: [
        { text: "Id", value: "id" },
        { text: "Name", value: "name" },
        { text: "Price", value: "price" },
        { text: "Actions", value: "actions", sortable: false }
      ]
      // tableHeaders: [
      //   { text: "Id", value: "id" },
      //   {
      //     text: "Name",
      //     sortable: false,
      //     value: "name",
      //   },
      //   { text: "Address", value: "address" },
      //   { text: "Actions", value: "actions", sortable: false },
      // ],
    };
  },
  methods: {
    addedProduct() {
      this.getProducts();
      this.$refs["addProduct"].hide();
    },

    showProduct(product, bool) {
      this.edit = bool;
      this.dialog = true;
      this.product = product;
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
    close() {
      this.edit = false;
      this.dialog = false;
      this.product = {
        id: null,
        name: null,
        price: null,
        description: null
      };
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
    viewProduct(product) {
      this.product = product;
      this.$refs["viewProduct"].show();
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

<style scoped>
.navButtonMargin {
  margin: 0 5px;
}
.navLinks {
  width: 45%;
  font-size: 20px;
}
.navigation {
  height: 10vh;
}

@media (min-width: 768px) and (max-width: 992px) {
  .navLinks {
    width: 45%;
    font-size: 18px;
  }
}

@media (min-width: 576px) and (max-width: 767px) {
  .navLinks {
    width: 46%;
    font-size: 14px;
  }
}

@media (min-width: 200px) and (max-width: 575px) {
  .navigation {
    height: 15vh;
  }
  .navLinks {
    width: 45%;
    font-size: 12px;
  }
  .navButtonMargin {
    margin: 0px;
  }
}
</style>
