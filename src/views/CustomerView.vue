<template>
  <div>
    <b-container class="clear fullHeight" fluid>
      <b-navbar style="height:10vh;" type="dark" variant="info">
        <b-navbar-brand>
          <h1>Customers</h1>
        </b-navbar-brand>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-input type="text" v-model="searchCustomer" placeholder="Search"></b-input>
            <b-button
              @click="showCustomer(null,false)"
              class="margin"
              size="lg"
              variant="success"
            >Add Customer</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>

      <b-table fixed :fields="customerFields" :items="filterCustomerList">
        <template v-slot:cell(actions)="data">
          <b-dropdown no-caret id="dropdown-1" text="Options" class="m-md-2">
            <template v-slot:button-content variant="link">
              <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
            </template>
            <b-dropdown-group id="dropdown-group-1">
              <b-dropdown-item @click="showCustomer(data.item, true)">Edit</b-dropdown-item>
              <b-dropdown-item @click="deleteCustomer(data.item)">Delete</b-dropdown-item>
            </b-dropdown-group>
            <!-- <b-button variant="warning" block @click="addProduct(data.item,true)">Edit</b-button>
            <b-button variant="danger" block @click="deleteProduct(data.item)">Delete</b-button>-->
          </b-dropdown>
        </template>
        <template v-slot:custom-foot v-if="filterCustomerList == 0">
          <tr>
            <td></td>
            <td>
              <h1>No Data</h1>
            </td>
            <td></td>
            <td></td>
          </tr>
        </template>
      </b-table>
      <b-modal hide-footer centered :title="modalName" ref="addCustomer" id="addCustomer">
        <keep-alive>
          <AddCustomer
            @addedCustomer="addedCustomer"
            v-bind:edit="edit"
            v-bind:customer="customer"
          />
        </keep-alive>
      </b-modal>
    </b-container>
  </div>
</template>

<script>
import AddCustomer from "/Users/ronaldgilliard/invoice-app-electron/src/components/Customer/AddCustomer.vue";
const axios = require("axios");
const path = "http://localhost:5000/api/customer";

export default {
  name: "CustomerView",
  components: {
    AddCustomer
  },
  data: function() {
    return {
      edit: false,
      customers: [],
      searchCustomer: "",
      customer: {
        id: 0,
        name: "",
        address: ""
      },
      options: {
        buttons: ["Yes", "No", "Cancel"],
        message: "Do you really want to quit?"
      },
      customerFields: [
        { key: "id", label: "Id" },
        { key: "name", label: "Name" },
        { key: "address", label: "Address" },
        { key: "actions", label: "" }
      ]
    };
  },
  methods: {
    addedCustomer() {
      this.getCustomers();
      this.$refs["addCustomer"].hide();
    },
    showCustomer(customer, edit) {
      this.customer = customer;
      this.edit = edit;
      this.$refs["addCustomer"].show();
    },
    //* gets all customers
    getCustomers() {
      axios
        .get(path)
        .then(res => {
          this.customers = res.data.customers;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    submitCustomer(edit) {
      this.edit = edit;
      if (this.edit) {
        axios
          .put(path + "/" + this.customer.id, this.customer)
          .then(res => {
            console.log(res.data);
          })
          .catch(err => {
            console.log(err.data);
          });
        this.edit = false;
      } else {
        axios
          .post(path, this.customer)
          .then(res => {
            console.log(res.data);
            this.getCustomers();
          })
          .catch(error => {
            console.log(error.data);
          });
        console.log("Submitted Product");
      }
    },
    editCustomer(customer) {
      this.customer = customer;
      this.edit = true;
    },
    deleteCustomer(customer) {
      if (confirm("Do you really want to delete?")) {
        axios
          .delete(path + "/" + customer.id)
          .then(res => {
            console.log(res.data);
            this.getCustomers();
          })
          .catch(err => {
            console.log(err.data);
          });
      }
    }
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
      return this.customers.filter(item => {
        return this.searchCustomer
          .toLowerCase()
          .split(" ")
          .every(v => item.name.toLowerCase().includes(v));
      });
    }
  }
};
</script>

<style>
</style>