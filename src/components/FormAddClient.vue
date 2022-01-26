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
        <span class="text-h5">Client Toevoegen</span>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="addClient">
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
                  prepend-icon="mdi-email"
                  :rules="[rules.required, rules.email]"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Telefoonnummer"
                  v-model="phonenmbr"
                  prepend-icon="mdi-phone"
                  :rules="[rules.required, rules.tel]"
                  pattern="^\d{10}$"
                  type="tel"
                  required
                  counter
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Zorgpasnummer*"
                  v-model="cardnmbr"
                  prepend-icon="mdi-card-account-details"
                  :rules="[rules.required, rules.max]"
                  type="number"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-select
                  prepend-icon="mdi-office-building"
                  :items="names"
                  label="Afdeling*"
                  v-model="department"
                  required
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*Verplichte velden</small>
          <v-btn color="red" text @click="close">
            <v-icon>mdi-delete</v-icon>
            Annuleren
          </v-btn>
          <v-btn color="green" text type="submit">
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
    cardnmbr: "",
    department: "",
    departments: [],
    names: [],
    rules: {
      required: (value) => !!value || "Verplicht",
      max: (value) => (value || "").length <= 20 || "Max 20 karakters",
      tel: (value) =>
        (value || "").length == 10 || "Telefoonnummer moet 10 karakters hebben",
      email: (value) => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return pattern.test(value) || "Incorrecte e-mail.";
      },
    },
  }),
  mounted() {
    this.getClient();
    this.getDepartments();
  },
  methods: {
    async getClient() {
      let snapshot = await db.collection("Clienten").get();
      let clienten = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        clienten.push(appData);
      });
      this.clienten = clienten;
    },
    async addClient() {
      if (this.firstname && this.lastname && this.email) {
        await db.collection("Clienten").add({
          firstname: this.firstname,
          lastname: this.lastname,
          email: this.email,
          phonenmbr: this.phonenmbr,
          cardnmbr: this.cardnmbr,
          department: this.department,
        });
        this.getClient();
        this.firstname = "";
        this.lastname = "";
        this.email = "";
        this.phonenmbr = "";
        this.cardnmbr = "";
        this.department = "";
        this.dialog = false;
        alert("Cliënt is toegevoegd");
        window.location.href = "admin-dashboard";
      } else {
        alert("Voornaam, achternaam en email zijn verplicht");
      }
    },
    // Haalt begeleiders op uit firebase
    async getDepartments() {
      let snapshot = await db.collection("Afdelingen").get();
      let departments = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        departments.push(appData);
      });
      for (let i = 0; i < departments.length; i++) {
        var name = departments[i].name;
        this.names.push(name);
      }
    },
    close() {
      if (confirm("Weet u zeker dat u wilt afsluiten?")) {
        this.dialog = false;
        this.firstname = "";
        this.lastname = "";
        this.email = "";
        this.phonenmbr = "";
        this.cardnmbr = "";
        this.department = "";
      } else {
        this.dialog = true;
      }
    },
  },
};
</script>
