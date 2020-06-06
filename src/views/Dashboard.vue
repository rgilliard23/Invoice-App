<template>
  <div>
    <b-container style="margin: 0; padding: 0;" class="w-100" fluid>
      <b-row style="margin: 0; padding: 0;">
        <b-col col lg="3" class="w-100 fullHeight m-0 p-0" variant="dark">
          <b-nav
            fill
            pills
            onmouseover="toggleSidebar()"
            type="light"
            style="margin: 0; padding: 0;"
            vertical
            class="w-100 fullHeight bg-dark"
          >
            <b-nav-item class="profile">
              <h1>Invoice App</h1>
            </b-nav-item>
            <hr class="w-75 brandLine" />
            <b-nav-item class="">
              <h3 class="text-primary">
                <b-row class=" w-100 m-auto" align-h="center">
                  <span class="marginNavItems">
                    <b-icon-house></b-icon-house>
                  </span>
                  <li
                    :class="[
                      currentPage.includes('dashboard') ? activeClass : ''
                    ]"
                  >
                    <router-link class="noMargin link text-light" to="/home">
                      Home</router-link
                    >
                  </li>
                </b-row>

                <!-- <span>Invoice</span> -->
              </h3>
            </b-nav-item>
            <b-nav-item class="">
              <h3 class="text-primary">
                <span>
                  <span><b-icon-people></b-icon-people></span>
                </span>
                <router-link class="noMargin link text-light" to="/customer">
                  Customers</router-link
                >
                <!-- <span>Invoice</span> -->
              </h3>
            </b-nav-item>
            <b-nav-item class="">
              <h3 class="text-primary">
                <b-row class=" w-100 m-auto" align-h="center">
                  <span class="marginNavItems">
                    <b-icon-layers></b-icon-layers>
                  </span>
                  <router-link class="noMargin link text-light" to="/product">
                    Products
                  </router-link>
                </b-row>
                <!-- <span>Invoice</span> -->
              </h3>
            </b-nav-item>
            <b-nav-item class="">
              <h3 class="text-primary">
                <b-row class=" w-100 m-auto" align-h="center">
                  <span class="marginNavItems">
                    <b-icon-archive-fill></b-icon-archive-fill>
                  </span>
                  <router-link class="link text-light" to="/">
                    Invoices</router-link
                  >
                </b-row>
              </h3>
            </b-nav-item>
          </b-nav>
        </b-col>
        <b-col col lg="9" class="clear fullHeight">
          <!-- <keep-alive>
            <component v-bind:is="currentTabComponent" />
          </keep-alive> -->
          <router-view class="overflow-scroll"></router-view>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import {
  BIconPeople,
  BIconHouse,
  BIconLayers,
  BIconArchiveFill
} from "bootstrap-vue";
export default {
  name: "Dashboard",
  components: {
    BIconPeople,
    BIconHouse,
    BIconLayers,
    BIconArchiveFill
  },
  data: function() {
    return {
      activeClass: "active"
    };
  },
  computed: {
    currentPage() {
      return this.$route.path;
    }
  },
  methods: {
    toggleSideBar() {
      console.log("opening");
    }
  }
};
</script>

<style scoped>
.brandLine {
  border: 1px solid white;
}

.listRow {
  width: 45%;
}
/* a.router-link-active {
  border-left-color: orange;
  color: red;
} */
.noMargin {
  margin: 0;
  padding: 0;
}
.marginNavItems {
  margin: 0 5px;
}
.active{
  color: red !important;
}
.profile {
  margin-top: 1vh;
  height: 8vh;
  max-height: 8vh;
}
.sidebarItems {
  height: 15vh;
  padding: 3vh;
  color: white;
}
.sidebarItems:hover {
  background: #495057;
  color: #17a2b8;
}
.link:hover {
  text-decoration: none;
}
</style>
