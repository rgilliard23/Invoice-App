<template>
  <div>
    <b-form @submit.stop.prevent="onSubmit">
      <b-form-group id="input-group-1" label="Product Name:" label-for="input-1">
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
      <b-form-group label="Product Price:">
        <b-input-group prepend="$">
          <b-form-input
            id="input-1"
            v-model="$v.form.price.$model"
            type="number"
            min="0"
            step="1"
            required
            :state="validateState('price')"
            placeholder="0"
            aria-describedby="input-2-live-feedback"
          ></b-form-input>
        </b-input-group>

        <b-form-invalid-feedback id="input-2-live-feedback">Price is required</b-form-invalid-feedback>
      </b-form-group>
      <b-form-group label="Select Quantity:">
        <b-input-group>
          <b-form-input
            id="input-1"
            v-model="$v.form.quantity.$model"
            type="number"
            min="1"
            step="1"
            required
            :state="validateState('quantity')"
            placeholder="0"
            aria-describedby="input-2-live-feedback"
          ></b-form-input>
        </b-input-group>

        <b-form-invalid-feedback id="input-2-live-feedback">Quantity Too High</b-form-invalid-feedback>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button class="ml-2" @click="resetForm()">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, minLength, between } from "vuelidate/lib/validators";
export default {
  mixins: [validationMixin],
  name: "AddProductInvoice",
  data: function() {
    return {
      form: {
        name: null,
        price: null,
        quantity: 1,
        description: null
      },
      product: {
        name: null,
        price: null,
        quantity: 1,
        description: null
      }
    };
  },
  validations: {
    form: {
      price: {
        required,
        between: between(0, 99999999999)
      },
      name: {
        required,
        minLength: minLength(3)
      },
      quantity: {
        between: between(0, 9999)
      }
    }
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
      alert("Product Saved and Added To List!");
      this.product.name = this.form.name;
      this.product.price = this.form.price;
      this.product.description = this.form.description;
      this.product.quantity = this.form.quantity;
      this.$emit("addToProductList", this.product);
    }
  }
};
</script>

<style>
</style>