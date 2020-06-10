import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import InvoiceView from "../views/InvoiceView.vue";
import ProductView from "../views/ProductView.vue";
import CustomerView from "../views/CustomerView.vue";
import Invoice from "../components/Invoice/Invoice.vue";
import Home from "../views/Home.vue";
import CreateInvoice from "../views/CreateInvoice"






Vue.use(VueRouter);

// const routes = [
//   {
//     path: "/route",
//     // We don't provide a name on this parent route, but rather
//     // set the name on the default child route instead
//     // name: 'some-route',
//     component: InvoiceView,
//     // Child route "tabs"
//     children: [
//       // Note we provide the above parent route name on the default child tab
//       // route to ensure this tab is rendered by default when using named routes
//       { path: "home", component: Home, name: "route" },
//       { path: "newinvoice", component: Invoice, name:"New Invoice" },
//       { path: "invoiceview", component: InvoiceView, name: "Invoice View" },
//       { path: "customer", component: CustomerView, name: "Customer View" },
//       { path: "product", component: ProductView, name: "Product View" }
//     ]
//   }
// ];

const routes = [
  {
    path: "/home",
    name: "Home",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Home,
  },
  {
    path: "/",
    name: "InvoiceView",
    component: InvoiceView,
  },
  {
    path: "/newinvoice",
    name: "New Invoice",
    component: Invoice,
  },
  {
    path: "/customer",
    name: "Customer View",
    component: CustomerView,
  },
  {
    path: "/product",
    name: "Product View",
    component: ProductView,
  },
  {
    path: "/createinvoice",
    name: "Create Invoice",
    component: CreateInvoice,
  },
  // {
  //   path: "/",
  //   name: "Home",
  //   component: Home
  // },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  linkExactActiveClass: "active",
  linkActiveClass: "active",
});

export default router;
