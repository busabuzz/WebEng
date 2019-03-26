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
  </div>
</template>

<script>
    export default {
        name: "CarriersOnAirport",
        data: {
          code: ""
        },
        methods: {
          submit: function() {
            alert(this.code)
          }
        }
    }
</script>

<style scoped>

</style>
