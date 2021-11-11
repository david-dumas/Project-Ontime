<template>
  <div class='html'>
  <Header />
  <div class='login'>    
      <Loginform />
    </div>
    <Footer />
  </div>
</template>

<script>

import Header from '../components/Header'
import Footer from '../components/Footer'
import Loginform from '../components/Loginform'

export default {
  name: 'login',
  components: {
      Footer,
      Header,
      Loginform
  }
}
</script>

<style scoped>

</style>