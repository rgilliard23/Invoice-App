<template>
  <div>
    <b-form>
      <b-col class="w-100 m-auto"
        ><b-row class="w-100">
          <h4>Product Name:</h4>
          <b-form-input
            id="input-1"
            type="text"
            readonly
            :value="product.name"
            aria-describedby="input-1-live-feedback"
          ></b-form-input>
        </b-row>
        <b-row class="w-100" style="margin-top: 1vh;">
          <h4>Product Address:</h4>
          <!-- <h3>{{ customer.address }}</h3> -->
          <b-form-input
            id="input-1"
            type="text"
            readonly
            :value="product.price"
            aria-describedby="input-2-live-feedback"
          ></b-form-input>
        </b-row>
        <b-row class="w-100" style="margin-top: 1vh;">
          <h4>Product Description:</h4>
          <!-- <h3>{{ customer.address }}</h3> -->
          <b-form-textarea
            id="input-1"
            type="text"
            readonly
            :value="product.description"
            aria-describedby="input-2-live-feedback"
          ></b-form-textarea>
        </b-row>
      </b-col>
      <!-- <b-form-group label="Product Name:" class="text-center">
        <h5>{{ product.name }}</h5>
      </b-form-group>
      <b-form-group label="Product Price:" class="text-center">
        <h5>{{ product.price }}</h5>
      </b-form-group>
      <b-form-group label="Product Description:" class="text-center">
        <h5>{{ product.description }}</h5>
      </b-form-group> -->
    </b-form>
  </div>
</template>

<script>
export default {
  name: "ViewProduct",
  props: {
    product: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {};
  },
};
</script>

<style></style>
