<template>
  <div class="login">
    <div class="image">
      <img src="../assets/logo-Bartiméus.png" width="150" />
    </div>
    <br />
    <br />
    <br />
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

        <v-btn type="submit" color="primary"> Login </v-btn>
      </v-form>
    </v-container>
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

      const response = await fetch("http://145.89.192.95:5555/login_request_attendant", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(data),
      });

      const res = await response.json();

      if (res.val == true) {
  
        localStorage.setItem("token", res.token);

        this.$store.commit("setAuthentication", true);

        let redirect_url =
          this.$route.query.redirect || "/begeleider-dashboard";
        this.$router.push(redirect_url);

        //CHECKEN OF GEBRUIKER EEN ADMIN IS NA FOUTIEVE USER AUTH
      } else if (res.val == false) {
        const responseAdmin = await fetch("http://145.89.192.95:5555/login_request_admin", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          credentials: "include",
          body: JSON.stringify(data),
        });

        const res2 = await responseAdmin.json();

        if (res2.val == true) {
          localStorage.setItem("token", res2.token);

          this.$store.commit("setAuthentication", true);

          let redirect_url = this.$route.query.redirect || "/admin-dashboard";
          this.$router.push(redirect_url);
        } else if (res2.val == false) {
          console.log("Error");
        } else {
          alert("Dit werkt niet zemmer")
        }
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

.v-btn {
  margin-right: 1em;
}

.image {
  margin-top: 1em;
}
</style>