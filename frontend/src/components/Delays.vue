<template>
  <div>
    <h1>
      Delays
    </h1>
    <p>Here is some information. This is the Delays page</p>
    <form id="flightsform">
      <p>Airport Code:</p>
      <input v-model="airport_code" placeholder="Enter code">
      <p>Reason:</p>
      <input v-model="reason" placeholder="Enter reason">
      <p>Month:</p>
      <input v-model="month" placeholder="Enter month">
      <p><button v-on:click="submit">Submit</button></p>
    </form>
  </div>
</template>

<script>
    export default {
        name: "Delays",
        data: {
          airport_code: "",
          reason: "all",
          month: 0
        },
        methods: {
          submit: function() {
            alert(this.airport_code + " " + this.reason + " "+ this.month)
          }
        }
    }
</script>

<style scoped>

</style>
