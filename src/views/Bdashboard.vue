<template>
<div class="bdashboard">
    <Header />
  <h1>
    Dashboard
  </h1>
  <table>
    <tr>
      <th>Company</th>
      <th>Contact</th> 
      <th>Country</th>
    </tr>
    <tr>
      <td>Alfreds Futterkiste</td>
      <td>Maria Anders</td> 
      <td>Germany</td>
    </tr>
    <tr>
      <td>Centro comercial Moctezuma</td>
      <td>Francisco Chang</td> 
      <td>Mexico</td>
    </tr>
  </table>
  <Footer />

</div>

</template>

<script>

import Header from '../components/Header';
import Footer from '../components/Footer';


export default {
    name: 'Bdashboard',
    components: {
        Header,
        Footer
    }

}
</script>


<style>

#table, th, td{
  border: 1px solid black;
  text-align: center;
}

</style>