import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import InvoiceView from "../views/InvoiceView.vue"
import ProductView from "../views/ProductView.vue"
import CustomerView from "../views/CustomerView.vue"
import Invoice from "../components/Invoice/Invoice.vue"
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "InvoiceView",
    component: InvoiceView,
  },
  {
    path: "/newinvoice",
    name: "New Invoice",
    component: Invoice
  },
  {
    path: "/customer",
    name: "Customer View",
    component: CustomerView
  },
  {
    path: "/product",
    name: "Product View",
    component: ProductView
  },
  // {
  //   path: "/",
  //   name: "Home",
  //   component: Home
  // },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
