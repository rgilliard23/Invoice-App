<template>
  <div class="clear">
    <b-container class="clear fullHeight" fluid>
      <b-navbar style="height:10vh;" class="clear" toggleable="lg" type="dark" variant="info">
        <b-navbar-brand class="margin" tag="h1" href="#">
          <h1>Create Invoice</h1>
        </b-navbar-brand>

        <!-- //* Invoice Table -->

        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-button class="margin" size="lg" variant="danger">Invoice Pdf</b-button>
            <b-button class="margin" size="lg" variant="secondary">Export To Excel</b-button>
            <b-button class="margin" size="lg" variant="success">Save Invoice</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-navbar>
      <b-row style="height: 10vh;">
        <b-col lg="6" class="my-1">
          <b-form-group
            label="Date Created:"
            label-cols-lg="3"
            label-align-sm="right"
            label-for="sortBySelect"
            class="mb-0"
          >
            <b-form-datepicker size="lg" id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
          </b-form-group>
        </b-col>

        <b-col lg="6" class="my-1">
          <b-form-group
            label="Date Due:"
            label-cols-lg="3"
            label-align-sm="right"
            label-for="initialSortSelect"
            class="mb-0"
          >
            <b-form-datepicker size="lg" id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
          </b-form-group>
        </b-col>

        <b-col lg="6" class="my-1">
          <b-form-group
            label="Add Products:"
            label-cols-lg="3"
            label-align-sm="right"
            label-for="filterInput"
            class="mb-0"
          >
            <b-button block variant="success">Add Products</b-button>
          </b-form-group>
        </b-col>

        <b-col lg="6" class="my-1">
          <b-form-group
            label="Select Customer:"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="filterInput"
            class="mb-0"
          >
            <b-button v-b-modal.modal-1 block variant="outline-success">Select Customer</b-button>
          </b-form-group>
        </b-col>
      </b-row>
      <div style="height: 1vh;"></div>
      <b-container fluid>
        <b-table
          small
          striped
          fixed
          sticky-header="60vh"
          :items="items"
          :key="index"
          :fields="invoiceFields"
        >
          <template v-slot:cell(id)="data">
            <b-form-input
              readonly
              type="number"
              v-model="data.item.id"
              read-only
              placeholder="Enter your name"
            ></b-form-input>
          </template>
          <template v-slot:cell(name)="data">
            <b-form-input
              type="text"
              v-model="data.item.name"
              read-only
              placeholder="Enter your name"
            ></b-form-input>
          </template>
          <template v-slot:cell(price)="data">
            <b-form-input
              type="number"
              v-model="data.item.price"
              read-only
              placeholder="Enter your name"
            ></b-form-input>
          </template>
          <template v-slot:cell(quantity)="data">
            <b-form-input
              type="number"
              v-model="data.item.quantity"
              read-only
              placeholder="Enter your name"
            ></b-form-input>
          </template>
          <template v-slot:cell(total)="data">
            <b-form-input
              readonly
              type="number"
              v-model="data.item.total"
              read-only
              placeholder="Enter your name"
            ></b-form-input>
          </template>
          <template v-slot:cell(actions)>
            <b-button variant="danger" @click="deleteRow(index)">Remove</b-button>
          </template>
          <template v-slot:custom-foot>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Sub Total:</td>
              <td>$1,500</td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Tax:</td>
              <td>
                <b-input-group append="%">
                  <b-form-input append="%" type="number"></b-form-input>
                </b-input-group>
              </td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Discount:</td>
              <td>
                <b-input-group append="%">
                  <b-form-input type="number"></b-form-input>
                </b-input-group>
              </td>
              <td></td>
            </tr>
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>Grand Total:</td>
              <td>1,500</td>
              <td></td>
            </tr>
          </template>
        </b-table>
      </b-container>

      <b-button v-b-modal.modal-1>Launch demo modal</b-button>

      <b-modal size="lg" id="modal-1" title="BootstrapVue">
       <CustomerModal/>
      </b-modal>
      <!-- <b-table-simple fixed sticky-header="60vh">
        <b-thead>
          <b-tr>
            <b-th>Country</b-th>
            <b-th>City</b-th>
            <b-th>Trousers</b-th>
            <b-th>Skirts</b-th>
            <b-th>Dresses</b-th>
            <b-th>Bracelets</b-th>
            <b-th>Rings</b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr>
            <b-td>
              <b-form-input class="w-100" v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
            <b-td>
              <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>
            </b-td>
          </b-tr>
        </b-tbody>
        <b-tfoot>
          <b-tr>
            <b-td colspan="7" class="text-right">
              Total Rows:
              <b>5</b>
            </b-td>
          </b-tr>
        </b-tfoot>
      </b-table-simple>-->
    </b-container>
  </div>
</template>

<script>
import "axios";
import CustomerModal from "/Users/ronaldgilliard/invoice-app-electron/src/components/Customer/CustomerModal.vue";

export default {
  name: "Invoice",
  components: {
    CustomerModal
  },
  data: function() {
    return {
      transactions: [],
      customers: [],
      products: [],
      invoiceFields: [
        { key: "id", label: "Id" },
        { key: "name", label: "Name" },
        { key: "price", label: "Price" },
        { key: "quantity", label: "Quantity" },
        { key: "total", label: "Total" },
        { key: "actions", label: "" }
      ],
      items: [
        { id: 1, name: "Ronald", quantity: 1, price: 300, total: 300 },
        { id: 1, name: "Ronald", quantity: 1, price: 300, total: 300 },
        { id: 1, name: "Ronald", quantity: 1, price: 300, total: 300 },
        { id: 1, name: "Ronald", quantity: 1, price: 300, total: 300 },
        { id: 1, name: "Ronald", quantity: 1, price: 300, total: 300 },
        { id: 1, name: "Ronald", quantity: 1, price: 300, total: 300 }
      ]
    };
  },
  computed: {
    total() {
      return this.items.reduce(
        (acc, item) => acc + item.price * item.quantity,
        0
      );
    }
  },
  methods: {
    addRow() {
      this.items.push({ id: 0, name: "", quantity: 1, price: 0, total: 0 });
    },
    deleteRow(index) {
      this.items.splice(index, 1);
    }
  },
  filters: {
    currency(value) {
      return value.toFixed(2);
    }
  }
};
</script>

<style scoped>
.margin {
  margin-left: 5px;
  margin-right: 5px;
}
</style>