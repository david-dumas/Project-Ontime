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
    </v-app-bar>
  </nav>
</template>

<script>
import Helppopup from "../components/Helppopup";

export default {
  name: "Loginheader",
  components: {
    Helppopup,
  },
};
</script>

<style>
.help {
  margin-right: 5px;
}
</style>