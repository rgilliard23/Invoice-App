<template>
  <div class="bg-light">
    <b-container class="clear m-0 p-0 fullHeight" fluid>
      <b-navbar class="navigation" type="dark" variant="info">
        <b-navbar-brand>
          <h1>Products</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-input
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
            >
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <b-table fixed :fields="productFields" :items="filterProductList">
        <template v-slot:cell(actions)="data">
          <b-dropdown
            v-b-popover.hover.top="'Actions'"
            variant="primary"
            no-caret
            id="dropdown-1"
            text="Options"
            class="m-md-2 bg-transparent"
          >
            <template v-slot:button-content>
              <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
            </template>
            <b-dropdown-group id="dropdown-group-1">
              <b-dropdown-item @click="viewProduct(data.item)"
                >View</b-dropdown-item
              >
              <b-dropdown-item @click="addProduct(data.item, true)"
                >Edit</b-dropdown-item
              >
              <b-dropdown-item @click="deleteProduct(data.item)"
                >Delete</b-dropdown-item
              >
            </b-dropdown-group>
            <!-- <b-button variant="warning" block @click="addProduct(data.item,true)">Edit</b-button>
            <b-button variant="danger" block @click="deleteProduct(data.item)">Delete</b-button>-->
          </b-dropdown>
        </template>
        <!-- <template v-slot:custom-foot v-if="filterProductList.length === 0">
          <tr>
            <td></td>
            <td></td>
            <td>
              <h1>No Data</h1>
            </td>
            <td></td>
          </tr>
        </template> -->
      </b-table>
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
import AddProduct from "/Users/ronaldgilliard/invoice-app-electron/src/components/Products/AddProduct.vue";
import { BIconThreeDotsVertical } from "bootstrap-vue";
import ViewProduct from "../components/Products/ViewProduct";
export default {
  name: "ProductView",
  components: {
    AddProduct,
    ViewProduct,
    BIconThreeDotsVertical,
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
        description: "",
      },
      productFields: [
        { key: "id", label: "Id" },
        { key: "name", label: "Name" },
        { key: "price", label: "Price" },
        { key: "actions", label: "Actions" },
      ],
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
        .then((res) => {
          this.products = res.data.products;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    submitProduct() {
      if (this.edit) {
        axios
          .put(path + "/" + this.product.id, this.product)
          .then((res) => {
            console.log(res.data);
          })
          .catch((error) => {
            console.log(error.data);
          });
        this.$emit("currentTab", "Product");
        console.log("Submitted Product");
        this.edit = false;
      } else {
        axios
          .post(path, this.product)
          .then((res) => {
            console.log(res.data);
          })
          .catch((error) => {
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
          .then((res) => {
            console.log(res.data);
            this.getProducts();
          })
          .catch((error) => {
            console.log(error.data);
          });
      }
    },
  },
  computed: {
    filterProductList() {
      return this.products.filter((item) => {
        return this.searchProduct
          .toLowerCase()
          .split(" ")
          .every((v) => item.name.toLowerCase().includes(v));
      });
    },
    modalName() {
      if (this.edit) {
        return "Edit Product";
      }
      return "Add Product";
    },
  },
  created() {
    this.getProducts();
  },
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
