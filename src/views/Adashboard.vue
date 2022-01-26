<template>
  <div classname="adashboard">
    <AHeader />
    <h1>Admin Dashboard</h1>
    <div class="tables">
      <v-container>
        <v-row>
          <v-col>
            <Department />
          </v-col>
          <v-col>
            <Attendant />
          </v-col>
          <v-col>
            <Client />
          </v-col>
        </v-row>
      </v-container>
    </div>
    <Footer />
  </div>
</template>

<script>
import AHeader from "../components/AHeader.vue";
import Footer from "../components/Footer.vue";
import Attendant from "../components/Attendant.vue";
import Client from "../components/Client.vue";
import Department from "../components/Department.vue";
export default {
  name: "Adashboard",
  components: {
    Footer,
    AHeader,
    Attendant,
    Client,
    Department,
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 1em;
  margin-bottom: 1em;
}
v-col {
  width: 300px;
}
</style>
