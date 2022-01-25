<template>
  <div class="login">
    <div class="image">
      <img src="../assets/logo-Bartiméus.png" width="150" />
    </div>

    <h3>Beheerder login</h3>

    <v-container fluid style="width: 500px">
      <v-form
        @submit.prevent="Loginform"
        method="POST"
        ref="form"
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

        <v-btn type="submit" color="#018245" class="ma-2 white--text"> Log in </v-btn>
      </v-form>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "AdmLogin",
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
        const response = await fetch("http://145.89.192.95:5555/login_request_admin",
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

        let redirect_url = this.$route.query.redirect || "/admin-dashboard";
        this.$router.push(redirect_url);

      } else if (res.val == false) { 
          alert("Verkeerde beheerder gegevens.")
      }
    },
  }
};
</script>

<style scoped>
.login {
  margin-top: 10em;
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