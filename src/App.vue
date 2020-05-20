<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/> -->
    <Dashboard />
  </div>
</template>

<script>
import Dashboard from "/Users/ronaldgilliard/invoice-app-electron/src/views/Dashboard.vue";
export default {
  name: "App",
  components: {
    Dashboard
  }
};
</script>

<style lang="scss">
@import "~bootstrap/scss/bootstrap.scss";
@import "~bootstrap-vue/dist/bootstrap-vue.css";

html { height: 100%; }
body { height: 100%; display: flex; }
body > div { flex: 1; }

.danger {
  background-color: purple;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.fullHeight {
  height: 100vh;
  margin: 0;
  padding: 0;
}
</style>
