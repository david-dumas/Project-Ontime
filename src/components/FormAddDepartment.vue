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
        <v-icon dark>mdi-plus</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">Afdeling Toevoegen</span>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="addDepartment">
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Afdelingnaam*"
                  v-model="name"
                  prepend-icon="mdi-office-building"
                  :rules="[rules.required, rules.max]"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Locatie*"
                  v-model="location"
                  prepend-icon="mdi-map-marker"
                  :rules="[rules.required, rules.max]"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field
                  label="Telefoonnummer*"
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
                <v-select
                  prepend-icon="mdi-account"
                  :items="names"
                  label="Hoofdbegeleider*"
                  v-model="headattendant"
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
    name: "",
    location: "",
    phonenmbr: "",
    headattendant: "",
    attendants: [],
    names: [],
    rules: {
      required: (value) => !!value || "Verplicht",
      max: (value) => (value || "").length <= 20 || "Max 20 karakters",
      tel: (value) =>
        (value || "").length == 10 || "Telefoonnummer moet 10 karakters hebben",
    },
  }),
  mounted() {
    this.getDepartment();
    this.getAttendant();
  },
  methods: {
    async getDepartment() {
      let snapshot = await db.collection("Afdelingen").get();
      let departments = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        departments.push(appData);
      });
      this.departments = departments;
    },
    async addDepartment() {
      if (this.name && this.location && this.phonenmbr && this.headattendant) {
        await db.collection("Afdelingen").add({
          name: this.name,
          location: this.location,
          phonenmbr: this.phonenmbr,
          headattendant: this.headattendant,
        });
        this.getDepartment();
        this.name = "";
        this.location = "";
        this.phonenmbr = "";
        this.headattendant = "";
        this.dialog = false;
        alert("Afdeling is toegevoegd");
        window.location.href = "admin-dashboard";
      } else {
        alert(
          "Naam, locatie, telefoonnummer en hoofdbegeleider zijn verplicht"
        );
      }
    },
    // Haalt begeleiders op uit firebase
    async getAttendant() {
      let snapshot = await db.collection("Begeleiders").get();
      let attendants = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        attendants.push(appData);
      });
      for (let i = 0; i < attendants.length; i++) {
        var name = attendants[i].firstname + " " + attendants[i].lastname;
        this.names.push(name);
      }
    },
    close() {
      if (confirm("Weet u zeker dat u wilt afsluiten?")) {
        this.dialog = false;
        this.name = "";
        this.location = "";
        this.phonenmbr = "";
        this.headattendant = "";
      } else {
        this.dialog = true;
      }
    },
  },
};
</script>
