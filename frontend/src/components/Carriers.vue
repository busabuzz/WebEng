<template>
  <div>
    <h1>
      Carriers
    </h1>
    <p>Here is some information. This is the Carrier page</p>
    <div>
      <p>Get all Carriers</p>
      <button v-on:click="submit">Submit</button>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Carriers",
        methods: {
          submit: function() {
            alert("Hello")
          }
        }
    }
</script>

<style scoped>

</style>
