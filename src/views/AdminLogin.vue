<template>
  <div class="html">
    <Loginheader />
    <div class="login">
      <AdmLogin />
    </div>
    <Footer />
  </div>
</template>

<script>
import Loginheader from "../components/Loginheader";
import Footer from "../components/Footer";
import AdmLogin from "../components/AdmLogin";

export default {
  name: "login",
  components: {
    Footer,
    Loginheader,
    AdmLogin,
  },
};
</script>

<style scoped>
</style>