<template>
    <div class="login">
        <br>
        <br>
        <div class="image">
            <img src='../assets/logo-Bartiméus.png' width="150">
        </div>
        <br>
        <br>
        <br>
        <h3>Login</h3>
        
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
                v-model="formData.email"
                label="E-mail"
                required
                ></v-text-field>

                <v-text-field
                id="password"
                v-model="formData.password"
                label="Password"
                required
                ></v-text-field>

                <!-- Moet er een 'is dit een admin account' knop komen? -->
                
                <v-btn
                type='submit'
                @click="submit"
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
            formData: {
                email: "",
                password: "",
            },
        }
    },
    methods: {
        Loginform(){
             fetch(('http://127.0.0.1:5000/login_request', this.formData),{
                method: 'POST',
                headers: 
                    {"Content-Type":"application/json"},
                body: JSON.stringify
                })
                .then(resp => resp.json())
                .then(json => {console.log(json);
                }) 
                .catch(error => {console.log(error)
            })
            /* Doorverwijzen naar de dashboard pagina */
            this.$router.push('Bdashboard');
        }
    }
    
}

</script>

<style scoped>

.login {
    margin-top: 40px;
    text-align: center;
}

</style>

