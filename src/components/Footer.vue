<template>
  <v-footer app bottom fixed color="#006027" padless>
    <v-card
      flat
      tile
      color="#006027"
      class="white--text text-center"
      width="100%"
    >
      <v-card-text class="white--text">
        Ontime - {{ new Date().getFullYear() }}
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style>
</style>