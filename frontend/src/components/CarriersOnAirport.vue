<template>
  <div>
    <h1>
      Carriers on Airport
    </h1>
    <p>Here is some information. This is the Carriers on Airport page</p>
    <form id="carrierform">
      <p>Airport Code:</p>
      <input v-model="code" placeholder="Enter code">
      <button v-on:click="submit">Submit</button>
    </form>
    <div>
      <table v-if="show" align="center">
        <tr>
          <th>Code</th>
          <th>Name</th>
        </tr>
        <tr v-for="message of messages">
          <td>{{message.code}}</td>
          <td>{{message.name}}</td>
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
            code: "",
          }
        },
        methods: {
          submit: function() {
            axios
              .get('http://localhost:5000/v1/airports/'+this.code+'/carriers', {
                headers: {
                  'Accept': 'application/json',
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
