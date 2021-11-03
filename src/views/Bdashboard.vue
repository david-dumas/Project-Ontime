<template>
<div class="bdashboard">
    <Header />
  <h1>
    Dashboard
  </h1>

    <div class="tabeldash">

    <Tabeldash />

    </div>

    <div class="afsprakendash">

    <Afsprakendash />

    </div>
  
  <Footer />

</div>

</template>

<script>
import Header from '../components/Header';
import Footer from '../components/Footer';
import Afsprakendash from '../components/Afsprakendash.vue';
import Tabeldash from '../components/Tabeldash';
export default {
    name: 'Bdashboard',
    components: {
        Header,
        Footer,
        Afsprakendash,
        Tabeldash
    }
}
</script>

<style>
.bdashboard h1 {
  text-align: center;
}
.afsprakendash {
  width: 500px;
  float: right;
  margin-right: 3em;
}
.tabeldash {
  width: 500px;
  float: left;
  margin-left: 3em;
}
</style>