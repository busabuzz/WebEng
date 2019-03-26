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
  </div>
</template>

<script>
    export default {
        name: "Airports",
        methods: {
          submit: function() {
            alert("Hello")
          }
        }
    }
</script>

<style scoped>

</style>
