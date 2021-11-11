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
                ref="form"
                v-model="valid"
                lazy-validation
            >
                <v-text-field
                v-model="name"
                :rules="nameRules"
                label="Name"
                required
                ></v-text-field>

                <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                required
                ></v-text-field>
                
                
                <!-- @click="loginUser"  -->
                <v-btn
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
    

}
</script>

<style scoped>

.login {
    margin-top: 40px;
    text-align: center;
}


</style>

method: {
    getUser(){
        fetch('', {
            method: GET,
            headers: {
                "Content-Type":"application/json"
                }
            })
            .then(resp => resp.json())
            .then(data => {
                console.log(data);
            }) 
            .catch(error => {
                console.log(error)
        })
    }
}