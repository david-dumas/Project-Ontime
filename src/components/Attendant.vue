<template>
  <v-data-table
    :headers="headers"
    :items="attendants"
    sort-by="lastname"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Begeleiders</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <FormAddAttendant />
        <!-- Dialog voor confirm delete -->
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5"
              >Weet u zeker dat u dit wilt verwijderen?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn
                color="blue darken-1"
                text
                @click="deleteAttendant(selected.id)"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!-- Dialog met begeleider gegevens -->
        <v-dialog v-model="dialogOpen" max-width="500px">
          <v-card>
            <v-icon
              class="mr-2 black--text float-right m-2 p-2"
              @click="closeOpen"
            >
              mdi-close
            </v-icon>
            <v-card-title class="text-h5">Begeleider gegevens </v-card-title>

            <v-card-text class="black--text text-body1">
              <v-col cols="12">
                <v-row>
                  {{ selected.firstname }} {{ selected.lastname }}
                </v-row>
                <v-row>
                  {{ selected.email }}
                </v-row>
                <v-row>
                  {{ selected.phonenmbr }}
                </v-row>
              </v-col>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-icon class="mr-2" @click="editItem(selected)">
                mdi-pencil
              </v-icon>
              <v-icon class="mr-2" @click="deleteItem()">
                mdi-delete
              </v-icon>

              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!-- Dialog om begeleider te wijzigen -->
        <v-dialog v-model="dialogEdit" max-width="500px">
          <v-card>
            <v-card-title>
              <span class="text-h5">Begeleider Wijzigen</span>
            </v-card-title>
            <v-card-text>
              <v-form>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        label="Voornaam*"
                        v-model="selected.firstname"
                        prepend-icon="mdi-account"
                        required
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        label="Achternaam*"
                        v-model="selected.lastname"
                        required
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        label="Email*"
                        v-model="selected.email"
                        prepend-icon="mdi-email"
                        required
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        label="Telefoonnummer*"
                        v-model="selected.phonenmbr"
                        prepend-icon="mdi-phone"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        label="Password*"
                        type="password"
                        v-model="selected.password"
                        prepend-icon="mdi-lock"
                        required
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
                <small>*indicates required field</small>
                <v-btn color="red" text left class="left" @click="closeEdit">
                  <v-icon>mdi-delete</v-icon>
                  Close
                </v-btn>
                <v-btn
                  color="green"
                  text
                  right
                  class="left"
                  @click="updateAttendant(selected)"
                >
                  <v-icon>mdi-content-save</v-icon>
                  Opslaan
                </v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <!-- Acties -->
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon class="mr-2" @click="openItem(item)">
        mdi-account-details
      </v-icon>
    </template>
    <!-- Geen data -->
    <template v-slot:no-data>
      <p>Please Wait</p>
    </template>
  </v-data-table>
</template>

<script>
import { db } from "@/main";
import FormAddAttendant from "./FormAddAttendant.vue";
export default {
  components: {
    FormAddAttendant,
  },
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
    attendants: [],
  }),
  created() {
    this.getAttendant();
  },
  methods: {
    // Haalt begeleiders op uit firebase
    async getAttendant() {
      let snapshot = await db.collection("Begeleiders").get();
      let attendants = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        attendants.push(appData);
      });
      this.attendants = attendants;
      this.isLoading = false;
    },
    // Verwijderd begeleiders in firebase
    async deleteAttendant(item) {
      await db
        .collection("Begeleiders")
        .doc(item)
        .delete();
      this.getAttendant();
      this.dialogDelete = false;
      this.dialogOpen = false;
    },
    // Update begeleiders in firebase
    async updateAttendant(item) {
      await db
        .collection("Begeleiders")
        .doc(item.id)
        .update({
          firstname: item.firstname,
          lastname: item.lastname,
          email: item.email,
          phonenmbr: item.phonenmbr,
          password: item.password,
        });
      this.getAttendant();
      this.dialogEdit = false;
    },
    // Opent dialog om gegevens te bewerken
    editItem() {
      this.dialogEdit = true;
    },
    // Opent dialog met begeleider gegevens
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