<template>
  <div>
    <h1>
      Airports
    </h1>
    <p>Here is some information. This is the Airport page</p>
    <div>
      <p>Get all airports</p>
      <button v-on:click="submit">Submit</button>
    </div>
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
        name: "Airports",
        data() {
          return {
            messages: [],
            show: false,
          }
        },
        methods: {
          submit: function() {
            axios
              .get('http://localhost:5000/v1/airports', {
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
