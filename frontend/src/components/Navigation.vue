<template>
  <nav>
    <router-link class="spacing" v-for="routes in links"
                 v-bind:key="routes.id"
                 :to="`${routes.page}`">{{routes.text}}</router-link>
  </nav>
</template>

<script>
    export default {
        name: "Navigation",
        data() {
          return {
            links: [
              {
                id:0,
                text: 'Home',
                page: '/'
              },
              {
                id:1,
                text: 'Airports',
                page: '/airports'
              },
              {
                id:2,
                text: 'Carriers',
                page: '/carriers'
              },
              {
                id:3,
                text: 'Carriers on Airport',
                page: '/carriersonairport'
              },
              {
                id:4,
                text: 'Statistics',
                page: '/statistics'
              },
              {
                id:5,
                text: 'Flights',
                page: '/flights'
              },
              {
                id:6,
                text: 'Delays',
                page: '/delays'
              },
              {
                id:7,
                text: 'Descriptive Statistics',
                page: '/descriptivestatistics'
              }
            ]
          }
        }
    }
</script>

<style scoped>
  .spacing {
    Margin-right: 10px;
  }
</style>
