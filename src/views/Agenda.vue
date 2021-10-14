<template>
  <div class='agenda'>
      <Header />
        <div class='agenda'>
            <h1>Agenda</h1>
        </div>
      <Footer />
  </div>
</template>

<script>

import Header from '../components/Header'
import Footer from '../components/Footer'

export default {
    name: 'Agenda',
    components: {
      Footer,
      Header
  }
}
</script>

<style>

.agenda{
  height: 100%;
}

</style>