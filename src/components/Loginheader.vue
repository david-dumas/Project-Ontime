<template>
  <nav>
    <v-toolbar flat app color="#018245">
      <v-toolbar-title class="text-uppercase white--text">
        <span class="font-weight-light">Ontime</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <div class="help">
        <Helppopup />
      </div>
    </v-toolbar>
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