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
      <table v-if="reason === null" align="center">
        <tr>
          <th>Code</th>
          <th>Name</th>
          <th>Carrier</th>
          <th>Late aircraft</th>
          <th>National aviation system</th>
          <th>Security</th>
          <th>Weather</th>
        </tr>
        <tr v-for="message of messages">
          <td>{{message["carrier"]['code']}}</td>
          <td>{{message["carrier"]['name']}}</td>
          <td>{{message["delays"]['carrier']}}</td>
          <td>{{message["delays"]['late aircraft']}}</td>
          <td>{{message["delays"]['national aviation system']}}</td>
          <td>{{message["delays"]['security']}}</td>
          <td>{{message["delays"]['weather']}}</td>
        </tr>
      </table>
        <table v-if="reason !== null" align="center">
          <tr>
            <th>Code</th>
            <th>Name</th>
            <th>{{reason}}</th>
          </tr>
          <tr v-for="message of messages">
            <td>{{message["carrier"]['code']}}</td>
            <td>{{message["carrier"]['name']}}</td>
            <td>{{message["delays"][reason]}}</td>
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
