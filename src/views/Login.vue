<template>
  <div class='html'>
  <Loginheader />
  <div class='login'>    
      <Loginform />
    </div>
    <Footer />
  </div>
</template>

<script>

import Loginheader from '../components/Loginheader'
import Footer from '../components/Footer'
import Loginform from '../components/Loginform'

export default {
  name: 'login',
  components: {
      Footer,
      Loginheader,
      Loginform
  }
}
</script>

<style scoped>

</style>