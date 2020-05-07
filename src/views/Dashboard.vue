<template>
  <div>
    <b-container style="margin: 0; padding: 0;" class="w-100" fluid>
      <b-row style="margin: 0; padding: 0;">
        <b-col col lg="3" class="w-100 fullHeight" style="margin:0; padding:0;" variant="dark">
          <b-nav vertical class="w-100 fullHeight bg-dark">
            <b-nav-item active>Active</b-nav-item>
            <b-nav-item>Link</b-nav-item>
            <b-nav-item>Another Link</b-nav-item>
            <b-nav-item disabled>Disabled</b-nav-item>
          </b-nav>
        </b-col>
        <b-col col lg="9" class="clear fullHeight">
          <Invoice />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Invoice from "/Users/ronaldgilliard/invoice-app-electron/src/components/Invoice/Invoice.vue";
export default {
  name: "Dashboard",
  components: {
    Invoice
  }
};
</script>

<style>
</style>