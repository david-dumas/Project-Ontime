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
            <router-link to="/" active-class="active" tag="button" exact class="nav-btn" @click="logout">
                        Log uit
            </router-link>
        </v-btn>

        </v-toolbar>
    </nav>
</template>

<script>
import Helppopup from '../components/Helppopup'

export default {
    name: 'AHeader',
    components: {
        Helppopup
    }
}
</script>

<style>
    .button{
        margin-right: 5px;
    }
</style>