<template>
  <div>
    <b-row>
      <b-col>
        <b-input v-model="searchCustomer" type="text" placeholder="Search"></b-input>
        <div style="height: 2vh;"></div>
        <b-list-group class="list-group-overflow">
          <b-list-group-item v-for="customer in filterCustomerList" :key="customer">
            <b-row align-h="between">
              <div>{{customer.name}}</div>
              <b-button @click="selectCustomer(customer)" variant="primary">Select Customer</b-button>
            </b-row>
          </b-list-group-item>
        </b-list-group>
        <b-button
          style="margin-top: 10px;"
          v-b-modal.addCustomerModal
          variant="info"
        >Add Customer</b-button>

        <b-modal centered ref="addCustomerModal" id="addCustomerModal" title="Add Customer">
          <AddCustomerInvoice />
        </b-modal>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength } from "vuelidate/lib/validators";
import AddCustomerInvoice from "/Users/ronaldgilliard/invoice-app-electron/src/components/Customer/AddCustomerInvoice.vue";

export default {
  mixins: [validationMixin],
  name: "CustomerModal",
  components: {
    AddCustomerInvoice
  },
  data: function() {
    return {
      searchCustomer: "",
      form: {
        name: null,
        address: null
      },
      customer: {
        name: "",
        address: ""
      },
      customers: [
        { name: "Ronald", address: "3202 cherrydale dr" },
        { name: "Joyce Gilliard", address: "3202 cherrydale dr" },
        { name: "Ronald", address: "3202 cherrydale dr" },
        { name: "Joyce Gilliard", address: "3202 cherrydale dr" },
        { name: "Ronald", address: "3202 cherrydale dr" },
        { name: "Joyce Gilliard", address: "3202 cherrydale dr" },
        { name: "Ronald", address: "3202 cherrydale dr" },
        { name: "Joyce Gilliard", address: "3202 cherrydale dr" },
        { name: "Ronald", address: "3202 cherrydale dr" },
        { name: "Joyce Gilliard", address: "3202 cherrydale dr" },
        { name: "Ronald", address: "3202 cherrydale dr" },
        { name: "Joyce Gilliard", address: "3202 cherrydale dr" },
        { name: "Bob", address: "3202 cherrydale dr" }
      ]
    };
  },
  methods: {
    validateState(name) {
      const { $dirty, $error } = this.$v.form[name];
      return $dirty ? !$error : null;
    },
    resetForm() {
      this.form = {
        name: null,
        address: null
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

      alert("Form submitted!");
      this.customer.name = this.form.name;
      this.customer.address = this.form.address;
    },
    selectCustomer(customer) {
      this.customer.name = customer.name;
      this.customer.address = customer.address;
      this.$emit("selectCustomer", customer);
    }
  },
  computed: {
    filterCustomerList() {
      return this.customers.filter(item => {
        return this.searchCustomer
          .toLowerCase()
          .split(" ")
          .every(v => item.name.toLowerCase().includes(v));
      });
    },
    
  },
  validations: {
    form: {
      address: {
        required,
        minLength: minLength(5)
      },
      name: {
        required,
        minLength: minLength(3)
      }
    }
  }
};
</script>

<style>
.list-group-overflow {
  overflow: scroll;
  max-height: 60vh;
}
</style>