<template>

  <div class='agenda'>
      <Header />

      <Calendar />
        
      <Footer />
  </div>

</template>

<script>

import Header from '../components/Header';
import Footer from '../components/Footer';
import Calendar from '../components/Calendar';

export default {
    name: 'Agenda',
    components: {
      Footer,
      Header,
      Calendar
  }
}
</script>

<style>


</style>