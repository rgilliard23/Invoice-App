import Vue from "vue";
import "./plugins/bootstrap-vue";
import App from "./App.vue";
import Vuelidate from "vuelidate";
import router from "./router";
import vuetify from './plugins/vuetify';
Vue.use(Vuelidate);
Vue.use(require("vue-moment"));

Vue.config.productionTip = false;

// let options = {
//   mode: "text",
//   pythonPath: "path/to/python",
//   pythonOptions: ["-u"], // get print results in real-time
//   scriptPath: "path/to/my/scripts",
//   args: ["value1", "value2", "value3"],
// };

let { PythonShell } = require("python-shell");

PythonShell.run("src/data/database.py", function(err, results) {
  console.log(results);
  if (err) console.log(err);
});

new Vue({
  router,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");
