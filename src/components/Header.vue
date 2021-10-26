<template>
    <nav>
        <v-toolbar flat app color="#018245">
            <v-toolbar-title class="text-uppercase grey--text">
                <span class="font-weight-light">Ontime</span>
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn
            depressed
            color="primary"
            >
            <router-link to="/" active-class="active" tag="button" exact class="nav-btn">
                    Log uit
        </router-link>
            </v-btn>

        <router-link to="/" active-class="active" tag="button" exact class="nav-btn">
                    Log uit
        </router-link>

      <router-link to="/help" active-class="active" tag="button" exact class="nav-btn">
                    Help
        </router-link>

      <router-link to="/agenda" active-class="active" tag="button" exact clasass="nav-btn">
                    Agenda
        </router-link>

        <router-link to="/begeleider-dashboard" active-class="active" tag="button" exact class="nav-btn">
                    Dashboard
        </router-link>
        
        </v-toolbar>
    </nav>
</template>

<script>
export default {
    name: 'Header2'
}
</script>

<style>

</style>