<template>
  <div>
    <b-container style="margin: 0; padding: 0;" class="w-100" fluid>
      <b-row style="margin: 0; padding: 0;">
        <b-col
          col
          lg="3"
          class="w-100 fullHeight m-0 p-0"
          variant="dark"
        >
          <b-nav type="light" style="margin: 0; padding: 0;" vertical class="w-100 fullHeight bg-dark">
            <b-list-group-item
              class="profile bg-dark text-light d-flex justify-content-center align-items-center"
            >
              <h1>Howdy</h1>
            </b-list-group-item>
           
            <b-nav-item class="sidebarItems">
              <h3>
                <span>
                  <span><b-icon-people></b-icon-people></span>
                </span>
                <router-link class="noMargin" to="/customer"> Customers</router-link>
                <!-- <span>Invoice</span> -->
              </h3>
            </b-nav-item>
            <b-nav-item class="sidebarItems">
              <h3>
                <span>
                  <span><b-icon-layers></b-icon-layers></span>
                </span>
                <router-link class="noMargin" to="/product">Products</router-link>
                <!-- <span>Invoice</span> -->
              </h3>
            </b-nav-item>
            <b-nav-item class="sidebarItems">
              <h3>
                <span>
                  <b-icon-house></b-icon-house>
                </span>
                <router-link class="noMargin" to="/"> Invoice</router-link>
                <!-- <span>Invoice</span> -->
              </h3>
            </b-nav-item>
            <!-- <b-nav-item
              v-on:click="currentTab = tab"
              v-for="tab in tabs"
              :key="tab"
              class="sidebarItems"
            >
              <b-nav-text v-on:click="currentTab = tab" class="sidebarItems">
                <h3>
                  <span>
                    <b-icon-house></b-icon-house>
                  </span>
                  <span>{{tab}}</span>
                </h3>
              </b-nav-text>
            </b-nav-item> -->
            <!-- <b-nav-item class="sidebarItems">
              <b-nav-text class="sidebarItems">
                <h3><span><b-icon-people></b-icon-people></span><span>Customers</span></h3>
              </b-nav-text>
            </b-nav-item>
            <b-nav-item class="sidebarItems">
              <b-nav-text class="sidebarItems">
                <h3><span><b-icon-layers></b-icon-layers></span><span>Products</span></h3>
              </b-nav-text>
            </b-nav-item>
            <b-nav-item class="sidebarItems">
              <b-nav-text class="sidebarItems">
                <h3><span><b-icon-folder-plus></b-icon-folder-plus></span><span>Create Invoice</span></h3>
              </b-nav-text>
            </b-nav-item>-->
          </b-nav>
        </b-col>
        <b-col col lg="9" class="clear fullHeight">
          <!-- <keep-alive>
            <component v-bind:is="currentTabComponent" />
          </keep-alive> -->
          <router-view></router-view>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// import Invoice from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/Invoice.vue";
// import ProductView from "/Users/ronaldgilliard/invoice-app-electron/src/views/ProductView.vue";
// import CustomerView from "/Users/ronaldgilliard/invoice-app-electron/src/views/CustomerView.vue";
// import InvoiceView from "/Users/ronaldgilliard/invoice-app-electron/src/views/InvoiceView.vue";
// import BIconHouse from "bootstrap-vue";
import { BIconPeople, BIconHouse, BIconLayers,  } from "bootstrap-vue";
export default {
  name: "Dashboard",
  components: {
    // Invoice,
    // ProductView,
    // InvoiceView,
    // CustomerView,
    BIconPeople,
    BIconHouse,
    BIconLayers,

  },
  data: function() {
    return {
      // currentTab: "Products",
      // tabs: ["Customers", "Products", "Create Invoice"]
    };
  },
  computed: {
    // currentTabComponent: function() {
    //   if (this.currentTab === "Products") {
    //     return ProductView;
    //   }
    //   if (this.currentTab === "Customers") {
    //     return CustomerView;
    //   }
    //   return InvoiceView;
    // }
  }
};
</script>

<style scoped>
.noMargin{
    margin: 0;
    padding: 0;
}
.profile {
  height: 10vh;
}
.sidebarItems {
  padding: 3vh;
  color: white;
}
.sidebarItems:hover {
  background: #495057;
  color: #17a2b8;
}
</style>
