<template>
  <div>
    <h1>
      Statistics
    </h1>
    <p>Here is some information. This is the Statistics page</p>
    <form id="statisticsform">
      <p>Carrier Code:</p>
      <input v-model="carrier_code" placeholder="Enter code">
      <p>Airport Code:</p>
      <input v-model="airport_code" placeholder="Enter code">
      <p>Month:</p>
      <input v-model="month" placeholder="Enter month">
      <p><button v-on:click="submit">Submit</button></p>
    </form>
    <div v-if="show">
      <p># of delays</p>
      <table align="center">
        <tr>
          <th>Carrier</th>
          <th>Late aircraft</th>
          <th>National aviation system</th>
          <th>Security</th>
          <th>Weather</th>
        </tr>
        <tr v-for="message of messages">
          <td>{{message["# of delays"]['carrier']}}</td>
          <td>{{message["# of delays"]['late aircraft']}}</td>
          <td>{{message["# of delays"]['national aviation system']}}</td>
          <td>{{message["# of delays"]['security']}}</td>
          <td>{{message["# of delays"]['weather']}}</td>
        </tr>
      </table>
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
          <td>{{message["flights"]['cancelled']}}</td>
          <td>{{message["flights"]['delayed']}}</td>
          <td>{{message["flights"]['diverted']}}</td>
          <td>{{message["flights"]['on time']}}</td>
          <td>{{message["flights"]['total']}}</td>
        </tr>
      </table>
      <p>Minutes delayed</p>
      <table align="center">
        <tr>
          <th>Carrier</th>
          <th>Late aircraft</th>
          <th>National aviation system</th>
          <th>Security</th>
          <th>Weather</th>
        </tr>
        <tr v-for="message of messages">
          <td>{{message["minutes delayed"]['carrier']}}</td>
          <td>{{message["minutes delayed"]['late aircraft']}}</td>
          <td>{{message["minutes delayed"]['national aviation system']}}</td>
          <td>{{message["minutes delayed"]['security']}}</td>
          <td>{{message["minutes delayed"]['weather']}}</td>
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
            .get('http://localhost:5000/v1/statistics', {
              headers: {
                'Accept': 'application/json',
              },
              params: {
                carrier: this.carrier_code,
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
