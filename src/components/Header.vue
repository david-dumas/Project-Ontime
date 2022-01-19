<template>
  <nav>
    <v-app-bar flat app color="#018245">
      <v-app-bar-title class="text-uppercase white--text">
        <span class="font-weight-light">Ontime</span>
      </v-app-bar-title>

      <v-spacer></v-spacer>

      <div class="help">
        <Helppopup />
      </div>

      <v-btn class="button" depressed color="white">
        <router-link
          to="/begeleider-dashboard"
          active-class="active"
          tag="button"
          exact
          class="nav-btn"
        >
          Dashboard
        </router-link>
      </v-btn>

      <v-btn class="button" depressed color="white">
        <router-link
          to="/agenda"
          active-class="active"
          tag="button"
          exact
          clasass="nav-btn"
        >
          Agenda
        </router-link>
      </v-btn>


      <!-- @click="logout" LOGUIT FUNCTIE DIE WE (NOG NIET) GEBRUIKEN -->
      <v-btn class="button" depressed color="white">
        <router-link
          to="/"
          active-class="active"
          tag="button"
          exact
          class="nav-btn"
        >
          Log uit
        </router-link>
      </v-btn>
    </v-app-bar>
  </nav>
</template>

<script>
import Helppopup from "../components/Helppopup";

export default {
  name: "Header",
  components: {
    Helppopup,
  },
};

/* Loguit functie die kan worden aangeroepen na klikken log uit knop 

logout({commit}){
  return new Promise((resolve, reject) => {
    commit('logout')
    this.$store.commit("setAuthentication", false);
    localStorage.removeItem('token')
  })
}

*/
</script>

<style>
.button {
  margin-right: 5px;
}
</style>