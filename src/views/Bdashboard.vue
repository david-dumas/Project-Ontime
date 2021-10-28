<template>
<div class="bdashboard">
    <Header />
  <h1>
    Dashboard
  </h1>
  <Table/>
  <Footer />

</div>

</template>

<script>

import Header from '../components/Header';
import Footer from '../components/Footer';
import Table from '../components/Table.vue';


export default {
    name: 'Bdashboard',
    components: {
        Header,
        Footer,
        Table
    }

}
</script>


<style>

#table, th, td{
  border: 1px solid black;
  text-align: center;
}

h1 {
  text-align: center;
}
</style>