<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        color="#006027"
        dark
        class="mx-2"
        fab
        small
        v-bind="attrs"
        v-on="on"
      >
        <v-icon dark>mdi-account-plus</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">Begeleider Toevoegen</span>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="addAttendant">
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="Voornaam*"
                  v-model="firstname"
                  prepend-icon="mdi-account"
                  :rules="[rules.required, rules.max]"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="Achternaam*"
                  v-model="lastname"
                  :rules="[rules.required, rules.max]"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Email*"
                  v-model="email"
                  :rules="[rules.required, rules.email]"
                  prepend-icon="mdi-email"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Telefoonnummer*"
                  v-model="phonenmbr"
                  :rules="[rules.required, rules.tel]"
                  prepend-icon="mdi-phone"
                  pattern="^\d{10}$"
                  type="tel"
                  required
                  counter
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Wachtwoord*"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  hint="Tenminste 8 karakters"
                  counter
                  @click:append="show1 = !show1"
                  :type="show1 ? 'text' : 'password'"
                  v-model="password"
                  prepend-icon="mdi-lock"
                  :rules="[rules.required, rules.min]"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*Verplichte velden</small>
          <v-btn color="red" text left class="left" @click="close">
            <v-icon>mdi-delete</v-icon>
            Annuleren
          </v-btn>
          <v-btn color="green" text right class="left" type="submit">
            <v-icon>mdi-content-save</v-icon>
            Opslaan
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import { db } from "@/main";
export default {
  data: () => ({
    dialog: false,
    firstname: "",
    lastname: "",
    email: "",
    phonenmbr: "",
    password: "",
    show1: false,
    rules: {
      required: (value) => !!value || "Verplicht",
      max: (value) => (value || "").length <= 20 || "Max 20 karakters",
      min: (value) => (value || "").length > 7 || "Min 8 karakters",
      tel: (value) =>
        (value || "").length == 10 || "Telefoonnummer moet 10 karakters hebben",
      email: (value) => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return pattern.test(value) || "Incorrecte e-mail.";
      },
    },
  }),
  mounted() {
    this.getAttendant();
  },
  methods: {
    async getAttendant() {
      let snapshot = await db.collection("Begeleiders").get();
      let attendants = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        attendants.push(appData);
      });
      this.attendants = attendants;
    },
    async addAttendant() {
      if (
        this.firstname &&
        this.lastname &&
        this.email &&
        this.phonenmbr &&
        this.password
      ) {
        await db.collection("Begeleiders").add({
          firstname: this.firstname,
          lastname: this.lastname,
          email: this.email,
          phonenmbr: this.phonenmbr,
          password: this.password,
        });
        this.firstname = "";
        this.lastname = "";
        this.email = "";
        this.phonenmbr = "";
        this.password = "";
        alert("Begeleider is toegevoegd");
        window.location.href = "admin-dashboard";
        this.getAttendant();
        this.dialog = false;
      } else {
        alert("Voornaam, achternaam, email en wachtwoord zijn verplicht");
      }
    },
    close() {
      if (confirm("Weet u zeker dat u wilt afsluiten?")) {
        this.dialog = false;
        this.firstname = "";
        this.lastname = "";
        this.email = "";
        this.phonenmbr = "";
        this.password = "";
      } else {
        this.dialog = true;
      }
    },
  },
};
</script>
