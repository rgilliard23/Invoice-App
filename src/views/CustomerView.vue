<template>
  <div>
    <b-container class="clear fullHeight" fluid></b-container>
    <b-navbar style="height:10vh;" type="dark" variant="info">
      <b-navbar-brand>
        <h1>Customers</h1>
      </b-navbar-brand>
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-button
            :disabled="InvoiceIncomplete"
            v-b-modal.InvoiceTemplate
            class="margin"
            size="lg"
            variant="danger"
          >Invoice Pdf</b-button>
          <b-button
            :disabled="InvoiceIncomplete"
            class="margin"
            size="lg"
            variant="secondary"
          >Export To Excel</b-button>
          <b-button
            :disabled="InvoiceIncomplete"
            class="margin"
            size="lg"
            variant="success"
          >Save Invoice</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "CustomerView"
};
</script>

<style>
</style>