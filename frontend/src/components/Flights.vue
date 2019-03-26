<template>
  <div>
    <h1>
      Flights
    </h1>
    <p>Here is some information. This is the Flights page</p>
    <form id="flightsform">
      <p>Carrier Code:</p>
      <input v-model="carrier_code" placeholder="Enter code">
      <p>Airport Code:</p>
      <input v-model="airport_code" placeholder="Enter code">
      <p>Month:</p>
      <input v-model="month" placeholder="Enter month">
      <p><button v-on:click="submit">Submit</button></p>
    </form>
  </div>
</template>

<script>
    export default {
        name: "Flights",
        data: {
          carrier_code: "",
          airport_code: "",
          month: 0
        },
        methods: {
          submit: function() {
            alert(this.carrier_code + " " + this.airport_code + " "+ this.month)
          }
        }
    }
</script>

<style scoped>

</style>
