<template>
  <v-footer
    app bottom fixed
    dark
    padless
  >
    <v-card
      flat
      tile
      color="#006027"
      class="white--text text-center"
    >

      <v-card-text class="white--text">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Tenetur autem in delectus vel modi iusto error hic molestiae reprehenderit, aliquid praesentium, facere incidunt assumenda ullam labore voluptatum, odio explicabo quibusdam!
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