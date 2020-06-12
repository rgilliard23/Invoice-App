<template>
  <div class="bg-light">
    <b-container
      class="clear m-0 p-0"
      style="height: 100vh; overflow: hidden;"
      fluid
    >
      <b-navbar
        style="height:10vh;"
        class="navigation bg-white"
        type="liht"
        variant="info"
      >
        <b-navbar-brand>
          <h1>Customers</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <v-col align="center">
              <v-row>
                <!-- <v-text-field
                  class="navSearch"
                  label="Search"
                  v-model="searchCustomer"
                  solo
                  hide-details
                ></v-text-field> -->
                <!-- <v-btn
                  @click="showCustomer(null, false)"
                  class="navLinks navButton navButtonMargin"
                  block
                  color="success"
                  >Add Customer
                </v-btn> -->
                <AddCustomer
                  :create="false"
                  :edit="edit"
                  :dialog="dialog"
                  @close="closeAddCustomer"
                  :customer="customer"
                  @addedCustomer="addedCustomer"
                  class="navLinks navButton navButtonMargin"
                ></AddCustomer>
              </v-row>
            </v-col>

            <!-- <b-button
              @click="showCustomer(null, false)"
              class="margin navLinks navButtonMargin"
              size="lg"
              variant="success"
              >Add Customer</b-button
            > -->
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <v-column style="height: 90vh">
        <v-card style="height: 90vh; overflow: auto;">
          <v-flex style="overflow: auto;" class="w-100">
            <v-card-title>
              <v-text-field
                v-model="searchCustomer"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table
              :headers="tableHeaders"
              :items="customers"
              :search="searchCustomer"
            >
              <template v-slot:item.actions="{ item }">
                <div>
                  <v-icon small class="mr-2" @click="showCustomer(item, true)">
                    mdi-pencil
                  </v-icon>
                  <v-icon small @click="deleteCustomer(item)">
                    mdi-delete
                  </v-icon>
                </div>
              </template>
            </v-data-table>
          </v-flex>
         
        </v-card>
      </v-column>

      <!-- <b-table fixed :fields="customerFields" :items="filterCustomerList">
        <template v-slot:cell(actions)="data">
          <b-dropdown
            v-b-popover.hover.top="'Actions'"
            variant="primary"
            no-caret
            id="dropdown-1"
            text="Options"
            class="m-md-2"
          >
            <template v-slot:button-content variant="link">
              <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
            </template>
            <b-dropdown-group id="dropdown-group-1">
              <b-dropdown-item @click="viewCustomer(data.item)"
                >View</b-dropdown-item
              >
              <b-dropdown-item @click="showCustomer(data.item, true)"
                >Edit</b-dropdown-item
              >
              <b-dropdown-item @click="deleteCustomer(data.item)"
                >Delete</b-dropdown-item
              >
            </b-dropdown-group>
          </b-dropdown>
        </template>
      </b-table>
      <div v-if="filterCustomerList == 0"><h1>No Data</h1></div> -->
      <!-- <b-modal
        hide-footer
        centered
        size="lg"
        :title="modalName"
        ref="addCustomer"
        id="addCustomer"
      >
        <keep-alive>
          <AddCustomer
            @closeAddCustomer="closeAddCustomer"
            @addedCustomer="addedCustomer"
            :dialog="dialog"
            v-bind:edit="edit"
            v-bind:customer="customer"
          />
        </keep-alive>
      </b-modal> -->
      <b-modal
        centered
        hide-footer
        size="lg"
        title="Customer Details"
        ref="viewCustomer"
      >
        <keep-alive>
          <ViewCustomer
            @invoiceDeleted="getCustomer"
            v-bind:customer="customer"
          />
        </keep-alive>
      </b-modal>
    </b-container>
  </div>
</template>

<script>
import AddCustomer from "/Users/ronaldgilliard/invoice-app-electron/src/components/Customer/AddCustomer.vue";
import ViewCustomer from "/Users/ronaldgilliard/invoice-app-electron/src/components/Customer/ViewCustomer.vue";

