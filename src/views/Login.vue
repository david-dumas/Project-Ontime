<template>
  <div class='html'>
  <Header />
  <div class='login'>    
      <h1>Login pagina</h1>
    </div>
    <Footer />
  </div>
</template>

<script>

import Header from '../components/Header'
import Footer from '../components/Footer'

export default {
  name: 'login',
  components: {
      Footer,
      Header
  }
}
</script>

<style scoped>

.html{
  height: 100%;
}

</style>