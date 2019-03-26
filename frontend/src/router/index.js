import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Statistics from "../components/Statistics";
import Home from "../components/Home";
import Airports from "../components/Airports";
import Carriers from "../components/Carriers";
import CarriersOnAirport from "../components/CarriersOnAirport";
import Flights from "../components/Flights";
import Delays from "../components/Delays";
import DescriptiveStatistics from "../components/DescriptiveStatistics";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/airports',
      name: 'Airports',
      component: Airports
    },
    {
      path: '/carriers',
      name: 'Carriers',
      component: Carriers
    },
    {
      path: '/carriersonairport',
      name: 'Carriers on Airports',
      component: CarriersOnAirport
    },
    {
      path: '/statistics',
      name: 'Statistics',
      component: Statistics
    },
    {
      path: '/flights',
      name: 'Flights',
      component: Flights
    },
    {
      path: '/delays',
      name: 'Delays',
      component: Delays
    },
    {
      path: '/descriptivestatistics',
      name: 'Descriptive Statistics',
      component: DescriptiveStatistics
    }
  ]
})
