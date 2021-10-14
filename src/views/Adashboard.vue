<template>
    <div classname="adashboard">
  <Header />
  <h1>Admin Dashboard</h1>

  <Footer />
  </div>
</template>

<script>

import Header from '../components/Header'
import Footer from '../components/Footer'

export default {
    name: 'Adashboard',
    components: {
      Footer,
      Header
  }
}

</script>

<style>

</style>