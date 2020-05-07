<template>
  <div>
    <b-row>
      <b-col>
        <b-form @submit.stop.prevent="onSubmit">
          <b-form-group
            id="input-group-1"
            label="Customer Name:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="$v.address.model"
              type="text"
              required
              placeholder="Enter Name"
            ></b-form-input>
          </b-form-group>
          <b-form-group label="Customer Address:">
               <b-form-input
              id="input-1"
              v-model="address"
              type="email"
              required
              placeholder="Enter Address"
            ></b-form-input>
          </b-form-group>
        </b-form>

        <b-button type="submit">Save Customer</b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { required, minLength } from "vuelidate/lib/validators";

export default {
  name: "CustomerModal",
  data: function() {
    return {
      showNameError: false,
      showAddressError: false,
      address: "",
      name: "",
      customer: {
        name: "",
        address: ""
      }
    };
  },
  methods: {
    addCustomer() {
      if (this.name.length > 3) {
        this.showNameError = true;
      }
      if (this.address > 5) {
        this.showAddressError;
      }

      if (this.showAddressError || this.showNameError) {
        return;
      } else {
        this.customer.address = this.address;
        this.customer.name = this.name;
        this.address = "";
        this.name = "";
      }
    }
  },
  validations: {
    name: {
      required,
      minLength: minLength(4)
    }
  }
};
</script>

<style>
</style>