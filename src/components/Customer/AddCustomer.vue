<template>
  <v-row justify="center">
    <v-dialog persistent v-model="show" max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn v-if="create" color="success" v-on="on">New Customer</v-btn>
        <v-btn color="success" v-else dark v-on="on">Add Customer</v-btn>
      </template>

      <v-card>
        <!-- Edit Customer -->
        <v-stepper v-if="edit" v-model="e1">
          <v-stepper-header>
            <v-stepper-step step="1">Contact</v-stepper-step>

            <v-stepper-step step="2">Billing</v-stepper-step>
          </v-stepper-header>
          <v-stepper-items>
            <v-stepper-content step="1">
              <v-form ref="form">
                <v-card-title class="headline">
                  <span v-if="!edit" class="headline">Contact Info</span>
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
                        <v-text-field
                          v-model="email"
                          label="Email"
                        ></v-text-field>
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
                              <v-icon
                                small
                                class="mr-2"
                                @click="editInvoice(item)"
                              >
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
                          <v-btn
                            color="success"
                            readonly
                            style="width: 70%;"
                            v-else
                            >Completed</v-btn
                          >
                        </div>
                      </template>
                    </v-data-table>
                  </v-flex>
                </v-card-text>
                <!-- <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn text @click="close">Close</v-btn>
                  <v-btn color="success" text @click="submit">Save</v-btn>
                </v-card-actions> -->
              </v-form>

              <v-btn color="primary" @click="e1 = 2">
                Continue
              </v-btn>

              <v-btn text @click="close">Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="2">
              <v-card
                class="mb-12"
                color="grey lighten-1"
                height="200px"
              ></v-card>

              <v-btn color="primary" v-on:click="e1 = 1">
                Back
              </v-btn>
              <v-btn text @click="close">Close</v-btn>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>

        <!--* Add Customer-->
        <v-stepper
          v-if="!edit"
          :non-linear="nextStep"
          :editable="nextStep"
          v-model="e1"
          :complete="nextStep"
        >
          <v-stepper-header>
            <v-stepper-step step="1">Contact</v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="2">Billing</v-stepper-step>
          </v-stepper-header>

          <v-stepper-items>
            <v-stepper-content step="1">
              <v-form ref="form">
                <v-card-title class="headline">
                  <span v-if="!edit" class="headline">Contact Info</span>
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
                        <v-text-field
                          v-model="email"
                          label="Email"
                        ></v-text-field>
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
                              <v-icon
                                small
                                class="mr-2"
                                @click="editInvoice(item)"
                              >
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
                          <v-btn
                            color="success"
                            readonly
                            style="width: 70%;"
                            v-else
                            >Completed</v-btn
                          >
                        </div>
                      </template>
                    </v-data-table>
                  </v-flex>
                </v-card-text>
              </v-form>

              <v-btn color="primary" @click="e1 = 2">
                Continue
              </v-btn>

              <v-btn text>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="2">
              <v-card
                class="mb-12"
                color="grey lighten-1"
                height="200px"
              ></v-card>

              <v-btn disabled color="primary" @click="e1 = 1">
                Continue
              </v-btn>

              <v-btn text @click="close">Cancel</v-btn>
              <!-- <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text @click="close">Close</v-btn>
                <v-btn color="success" text @click="submit">Save</v-btn>
              </v-card-actions> -->
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
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
      nextStep: false,
      e1: 1,
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
    next() {
      this.e1 = 2;
      this.nextStep = true;
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
  watch: {
    dialog() {
      this.show = this.dialog;
    },
  },
};
</script>

<style></style>
