<template>
  <v-footer
    app bottom fixed
    padless
    color="#006027"
  >
    <v-card
      flat
      tile
      color="#006027"
    >

      <v-card-text class="text-center white--text">
        Lorem ipsum
        {{ new Date().getFullYear() }}
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style>
  
</style>