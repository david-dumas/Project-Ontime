<template>
    <div classname="adashboard">
  <Header />
  <h1>Admin Dashboard</h1>
  <Table/>
  <Footer />
  </div>
</template>

<script>

import Header from '../components/Header'
import Footer from '../components/Footer'
import Table from '../components/Table.vue';

export default {
    name: 'Adashboard',
    components: {
      Footer,
      Header,
      Table
  }
}

</script>

<style>
h1 {
  text-align: center;
}
</style>