const axios = require("axios");
const path = "http://localhost:5000/api/customer";

export default {
  name: "CustomerView",
  components: {
    AddCustomer,
    ViewCustomer,
  },
  data: function() {
    return {
      edit: false,
      customers: [],
      dialog: false,
      searchCustomer: "",
      customer: {
        id: null,
        name: null,
        address: null,
      },
      options: {
        buttons: ["Yes", "No", "Cancel"],
        message: "Do you really want to quit?",
      },
      tableHeaders: [
        { text: "Id", value: "id" },
        {
          text: "Name",
          sortable: false,
          value: "name",
        },
        { text: "Address", value: "address" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      customerFields: [
        { key: "id", label: "Id" },
        { key: "name", label: "Name" },
        { key: "address", label: "Address" },
        { key: "actions", label: "Actions" },
      ],
    };
  },
  methods: {
    addedCustomer() {
      this.getCustomers();
      this.$refs["addCustomer"].hide();
    },
    showCustomer(customer, bool) {
      this.customer = customer;
      this.edit = bool;
      this.dialog = true;
    },
    viewCustomer(customer) {
      this.customer = customer;
      this.$refs["viewCustomer"].show();
    },
    //* gets all customers
    getCustomers() {
      axios
        .get(path)
        .then((res) => {
          this.customers = res.data.customers;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getCustomer() {
      axios
        .get(path + "/" + this.customer.id)
        .then((res) => {
          this.customer = res.data.customer;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    closeAddCustomer() {
      this.dialog = false;
      this.edit = false;
      this.customer = { id: 0, name: null, address: null, invoices: [] };
    },
    submitCustomer(edit) {
      this.edit = edit;
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
        axios
          .post(path, this.customer)
          .then((res) => {
            console.log(res.data);
            this.getCustomers();
          })
          .catch((error) => {
            console.log(error.data);
          });
        console.log("Submitted Product");
      }
    },
    editCustomer(customer) {
      this.customer = customer;
      this.edit = true;
      this.dialog = true;
    },
    deleteCustomer(customer) {
      if (confirm("Do you really want to delete?")) {
        axios
          .delete(path + "/" + customer.id)
          .then((res) => {
            console.log(res.data);
            this.getCustomers();
          })
          .catch((err) => {
            console.log(err.data);
          });
      }
    },
  },
  //* Calls function on load
  created() {
    this.getCustomers();
  },

  computed: {
    modalName() {
      if (this.edit) {
        return "Edit Customer";
      }
      return "Add Customer";
    },
    filterCustomerList() {
      return this.customers.filter((item) => {
        return this.searchCustomer
          .toLowerCase()
          .split(" ")
          .every((v) => item.name.toLowerCase().includes(v));
      });
    },
  },
};
</script>

<style scoped>
.navButtonMargin {
  margin: 0 5px;
}
.v-input__slot {
  min-height: unset;
  min-width: unset;
  width: 25%;
  height: 5vh;
}

.navLinks {
  width: 45%;
  font-size: 20px;
}
.navSearch {
  width: 45%;
  min-width: 5px !important;
}
.navButton {
  min-width: 2vh;
  padding: 0;
  font-size: 14px;
  height: 4.7vh;
  min-height: 4.7vh;
}
.v-text-field.v-text-field--enclosed .v-text-field__details,
.v-text-field.v-text-field--enclosed > .v-input__control > .v-input__slot {
  margin: 0;
  min-height: 32px !important;
  display: flex !important;
  align-items: center !important;
}
.navigation {
  height: 25vh;
}

@media (min-width: 768px) and (max-width: 992px) {
  .navLinks {
    width: 45%;
    /* font-size: 18px; */
  }
}

@media (min-width: 576px) and (max-width: 767px) {
  .navLinks {
    width: 45%;
    /* font-size: 16px; */
  }
}

@media (min-width: 200px) and (max-width: 575px) {
  .navLinks {
    width: 100%;
    /* font-size: 12px; */
  }
  .navButtonMargin {
    margin: 0px;
  }
}
</style>
