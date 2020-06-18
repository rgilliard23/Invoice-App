<template>
  <div>
    <v-menu
      v-model="menu"
      :close-on-content-click="false"
      :nudge-width="200"
      offset-x
      offset-y
      left
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on">
          Add Item
        </v-btn>
      </template>

      <v-card raised color="white">
        <v-card-title>
          <div class="w-100 mt-4 m-auto">
            <v-autocomplete
              outlined
              clearable
              v-model="product"
              :items="products"
              :search-input.sync="searchProducts"
              cache-items
              item-value="name"
              item-text="name"
              class="mt-2 filterItems"
              return-object
              hide-no-data
              hide-details
              @change="addItem"
              label="Search For Products"
              justify="between"
            >
              <template slot="item" slot-scope="data">
                <!-- HTML that describe how select should render items when the select is open -->
                <v-row justify-space-around
                  ><v-col> Name: {{ data.item.name }} </v-col>
                  <v-col>
                    Price: ${{ data.item.price.toLocaleString() }}
                  </v-col></v-row
                >
              </template>
            </v-autocomplete>
          </div>
        </v-card-title>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-row justify-center>
            <v-btn @click="addItem" color="success"> Add New</v-btn></v-row
          >
        </v-card-actions>
      </v-card>
    </v-menu>
  </div>
</template>

<script>
export default {
  name: "AddItem",
  props: {
    products: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      dialog: false,
      fav: true,
      menu: false,
      message: false,
      product: null,
      hints: true,
      searchProducts: ""
    };
  },
  methods: {
    addItem() {
      if (this.product === null) this.$emit("addItem", null);
      else this.$emit("addItem", this.product);
      this.product = null;
      this.menu = false;
    }
  }
};
</script>

<style></style>
