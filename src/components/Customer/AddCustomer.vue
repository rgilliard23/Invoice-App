<template>
  <div>
    <b-form @submit.stop.prevent="onSubmit">
      <b-col class="w-100 m-auto" align-h="between"
        ><b-row class="w-100">
          <h4>Customer Name:</h4>
          <b-form-input
            id="input-1"
            v-model="$v.form.name.$model"
            type="text"
            required
            :state="validateState('name')"
            placeholder="Enter Name"
            aria-describedby="input-1-live-feedback"
          ></b-form-input>
        </b-row>
        <b-row class="w-100" style="margin-top: 1vh;">
          <h4>Customer Address:</h4>
          <!-- <h3>{{ customer.address }}</h3> -->
          <b-form-input
            id="input-1"
            v-model="$v.form.address.$model"
            type="text"
            required
            :state="validateState('address')"
            placeholder="Enter Address"
            aria-describedby="input-2-live-feedback"
          ></b-form-input> </b-row
      ></b-col>
      <!-- <b-form-group
        id="input-group-1"
        label="Customer Name:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="$v.form.name.$model"
          type="text"
          required
          :state="validateState('name')"
          placeholder="Enter Name"
          aria-describedby="input-1-live-feedback"
        ></b-form-input>
        <b-form-invalid-feedback id="input-1-live-feedback"
          >Name must be at least 3 characters</b-form-invalid-feedback
        >
      </b-form-group>
      <b-form-group label="Customer Address:">
        <b-form-input
          id="input-1"
          v-model="$v.form.address.$model"
          type="text"
          required
          :state="validateState('address')"
          placeholder="Enter Address"
          aria-describedby="input-2-live-feedback"
        ></b-form-input>
        <b-form-invalid-feedback id="input-2-live-feedback"
          >Address be at least 5 characters</b-form-invalid-feedback
        >
      </b-form-group> -->
      <b-pagination
        v-if="invoices.length > perPage"
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
        :perPage ="perPage"
        style="margin-top: 1vh;"
        v-if="edit && invoices.length > 0"
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
      <!-- <b-row class="w-50" align-h="center" style="margin: 10px auto;"> </b-row> -->

      <b-button
        type="submit"
        style="margin-top: 1vh;"
        variant="primary"
        v-if="edit"
        >Update Customer</b-button
      >
      <b-button type="submit" style="margin-top: 1vh;" variant="primary" v-else
        >Create Customer</b-button
      >
      <b-button
        class="ml-2"
        style="margin-top: 1vh;"
        variant="danger"
        @click="resetForm()"
        >Reset Form</b-button
      >
    </b-form>
    <b-modal title="Invoice" hide-footer size="xl" ref="viewInvoice">
      <keep-alive>
        <InvoiceTemplate
          v-bind:transactions="transactions"
          v-bind:dateDue="invoice.date_due"
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
import { validationMixin } from "vuelidate";
import { required, minLength } from "vuelidate/lib/validators";
import moment from "moment";
import InvoiceTemplate from "../Invoice/InvoiceTemplate";
import Invoice from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/Invoice.vue";

const axios = require("axios");
const path = "http://localhost:5000/api/customer";
const invoicePath = "http://localhost:5000/api/invoice";

export default {
  mixins: [validationMixin],
  name: "AddCustomer",
  props: {
    edit: Boolean,
    customer: Object,
  },
  components: {
    Invoice,
    InvoiceTemplate,
  },
  data: function() {
    return {
      invoices: [],
      invoice: [],
      currentPage: 1,
      transactions: [],
      perPage: 5,
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
      form: {
        name: null,
        address: null,
      },
    };
  },
  methods: {
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
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
    resetForm() {
      this.form = {
        name: null,
        address: null,
      };

      this.$nextTick(() => {
        this.$v.$reset();
      });
    },
    onSubmit() {
      this.$v.form.$touch();
      if (this.$v.form.$anyError) {
        return;
      }
      if (this.edit) {
        if (confirm("Are You Sure Want To Change This Customer")) {
          axios
            .put(path + "/" + this.customer.id, this.customer)
            .then((res) => {
              this.$emit("addedCustomer");
              console.log(res.data);
            })
            .catch((err) => {
              console.log(err.data);
            });
          this.edit = false;
        }
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
  computed: {
    rows() {
      return this.invoices.length;
    },
  },
  created() {
    if (this.customer != null) {
      this.form.name = this.customer.name;
      this.form.address = this.customer.address;

      this.invoices = this.customer.invoices;
    }
  },
};
</script>

<style></style>
