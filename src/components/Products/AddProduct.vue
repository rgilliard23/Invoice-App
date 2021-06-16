<template>
<v-row justify="center">
    <v-dialog v-model="show" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-btn color="success" dark v-on="on">Add Product</v-btn>
      </template>

      <v-card>
        <v-form ref="form">
          <v-card-title class="headline">
            <span v-if="!edit" class="headline">New Product</span>
            <span v-else class="headline">Edit Product</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    :rules="inputRules"
                    v-model="form.name"
                    label="Name*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="form.price"
                    label="Price*"
                    number
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-textarea
                    auto-grow
                    outlined
                    rows="5"
                    row-height="24"
                    :rules="inputRules"
                    v-model="form.description"
                    label="Description"
                  ></v-textarea>
                </v-col>
              </v-row>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn text @click="close">Close</v-btn>
            <v-btn color="success" text @click="submit">Save</v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { validationMixin } from "vuelidate";
import {
  required,
  minLength,
  maxLength,
  between
} from "vuelidate/lib/validators";
const axios = require("axios");
const path = "http://localhost:5000/api/product";

export default {
  mixins: [validationMixin],
  name: "AddProduct",
  props: {
    edit: {
      type: Boolean,
      default: false
    },
    product: {
      type: Object,
      default: null
    },
    dialog: {
      type: Boolean,
      default: false
    }
  },
  data: function() {
    return {
      inputRules: [v => v.length >= 3 || "Minimum Length is 3 Characters"],
      show: false,
      form: {
        name: "",
        price: 0,
        description: ""
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
      description: {
        maxLength: maxLength(10000)
      }
    }
  },
  methods: {
    close() {
      this.show = false;
      this.$emit("close");
    },
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
    submit() {
      // if (this.$v.form.$anyError) {
      //   return;
      // }

      if (!this.$refs.form.validate()) {
        alert("foehofh");
        return;
      }
      if (this.edit) {
        let temp = { name: "", price: 0, description: "" };
        temp.name = this.form.name;
        temp.price = this.form.price;
        temp.description = this.form.description;
        axios
          .put(path + "/" + this.product.id, temp)
          .then(res => {
            this.$emit("addedProduct");
            this.show = false;
            alert("Product Updated");
            console.log(res.data);
          })
          .catch(error => {
            console.log(error.data);
          });
      } else {
        let temp = { name: "", price: 0, description: "" };
        temp.name = this.form.name;
        temp.price = this.form.price;
        temp.description = this.form.description;
        axios
          .post(path, temp)
          .then(res => {
            this.$emit("addedProduct");
            this.show = false;
            alert("Added Product");
            console.log(res.data);
          })
          .catch(error => {
            console.log(error.data);
          });
      }
    }
  },
  created() {
    this.show = this.dialog;
    if (this.product !== null) {
      this.form.name = this.product.name;
      this.form.description = this.product.description;
      this.form.price = this.product.price;
    }
  },
  watch: {
    product() {
      this.form.name = this.product.name;
      this.form.price = this.product.price;
      this.form.description = this.product.description;
    },
    dialog() {
      this.show = this.dialog;
    }
  }
};
</script>

<style></style>
