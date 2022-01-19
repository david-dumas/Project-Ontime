<template>
  <div class="login">
    <div class="image">
      <img src="../assets/logo-Bartiméus.png" width="150" />
    </div>

    <h3>Login</h3>

    <v-container fluid style="width: 500px">
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
          type="password"
          id="password"
          v-model="password"
          label="Password"
          required
        ></v-text-field>

        <v-btn type="submit" color="primary"> Log in </v-btn>
      </v-form>
    </v-container>

    <p>Geen begeleider?</p>
    <v-btn class="adminbutton" color="primary">
      <router-link
        to="/admin-login"
        active-class="active"
        tag="button"
        exact
        class="nav-btn"
      >
        log in als beheerder
      </router-link>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: "Loginform",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async Loginform() {
      const data = {
        email: this.email,
        password: this.password,
      };
      const response = await fetch(
        "http://145.89.192.95:5555/login_request_attendant",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          credentials: "include",
          body: JSON.stringify(data),
        }
      );

      const res = await response.json();

      if (res.val == true) {
        localStorage.setItem("token", res.token);

        this.$store.commit("setAuthentication", true);
        console.log("De login state is veranderd naar true!")

        let redirect_url =
          this.$route.query.redirect || "/begeleider-dashboard";
        this.$router.push(redirect_url);
      } else if (res !== 200){
        console.log('Je hebt een fout gemaakt')
        alert("Vekeerde login gegevens.");
      }
    },
  },
};
</script>

<style scoped>
.login {
  margin-top: 40px;
  text-align: center;
}

.login h3 {
  margin-top: 1em;
}

.v-btn {
  margin-right: 1em;
}

.image {
  margin-top: 1em;
}
</style>