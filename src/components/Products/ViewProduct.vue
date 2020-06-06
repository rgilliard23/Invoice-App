<template>
  <div>
    <b-form>
      <b-form-group label="Product Name:" class="text-center">
        <h5>{{ product.name }}</h5>
      </b-form-group>
      <b-form-group label="Product Price:" class="text-center">
        <h5>{{ product.price }}</h5>
      </b-form-group>
      <b-form-group label="Product Description:" class="text-center">
        <h5>{{ product.description }}</h5>
      </b-form-group>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "ViewProduct",
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  data() {
    return {};
  }
};
</script>

<style></style>
