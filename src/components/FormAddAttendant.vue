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
                  label="Telefoonnummer*"
                  v-model="phonenmbr"
                  prepend-icon="mdi-phone"
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Password*"
                  type="password"
                  v-model="password"
                  prepend-icon="mdi-lock"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
          <v-btn color="red" text left class="left" @click="close">
            <v-icon>mdi-delete</v-icon>
            Close
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
  data() {
    return {
      dialog: false,
      firstname: "",
      lastname: "",
      email: "",
      phonenmbr: "",
      password: "",
    };
  },
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
        // alert("Begeleider is toegevoegd");
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