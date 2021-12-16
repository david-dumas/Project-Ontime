<template>
  <v-card class="mx-auto" max-width="1000">
    <v-toolbar color="#006027" dark>
      <v-toolbar-title>Cliënten</v-toolbar-title>
    </v-toolbar>

    <v-spacer></v-spacer>

    <v-data-table
      :headers="headers"
      :items="clienten"
      sort-by="lastname"
      class="elevation-1"
    >
    </v-data-table>
  </v-card>
</template>

<script>
import { db } from "@/main";

export default {
  name: "Tabeldash",
  components: {},
  data: () => ({
    dialogEdit: false,
    dialogDelete: false,
    dialogOpen: false,
    selected: [],
    headers: [
      { text: "Voornaam", value: "firstname" },
      { text: "Achternaam", value: "lastname" },
      { text: "", value: "actions", sortable: false },
    ],
    clienten: [],
    departments: [],
    names: [],
  }),
  created() {
    this.getClient();
    this.getDepartments();
  },
  methods: {
    // Haalt clienten op uit firebase
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
    // Verwijderd clienten in firebase
    async deleteClient(item) {
      await db.collection("Clienten").doc(item).delete();
      this.getClient();
      this.dialogDelete = false;
      this.dialogOpen = false;
    },
    // Update clienten in firebase
    async updateClient(item) {
      await db.collection("Clienten").doc(item.id).update({
        firstname: item.firstname,
        lastname: item.lastname,
        email: item.email,
        phonenmbr: item.phonenmbr,
        cardnmbr: item.cardnmbr,
      });
      this.getClient();
      this.dialogEdit = false;
    },
    // Opent dialog om gegevens te bewerken
    editItem() {
      this.dialogEdit = true;
    },
    // Opent dialog met client gegevens
    openItem(item) {
      this.dialogOpen = true;
      this.selected = item;
    },
    // Opent dialog met are you sure you want to delete
    deleteItem() {
      this.dialogDelete = true;
    },
    // Sluit dialog met gegevens af
    closeOpen() {
      this.dialogOpen = false;
    },
    // Sluit verwijderen confirm af
    closeDelete() {
      this.dialogDelete = false;
    },
    // Sluit de edit dialog af
    closeEdit() {
      this.dialogEdit = false;
    },
  },
};
</script>