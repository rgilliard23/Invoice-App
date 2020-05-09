import Vue from "vue";
import "./plugins/bootstrap-vue";
import App from "./App.vue";
import Vuelidate from "vuelidate";
Vue.use(Vuelidate);
Vue.use(require("vue-moment"));

Vue.config.productionTip = false;

let {PythonShell} = require('python-shell')
PythonShell.run("src/data/engine.py", function(err, results) {
  console.log(results);
  if (err) console.log(err);
});
new Vue({
  render: (h) => h(App),
}).$mount("#app");
