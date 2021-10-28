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
      width="100%"
    >

      <v-card-text class="py-2 white--text text-center">
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