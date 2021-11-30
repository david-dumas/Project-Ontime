<template>
    <div class="login">
        <br>
        <br>
         <!-- Bartimeus logo -->
        <div class="image">
            <img src='../assets/logo-Bartiméus.png' width="150">
        </div>
        <br>
        <br>
        <br>
        <h3>Login</h3>
        
        <!-- Login form -->
        <v-container
        fluid style="width:500px"
        >
            <v-form
                @submit.prevent="Loginform"
                method="POST"
                ref="form"
                v-model="valid"
                lazy-validation
            >
                <v-text-field
                id="email"
                v-model="email"
                label="E-mail"
                required
                ></v-text-field>

                <v-text-field
                type='password'
                id="password"
                v-model="password"
                label="Password"
                required
                ></v-text-field>

                <v-btn
                type="submit"
                color="primary"
                >
                Login
                </v-btn>

                 <!-- Moet er een 'is dit een admin account' knop komen? 
                
                <p>Is dit een Admin account?</p>
                <input type="checkbox" id="checkbox" v-model="checked">
                <label for="checkbox">{{ checked }}</label>

                -->

            </v-form>
        </v-container>
    </div>
</template>

<script>

export default {
    name: "Loginform",
    data(){
        return {
                email: "",
                password: "",
        }
    },
    methods: {
        async Loginform(){
            const data = {
                email: this.email,
                password: this.password
            };

            /* Ophalen gebruiker uit de database */
            const response = await fetch('http://localhost:5000/login_request', {
                method: 'POST',
                headers: 
                    {"Content-Type":"application/json"},
                    credentials: "include",
                    body: JSON.stringify(data),
                });

                console.log(response)

                /* JWT token opslaan in local storage */
                localStorage.setItem('token', response.data.token)

                /* if statement om te kijken of de gebruiker authenticated is */
                if(response.status == 200){ 
                    let redirect_url = this.$route.query.redirect || '/begeleider-dashboard'
                    this.$router.push(redirect_url) 
                } else {
                    localStorage.removeItem('token', response.data.token)
                    alert("Verkeerde inlog gegevens")
                }        
        }
    }
}

// isAuthenticated variabele aanmaken
//let isAuthenticated = true

/* function routerAuthCheck() {
        if (response == 200){
            isAuthenticated = true
        } else {
            isAuthenticated = false
        }
    } */

    // zet authcheck naar true zodat de pagina kan worden geladen.
                    // isAuthenticated = true;

//export { isAuthenticated }

</script>

<style scoped>

.login {
    margin-top: 40px;
    text-align: center;
}

.v-btn {
    margin-right: 1em;
}

</style>                