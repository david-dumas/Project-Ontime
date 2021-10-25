<template>
  <v-card class="overflow-hidden">
    <v-app-bar
      absolute
      color="#018245"
      dark
      prominent
    >

      <v-spacer></v-spacer>

        <router-link to="/" active-class="active" tag="button" exact class="nav-btn">
                <div class="link-container">
                    Log uit
                </div>
        </router-link>

        <!-- <v-spacer></v-spacer> -->

      <router-link to="/help" active-class="active" tag="button" exact class="nav-btn">
                <div class="link-container">
                    Help
                </div>
        </router-link>

      <router-link to="/agenda" active-class="active" tag="button" exact class="nav-btn">
                <div class="link-container">
                    Agenda
                </div>
        </router-link>

        <router-link to="/bdashboard" active-class="active" tag="button" exact class="nav-btn">
                <div class="link-container">
                    Dashboard
                </div>
        </router-link>

      <template v-slot:extension>
        
      </template>
    </v-app-bar>
   
      <v-container style="height: 250px;"></v-container>
    
  </v-card>
</template>

<script>
export default {
    name: 'Header'
}
</script>
<style>

    
</style>