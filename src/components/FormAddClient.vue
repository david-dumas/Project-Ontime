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
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="Achternaam*"
                  v-model="lastname"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Email*"
                  v-model="email"
                  prepend-icon="mdi-email"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Telefoonnummer"
                  v-model="phonenmbr"
                  prepend-icon="mdi-phone"
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Zorgpasnummer*"
                  v-model="cardnmbr"
                  prepend-icon="mdi-card-account-details"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-select
                  prepend-icon="mdi-account"
                  :items="names"
                  label="Afdeling*"
                  v-model="department"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
          <v-btn color="red" text @click="close">
            <v-icon>mdi-delete</v-icon>
            Close
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
        });
        this.getClient();
        this.firstname = "";
        this.lastname = "";
        this.email = "";
        this.phonenmbr = "";
        this.cardnmbr = "";
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
      } else {
        this.dialog = true;
      }
    },
  },
};
</script>