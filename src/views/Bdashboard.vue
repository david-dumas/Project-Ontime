<template>
  <div class="bdashboard">
      <Header />
        <h1>
        Dashboard
        </h1>

      <div class="tabeldash">
        <Client />
      </div>

      <div class="afsprakendash">
        <Afsprakendash />
      </div>
    
    <Footer />

  </div>
</template>

<script>
//import axios from 'axios'

import Header from '../components/Header';
import Footer from '../components/Footer';
import Afsprakendash from '../components/Afsprakendash.vue';
import Client from '../components/Client'

export default {
    name: 'Bdashboard',
    components: {
        Header,
        Footer,
        Afsprakendash,
        Client
    },

    /* OPHALEN GEBRUIKER IN DATABASE, AUTHORIZATION CHECKEN UIT LOCAL STORAGE

    async created() {
      const response = await axios.get('https:......./user', {
        headers: {
          Authorizations: 'Bearer' + localStorage.getItem('token')
        }
      });

      console.log(response)
    },
     */
}
</script>

<style>
.bdashboard h1 {
  text-align: center;
  margin-top: 1em;
  margin-bottom: 1em;
}
.afsprakendash {
  width: 700px;
  float: right;
  margin-right: 4em;
}
.tabeldash {
  width: 700px;
  float: left;
  margin-left: 4em;
}
</style>