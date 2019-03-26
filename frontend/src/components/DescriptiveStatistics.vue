<template>
  <div>
    <h1>
      Descriptive Statistics
    </h1>
    <p>Here is some information. This is the Descriptive Statistics page</p>
    <form id="flightsform">
      <p>Airport Code1:</p>
      <input v-model="airport_code1" placeholder="Enter code">
      <p>Airport Code2:</p>
      <input v-model="airport_code2" placeholder="Enter code">
      <p>Carrier Code:</p>
      <input v-model="carrier_code" placeholder="Enter code">
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
        name: "DescriptiveStatistics",
        data: {
          airport_code1: "",
          airport_code2: "",
          carrier_code: "",
          reason: "all",
          month: 0
        },
        methods: {
          submit: function() {
            alert(this.airport_code1 + " " + this.airport_code2 + " " + this.carrier_code + " " + this.reason + " " + this.month)
          }
        }
    }
</script>

<style scoped>

</style>
