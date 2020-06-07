<template>
  <div>
    <b-form @submit.stop.prevent="onSubmit">
      <b-form-group
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
      </b-form-group>
      <b-list-group v-if="edit">
        <b-list-group-item v-for="invoice in invoices" :key="invoice.id">
          {{ invoice.date_created }}
        </b-list-group-item>
      </b-list-group>
      <b-row class="w-50" align-h="center" style="margin: 10px auto;"> <b-button type="submit" variant="primary">Submit</b-button>
      <b-button class="ml-2" variant="danger" @click="resetForm()">Reset</b-button></b-row>
     
    </b-form>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength } from "vuelidate/lib/validators";
const axios = require("axios");
const path = "http://localhost:5000/api/customer";

export default {
  mixins: [validationMixin],
  name: "AddCustomer",
  props: {
    edit: Boolean,
    customer: Object
  },
  data: function() {
    return {
      invoices: [],
      form: {
        name: null,
        address: null
      }
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
      if (this.edit) {
        if (confirm("Are You Sure Want To Change This Customer")) {
          axios
            .put(path + "/" + this.customer.id, this.customer)
            .then(res => {
              console.log(res.data);
            })
            .catch(err => {
              console.log(err.data);
            });
          this.edit = false;
          this.$emit("addedCustomer");
        }
      } else {
        let temp = { name: "", address: "" };
        temp.name = this.form.name;
        temp.address = this.form.address;
        axios
          .post(path, temp)
          .then(res => {
            this.$emit("addedCustomer");
            alert("Added Customer");
            console.log(res.data);
            this.getCustomers();
          })
          .catch(error => {
            console.log(error.data);
          });
      }

      this.customer.name = this.form.name;
      this.customer.address = this.form.address;
    }
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
  },
  created() {
    if (this.customer != null) {
      this.form.name = this.customer.name;
      this.form.address = this.customer.address;

      this.invoices = this.customer.invoices;
    }
  }
};
</script>

<style></style>
