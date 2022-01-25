<template>
  <div class="bdashboard">
    <Header />
    <h1>Dashboard</h1>

    <div class="tabeldash">
      <Tabeldash />
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import Tabeldash from "../components/Tabeldash";

export default {
  name: "Bdashboard",
  components: {
    Header,
    Footer,
    Tabeldash,
  },
};
</script>

<style>
.bdashboard h1 {
  text-align: center;
  margin-top: 1em;
  margin-bottom: 1em;
}
</style>