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
      <p><button v-on:click="submit">Submit</button></p>
    </form>
    <div v-if="show">
      <p>Minutes delayed</p>
      <table v-if="reason !== null" align="center">
        <tr>
          <th>Carrier</th>
          <th>Mean</th>
          <th>Median</th>
          <th>Standard Deviation</th>
        </tr>
        <tr v-for="message of messages">
          <td>{{message['carrier']}}</td>
          <td>{{message['statistics'][reason]['mean']}}</td>
          <td>{{message['statistics'][reason]['median']}}</td>
          <td>{{message['statistics'][reason]['stdev']}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "DescriptiveStatistics",
        data()  {
          return {
            airport_code1: "",
            airport_code2: "",
            carrier_code: null,
            reason: null,
            messages: [],
            show: false,
          }
        },
        methods: {
          submit: function() {
            axios
              .get('http://localhost:5000/v1/statistics/descriptive', {
                headers: {
                  'Accept': 'application/json',
                },
                params: {
                  airport1: this.airport_code1,
                  airport2: this.airport_code2,
                  carrier_code: this.carrier_code,
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
