<template>
    <div class="login">

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
                password: this.password,
            };

            /* Ophalen gebruiker uit de database */
            const response = await fetch('http://127.0.0.1:5000/login_request', {
                method: 'POST',
                headers: 
                    {"Content-Type":"application/json"},
                    credentials: "include",
                    body: JSON.stringify(data),
                });

                const res = await response.json();

                /* if statement om te kijken of de gebruiker authenticated is */
                if(res.val == true){ 

                    /* JWT token opslaan in local storage */
                    localStorage.setItem('token', res.token)
                
                    //Commit naar de store dat de gebruiker is ingelogd
                    this.$store.commit("setAuthentication", true);

                    let redirect_url = this.$route.query.redirect || '/begeleider-dashboard'
                    this.$router.push(redirect_url) 

                //CHECKEN OF GEBRUIKER EEN ADMIN IS NA FOUTIEVE USER AUTH

                } else if(res.val == false) {
                    const responseAdmin = await fetch('url', {
                        method: 'POST',
                        headers:
                            {"Content-Type":"application/json"},
                            credentials: "include",
                            body: JSON.stringify(data),
                    });

                    const resAdmin = await responseAdmin.json();

                    if(response.val == true){

                        localStorage.setItem('token', resAdmin.token)

                        this.$store.commit("setAuthentication", true);

                        let redirect_url = this.$route.query.redirect || '/admin-dashboard'
                        this.$router.push(redirect_url) 

                    } else if(response.val == false){
                        console.log("Error")
                    }
                } else {
                    alert("Verkeerde inlog gegevens")
                }        
        }
    }
}

</script>

<style scoped>

.login {
    margin-top: 40px;
    text-align: center;
}

.v-btn {
    margin-right: 1em;
}

.image {
    margin-top: 1em;
}

</style>