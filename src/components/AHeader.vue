<template>
    <nav>
        <v-toolbar flat app color="#018245">
            <v-toolbar-title class="text-uppercase white--text">
                <span class="font-weight-light">Ontime</span>
            </v-toolbar-title>

            <v-spacer></v-spacer>

        <v-btn
            class="button"
            depressed
            color="white"
            >
            <router-link to="/admin-dashboard" active-class="active" tag="button" exact class="nav-btn">
                        Dashboard
            </router-link>
        </v-btn>
        
        <v-btn
            class="button"
            depressed
            color="white"
            >
            <router-link to="/help" active-class="active" tag="button" exact class="nav-btn">
                        Help
            </router-link>
        </v-btn>

        <v-btn
            class="button"
            depressed
            color="white"
            >
            <router-link to="/" active-class="active" tag="button" exact class="nav-btn" @click="logout">
                        Log uit
            </router-link>
        </v-btn>

        </v-toolbar>
    </nav>
</template>

<script>
export default {
    name: 'AHeader'
}
</script>

<style>
    .button{
        margin-right: 5px;
    }
</style>