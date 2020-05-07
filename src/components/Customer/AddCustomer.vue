<template>
  <div>
    <b-form @submit.stop.prevent="onSubmit">
      <b-form-group id="input-group-1" label="Customer Name:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="$v.form.name.$model"
          type="text"
          required
          :state="validateState('name')"
          placeholder="Enter Name"
          aria-describedby="input-1-live-feedback"
        ></b-form-input>
        <b-form-invalid-feedback id="input-1-live-feedback">Name must be at least 3 characters</b-form-invalid-feedback>
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
        <b-form-invalid-feedback id="input-2-live-feedback">Address be at least 5 characters</b-form-invalid-feedback>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button class="ml-2" @click="resetForm()">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength } from "vuelidate/lib/validators";
export default {
  mixins: [validationMixin],
  name: "Add Customer Modal",
  data: function() {
    return {
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

      alert("Form submitted!");
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
  }
};
</script>

<style>
</style>