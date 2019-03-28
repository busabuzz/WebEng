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
    <div v-if="show">
      <p>Flights</p>
      <table align="center">
        <tr>
          <th>Cancelled</th>
          <th>Delayed</th>
          <th>Diverted</th>
          <th>On time</th>
          <th>Total</th>
        </tr>
        <tr v-for="message of messages">
          <td>{{message['cancelled']}}</td>
          <td>{{message['delayed']}}</td>
          <td>{{message['diverted']}}</td>
          <td>{{message['on time']}}</td>
          <td>{{message['total']}}</td>
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
          carrier_code: "",
          airport_code: "",
          month: null,
        }
      },
      methods: {
        submit: function() {
          axios
            .get('http://localhost:5000/v1/statistics/flights', {
              headers: {
                'Accept': 'application/json',
              },
              params: {
                carrier_code: this.carrier_code,
                airport: this.airport_code,
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
