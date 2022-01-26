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
        lazy-validation
      >
        <v-text-field
          label="Email*"
          v-model="email"
          :rules="[rules.required, rules.email]"
          prepend-icon="mdi-email"
          required
        ></v-text-field>

        <v-text-field
          label="Wachtwoord*"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          hint="Tenminste 5 karakters"
          counter
          @click:append="show1 = !show1"
          :type="show1 ? 'text' : 'password'"
          v-model="password"
          prepend-icon="mdi-lock"
          :rules="[rules.required, rules.min]"
          required
        ></v-text-field>

        <v-btn type="submit" color="#018245" class="ma-2 white--text">
          Log in
        </v-btn>
      </v-form>
    </v-container>

    <v-container class="adminlogin">
     <div class="tekst">
        <p>Geen begeleider?</p>
      </div>
        <v-btn class="adminbutton" color="#018245" outlined>
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
      show1: false,
      rules: {
        required: (value) => !!value || "Verplicht",
        max: (value) => (value || "").length <= 20 || "Max 20 karakters",
        min: (value) => (value || "").length > 4 || "Min 5 karakters",
        tel: (value) =>
          (value || "").length == 10 ||
          "Telefoonnummer moet 10 karakters hebben",
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Incorrect mail-adres.";
        },
      },
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

        let redirect_url =
          this.$route.query.redirect || "/begeleider-dashboard";
        this.$router.push(redirect_url);
      } else if (res.status == false) {
        console.log("Je hebt een fout gemaakt");
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
  margin-top: 10em;
}

.adminlogin {
  padding-top: 5em;
  float: center;
  max-width: 22%;
  clear: both;
}

.tekst {
  float: left;
  text-align: center;
  min-width: 50%;
  max-width: 50%;
}

.adminbutton {
  float: right;
  text-align: center;
  min-width: 50%;
  max-width: 50%;
}
</style>