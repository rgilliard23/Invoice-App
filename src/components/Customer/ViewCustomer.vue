<template>
  <div>
    <b-col align-h="between">
      <b-row class="w-100 m-auto" align-h="between"
        ><b-row class="w-50">
          <h4>Customer Name:</h4>
          <b-form-input readonly :value="customer.name"></b-form-input>
        </b-row>
        <b-row class="w-50">
          <h4>Customer Address:</h4>
          <!-- <h3>{{ customer.address }}</h3> -->
          <b-form-input
            readonly
            :value="customer.address"
          ></b-form-input> </b-row
      ></b-row>
    </b-col>
    <b-form @submit.stop.prevent="onSubmit" inline>
      <!-- <b-row style="margin-top: 1vh;" align-h="center">
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button class="ml-2" @click="resetForm()">Reset</b-button>
      </b-row> -->
    </b-form>
    <b-pagination
      style="margin-top: 2vh;"
      class="w-100"
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
      align="fill"
    ></b-pagination>
    <b-table
      :currentPage="currentPage"
      :per-page="perPage"
      :items="invoices"
      :fields="invoiceFields"
    >
      <template v-slot:cell(actions)="data">
        <div>
          <b-dropdown
            variant="primary"
            no-caret
            id="dropdown-1"
            text="Options"
            class="m-md-2 bg-transparent"
          >
            <template v-slot:button-content>
              <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
            </template>
            <b-dropdown-group id="dropdown-group-1">
              <b-dropdown-item @click="viewInvoice(data.item)">
                View</b-dropdown-item
              >
              <b-dropdown-item @click="editInvoice(data.item)"
                >Edit</b-dropdown-item
              >
              <b-dropdown-item @click="deleteInvoice(data.item)"
                >Delete</b-dropdown-item
              >
            </b-dropdown-group>
            <!-- <b-button variant="warning" block @click="addProduct(data.item,true)">Edit</b-button>
            <b-button variant="danger" block @click="deleteProduct(data.item)">Delete</b-button>-->
          </b-dropdown>
        </div>
      </template>
    </b-table>
    <b-modal title="Invoice" hide-footer size="xl" ref="viewInvoice">
      <keep-alive>
        <InvoiceTemplate
          v-bind:transactions="transactions"
          v-bind:dateDue="invoice.dateDue"
          v-bind:createdDate="invoice.createdDate"
        />
      </keep-alive>
    </b-modal>

    <b-modal hide-footer size="xl" ref="editInvoice">
      <keep-alive>
        <Invoice
          v-bind:invoiceCustomer="customer"
          v-bind:edit="true"
          v-bind:invoice="invoice"
        />
      </keep-alive>
    </b-modal>
  </div>
</template>

<script>
const axios = require("axios");
const path = "http://localhost:5000/api/customer";
const invoicePath = "http://localhost:5000/api/invoice";

import moment from "moment";
import { validationMixin } from "vuelidate";
import { required, minLength } from "vuelidate/lib/validators";
import Invoice from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/Invoice.vue";
import { BIconThreeDotsVertical } from "bootstrap-vue";
import InvoiceTemplate from "../Invoice/InvoiceTemplate";

export default {
  mixins: [validationMixin],
  name: "ViewCustomer",
  components: {
    BIconThreeDotsVertical,
    Invoice,
    InvoiceTemplate,
  },
  data: function() {
    return {
      invoice: {},
      pageOfItems: [],
      invoices: [],
      transactions: [],
      currentPage: 1,
      perPage: 5,
      form: {
        name: null,
        address: null,
      },
      invoiceFields: [
        { key: "id", label: "Id" },
        {
          key: "date_created",
          label: "Date Created",
          formatter: (value) => {
            return moment(value, "YYYYMMDD").format("MMM Do YYYY");
          },
        },
        { key: "completed", label: "Completed" },
        {
          key: "date_due",
          label: "Date Due",
          formatter: (value) => {
            return moment(value, "YYYYMMDD").format("MMM Do YYYY");
          },
        },
        {
          key: "total",
          label: "Total",
          formatter: (value) => {
            return "$" + value.toLocaleString();
          },
        },
        { key: "actions", label: "Actions" },
      ],
      customLabels: {
        first: "<<",
        last: ">>",
        previous: "<",
        next: ">",
      },
    };
  },
  props: {
    customer: Object,
  },
  methods: {
    onChangePage(pageOfItems) {
      // update page of items
      this.pageOfItems = pageOfItems;
    },
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    resetForm() {
      this.form = {
        name: null,
        address: null,
      };

      this.$nextTick(() => {
        this.$v.$reset();
      });
    },
    viewInvoice(invoice) {
      this.invoice = invoice;
      this.transactions = [];

      this.invoice.transactions.forEach((element) => {
        this.transactions.push({
          price: element.product.price,
          name: element.product.name,
          quantity: element.quantity,
        });
      });

      this.$refs["viewInvoice"].show();
    },
    deleteInvoice(invoice) {
      if (confirm("Are You Sure You Want To Delete This Invoice")) {
        axios
          .delete(invoicePath + "/" + invoice.id)
          .then((res) => {
            alert("Invoice Deleted");
            console.log(res.data);
            axios
              .get(path + "/" + this.customer.id)
              .then((res) => {
                this.customer = res.data.customer;
                this.invoices = res.data.customer.invoices;
              })
              .catch((err) => {
                console.log(err.data);
              });
          })
          .catch((err) => {
            console.log(err.data);
          });
      }
    },
    editInvoice(invoice) {
      this.invoice = invoice;
      this.$refs["editInvoice"].show();
    },
    formatDate(date) {
      let formatedDate = moment(date, "YYYYMMDD").format("MMMM Do YYYY");
      return formatedDate;
    },
    onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }
      if (this.edit) {
        axios
          .put(path + "/" + this.customer.id, this.customer)
          .then((res) => {
            console.log(res.data);
          })
          .catch((err) => {
            console.log(err.data);
          });
        this.edit = false;
      } else {
        let temp = { name: "", address: "" };
        temp.name = this.form.name;
        temp.address = this.form.address;
        axios
          .post(path, temp)
          .then((res) => {
            this.$emit("addedCustomer");
            alert("Added Customer");
            console.log(res.data);
            this.getCustomers();
          })
          .catch((error) => {
            console.log(error.data);
          });
      }

      this.customer.name = this.form.name;
      this.customer.address = this.form.address;
    },
  },
  computed: {
    rows() {
      return this.invoices.length;
    },
  },
  validations: {
    form: {
      address: {
        required,
        minLength: minLength(5),
      },
      name: {
        required,
        minLength: minLength(3),
      },
    },
  },
  created() {
    if (this.customer != null) {
      this.form.name = this.customer.name;
      this.form.address = this.customer.address;

      axios
        .get(path + "/" + this.customer.id)
        .then((res) => {
          this.customer = res.data.customer;
          this.invoices = res.data.customer.invoices;
        })
        .catch((err) => {
          console.log(err.data);
        });
    }
  },
};
</script>

<style scoped>
.button-GP {
  margin: 0 5;
}
</style>
