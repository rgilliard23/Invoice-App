<template>
  <div id="app">
    <Dashboard/>
    <!-- <Invoice/> -->
  </div>
</template>

<script>

// import Invoice from './components/Invoice/Invoice';
import Dashboard from './views/Dashboard';
export default {
  name: 'App',
  components: {
    // Invoice,
    Dashboard
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}

*{
  margin: 0;
  padding: 0;
}
.clear{
     margin:0;
     padding: 0;
 }
 .fullHeight{
   height: 100vh;
 }
</style>
