<template>
  <div>
    <b-container style="margin: 0; padding: 0;" class="w-100 m-0 p-0 h-100 sidebar" fluid>
      <b-row class="h-100" style="margin: 0; padding: 0;">
        <b-col col sm="3" class="w-100 h-100 shadow bg-dark fullHeight">
          <b-nav fill type="light" vertical class="w-100 h-100 bg-dark">
            <b-nav-item class="navLogo">
              <h1>Invoice App</h1>
            </b-nav-item>
            <hr class="brandLine" />
            <b-nav-item class="sideBarItem text-left " exact to="/home">
              <h4><b-icon-house class="icon"></b-icon-house>Home</h4>
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

            <b-nav-item to="/" class="sideBarItem text-left" exact>
              <h4>
                <span><b-icon-archive-fill class="icon"></b-icon-archive-fill></span>
                
                Invoices
              </h4>
            </b-nav-item>
          </b-nav>
        </b-col>
        <b-col col sm="9" class=" m-0 p-0 h-100">
          <router-view class="fullHeight overflow-scroll"></router-view>
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
      // activeClass: "active"
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
.boxShadow {
  box-shadow: inset 5px 0 9px 0px rgba(0, 0, 0, 0.4) !important;
  color: black;
  overflow: hidden;
}
.brandLine {
  width: 80%;
  border: 1px solid white;
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
  color: rgba(255, 255, 255, 0.616);
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
