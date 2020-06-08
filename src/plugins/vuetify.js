import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#6f42c1",
      },
      dark: {
        primary: "#6f42c1",
      },
    },
  },
});

export default vuetify;
