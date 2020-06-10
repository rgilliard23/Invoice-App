<template>
  <div id="app" style="height: 100vh; overflow: hidden;">
    <v-app class="h-100">
      <v-content class="h-100">
        <Dashboard  class="h-100" />
      </v-content>
      
    </v-app>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/> -->
  </div>
</template>

<script>
import Dashboard from "/Users/ronaldgilliard/invoice-app-electron/src/views/Dashboard.vue";

export default {
  name: "App",

  components: {
    Dashboard,
  },

  data: () => ({
    //
  }),
};
</script>
<style lang="scss">
@import "~bootstrap/scss/bootstrap.scss";
@import "~bootstrap-vue/dist/bootstrap-vue.css";

html {
  height: 100%;
}
body {
  height: 100%;
  display: flex;
}
body > div {
  flex: 1;
}

#app {
  // font-family: Avenir, Helvetica, Arial, sans-serif;
  font-family: Arial, Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
h4 {
  font-family: Arial, Helvetica, sans-serif;
}
.boxShadow {
  box-shadow: inset 5px 0 9px 0px rgba(0, 0, 0, 0.4) !important;
  color: black;
  overflow: hidden;
}
.cardShadow {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.3);
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    // color: #2c3e50;
    color: red !important;

    &.router-link-exact-active {
      color: #42b983 !important;
    }
  }
}

// #nav a.router-link-active {
//   color: red !important;
// }

.fullHeight {
  height: 100vh;
  // margin: 0;
  // padding: 0;
}
</style>
