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
    <div v-if="show">
      <p>Minutes delayed</p>
      <table align="center">
        <tr>
          <th>Code</th>
          <th>Delay in minutes</th>
        </tr>
        <tr v-for="message of messages">
          <td>{{message["carrier"]}}</td>
          <td>{{message["delay"]}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'
    export default {
      name: "CarriersOnAirport",
      data() {
        return {
          messages: [],
          show: false,
          reason: null,
          airport_code: null,
          month: null,
        }
      },
      methods: {
        submit: function() {
          axios
            .get('http://localhost:5000/v1/statistics/delays', {
              headers: {
                'Accept': 'application/json',
              },
              params: {
                airport: this.airport_code,
                carrier_specific: this.reason,
                month: this.month,
              }
            })
            .then((response) => {
              this.show = true
              this.messages = response.data
            })
        }
      }
    }
</script>

<style scoped>

</style>
