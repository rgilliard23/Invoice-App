<template>
  <div>
    <b-container style="" class="w-100 px-0 h-100 " fluid>
      <b-row class="h-100" style="">
        <b-col class="h-100 sidebar bg-primary fullHeight">
          <b-nav fill type="dark" vertical class="w-100 h-100">
            <b-nav-item class="navLogo">
              <h1 class="text-white">Invoice App</h1>
            </b-nav-item>
            <hr class="brandLine" />
            <b-nav-item class="sideBarItem text-left " exact to="/home">
              <h4 class=""><b-icon-house class="icon"></b-icon-house>Home</h4>
            </b-nav-item>
            <b-nav-item class="sideBarItem text-left" exact to="/customer">
              <h4><b-icon-people class="icon"></b-icon-people>Customers</h4>
            </b-nav-item>
            <b-nav-item class="sideBarItem text-left" exact to="/product">
              <h4><b-icon-layers class="icon"></b-icon-layers>Products</h4>
            </b-nav-item>
            <!-- <b-nav-item to="/" class="">
              <h3>
                  <router-link class="link text-light" to="/">
                    <span class="marginNavItems">
                      <b-icon-archive-fill></b-icon-archive-fill>
                    </span>
                    Invoices</router-link
                  >
              </h3>
               <b-icon-archive-fill></b-icon-archive-fill>
            </b-nav-item> -->

            <b-nav-item class="sideBarItem text-left p-0 m-0" exact>
              <h4>
                <v-expansion-panels flat accordion>
                  <v-expansion-panel>
                    <v-expansion-panel-header
                      style="background-color: #6f42c1; color: white;"
                      class="sideBarItem m-0 p-0 w-100"
                    >
                      <template v-slot:actions>
                        <v-icon color="white">mdi-chevron-down</v-icon>
                      </template>
                      <div class="m-0 p-0">
                        <h4>
                          <span
                            ><v-icon class="mr-2" dark
                              >mdi-credit-card-outline</v-icon
                            ></span
                          >Sales
                        </h4>
                      </div></v-expansion-panel-header
                    >
                    <v-expansion-panel-content
                      style="background-color: #6f42c1; color: white;"
                    >
                      <b-col class="m-0 p-0">
                        <div>
                          <router-link class="text-white pl-2 navLink" to="/"
                            >Invoices</router-link
                          >
                        </div>
                        <div class="mt-2">
                          <router-link class="text-white pl-2 navLink" to="/createinvoice"
                            >Create Invoice</router-link
                          >
                        </div>
                      </b-col>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>

                <!-- <span
                  ><b-icon-archive-fill class="icon"></b-icon-archive-fill
                ></span>
                Invoices -->

                <!-- <v-expansion-panel
                  style="background-color: #6f42c1; color: white;"
                  class="sideBarItem m-0 p-0 w-100"
                >
                  <template v-slot:actions>
                    <v-icon dark class="color: white;">mdi-chevron-up</v-icon>
                  </template>
                  <v-expansion-panel-header>
                    <div>
                      <h4>
                        <span
                          ><b-icon-credit-card
                            class="icon"
                          ></b-icon-credit-card></span
                        >Sales
                      </h4>
                    </div></v-expansion-panel-header
                  >
                  <v-expansion-panel-content>
                    <router-link to="/">
                      <span
                        ><b-icon-archive-fill class="icon"></b-icon-archive-fill
                      ></span>
                      Invoices</router-link
                    >
                  </v-expansion-panel-content>
                </v-expansion-panel> -->
              </h4>
            </b-nav-item>
          </b-nav>
        </b-col>
        <b-col col class=" h-100">
          <router-view class="fullHeight overflow-scroll"></router-view>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { BIconPeople, BIconHouse, BIconLayers } from "bootstrap-vue";
export default {
  name: "Dashboard",
  components: {
    BIconPeople,
    BIconHouse,
    BIconLayers,
  },
  data: function() {
    return {
      // activeClass: "active"
    };
  },
  computed: {
    currentPage() {
      return this.$route.path;
    },
  },
  methods: {
    toggleSideBar() {
      console.log("opening");
    },
  },
};
</script>

<style scoped>
.boxShadow {
  box-shadow: inset 5px 0 9px 0px rgba(0, 0, 0, 0.4) !important;
  color: black;
  overflow: hidden;
}
.brandLine {
  width: 95%;
  height: 0.1px;
  border: 0.5px solid rgb(137, 137, 137);
}
.sidebar {
  moz-box-shadow: -3px 0 5px 0 #555;
  -webkit-box-shadow: -3px 0 5px 0 #555;
  box-shadow: 4px 0px 5px rgba(0, 0, 0, 0.4);
  width: 20%;
  max-width: 20%;
}
.sidebarText {
  color: rgb(137, 137, 137);
  font-weight: 100 !important;
}
.navLink {
  padding: 0 !important;
}
.active {
  /* background: white; */
  /* color: red !important; */
  /* margin: auto; */
  /* width: 90%; */
  /* border-radius: 12%/50% !important; */
  color: white !important;
  background: #6f42c1 !important;
}
.profile {
  margin-top: 1vh;
  height: 8vh;
  max-height: 8vh;
}
.sideBarItem > a {
  /* border-radius: 12%/50% !important; */
  border-radius: 6%/35%;
  width: 100%;
  color: white !important;
}
.sideBarItem > a :hover {
  /* border-radius: 12%/50% !important; */
  /* border-radius: 5%/40%; */
  background: transparent;
  color: white !important;
}
.sideBarItem > a > h4 :hover {
  color: white !important;
}
.sideBarItem {
  margin: 1vh 0;
}
.sideBarItem :hover {
  color: white !important;
  background: rgba(111, 66, 193, 0.4);
}
.icon {
  margin-right: 10px;
  /* color: rgba(255, 255, 255, 0.616); */
}

/* .sideBarItems {
  height: 15vh;
  padding: 3vh;
  color: white;
}
.sidebarItems:hover {
  background: #495057;
  color: #17a2b8;
} */
/* .link:hover {
  text-decoration: none;
} */
</style>
