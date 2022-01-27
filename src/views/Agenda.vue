<template>
  <div class="agenda">
    <Header />
    <div class="Titel">
      <v-title class="text-h3">Agenda</v-title>
    </div>

    <div class="calendar">
      <Calendar />
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import Calendar from "../components/Calendar";

export default {
  name: "Agenda",
  components: {
    Footer,
    Header,
    Calendar,
  },
};
</script>

<style>
.Titel {
  text-align: center;
  margin-top: 3em;
}

.calendar {
  margin-top: 3em;
  margin-right: 5em;
  margin-left: 5em;
  margin-bottom: 5em;
}
</style>