<template>
  <!-- <div>
    <b-form @submit.stop.prevent="onSubmit">
      <b-col class="w-100 m-auto" align-h="between"
        ><b-row class="w-100"> -->
  <!-- <h4>Customer Name:</h4> -->
  <!-- <b-form-input
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
        :perPage="perPage"
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

            </b-dropdown>
          </div>
        </template>
      </b-table>


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
  </div> -->

  <!-- <div class="text-center">
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on }">
        <v-btn color="success" v-on="on">
          Add Customer
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2" primary-title>
          <div v-if="!edit">Add Customer</div>
          <div v-else>Edit Customer</div>
        </v-card-title>

        <v-card-text>
          <v-form ref="form" class="px-3">
            <v-text-field
              prepend-icon="mdi-account"
              label="Name"
              v-model="name"
              :rules="inputRules"
            ></v-text-field>
            <v-text-field
              prepend-icon="mdi-map-marker"
              label="Address"
              v-model="address"
              :rules="inputRules"
            ></v-text-field>
            <v-btn flat class="success mx-0 mt-3" @click="submit">Add Customer</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div> -->
  <v-row justify="center">
    <v-dialog persistent v-model="show" max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn v-if="create" color="success" v-on="on">New Customer</v-btn>
        <v-btn color="success" v-else dark v-on="on">Add Customer</v-btn>
      </template>
      <v-card>
        <v-form ref="form">
          <v-card-title class="headline">
            <span v-if="!edit" class="headline">Create Customer</span>
            <span v-else class="headline">Edit Customer</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    :rules="inputRules"
                    v-model="customer.name"
                    label="Name*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    :rules="inputRules"
                    v-model="customer.address"
                    label="Address*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field v-model="email" label="Email"></v-text-field>
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>

            <v-flex v-if="edit" style="overflow: auto;" class="w-100">
              <v-card-title>
                <v-text-field
                  v-model="searchInvoices"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
                ></v-text-field>
              </v-card-title>
              <v-data-table
                :headers="tableHeaders"
                :items="customer.invoices"
                :search="searchInvoices"
              >
                <template v-slot:item.actions="{ item }">
                  <v-menu open-on-hover top offset-y>
                    <template v-slot:activator="{ on }">
                      <div v-on="on">
                        <v-icon small class="mr-2" @click="editInvoice(item)">
                          mdi-pencil
                        </v-icon>
                        <v-icon small @click="deleteInvoice(item)">
                          mdi-delete
                        </v-icon>
                      </div>
                    </template>
                    <v-card>
                      <v-card-title>{{ item.name }}</v-card-title>
                      <v-card-text>howdy</v-card-text>
                    </v-card>
                  </v-menu>
                </template>

                <template v-slot:item.completed="{ item }">
                  <div>
                    <v-btn
                      v-if="!item.completed"
                      readonly
                      style="width: 70%;"
                      color="error"
                      >Unpaid</v-btn
                    >
                    <v-btn color="success" readonly style="width: 70%;" v-else
                      >Completed</v-btn
                    >
                  </div>
                </template>
              </v-data-table>
            </v-flex>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text @click="close">Close</v-btn>
            <v-btn color="success" text @click="submit">Save</v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength } from "vuelidate/lib/validators";
import moment from "moment";
// import InvoiceTemplate from "../Invoice/InvoiceTemplate";
// import Invoice from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/Invoice.vue";

const axios = require("axios");
const path = "http://localhost:5000/api/customer";
const invoicePath = "http://localhost:5000/api/invoice";

export default {
  mixins: [validationMixin],
  name: "AddCustomer",
  props: {
    edit: {
      type: Boolean,
      default: false,
    },
    customer: Object,
    dialog: {
      type: Boolean,
      default: false,
    },
    create: {
      type: Boolean,
      default: false,
    },
  },
  // components: {
  //   Invoice,
  //   InvoiceTemplate,
  // },
  data: function() {
    return {
      inputRules: [(v) => v.length >= 3 || "Minimum length is 3 characters"],
      invoices: [],
      show: false,
      email: null,
      tableHeaders: [
        { text: "Id", value: "id", sortable: true },
        { text: "Status", value: "completed", sortable: true },
        {
          text: "Due",
          sortable: true,
          value: "date_due",
        },

        { text: "Created", value: "date_created" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      invoice: [],
      currentPage: 1,
      transactions: [],
      searchInvoices: "",
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
      name: null,
      address: null,
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
    close() {
      if (this.edit) {
        this.name = null;
        this.address = null;
      }
      this.edit = false;
      this.show = false;
      this.$emit("close");
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
    submit() {
      if (!this.$refs.form.validate()) {
        return;
      }
      if (this.edit) {
        if (confirm("Are You Sure Want To Change This Customer")) {
          axios
            .put(path + "/" + this.customer.id, this.customer)
            .then((res) => {
              this.$emit("addedCustomer");
              this.show = false;
              console.log(res.data);
            })
            .catch((err) => {
              console.log(err.data);
            });
          this.edit = false;
        }
      } else {
        let temp = { name: "", address: "" };
        temp.name = this.customer.name;
        temp.address = this.customer.address;
        axios
          .post(path, temp)
          .then((res) => {
            this.$emit("addedCustomer");
            this.customer;
            this.show = false;
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
    this.show = this.dialog;
    if (this.customer != null) {
      this.name = this.customer.name;
      this.address = this.customer.address;

      this.invoices = this.customer.invoices;
    }
  },
};
</script>

<style></style>
