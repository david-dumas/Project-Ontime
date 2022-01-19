<template>
  <v-data-table
    :headers="headers"
    :items="departments"
    sort-by="lastname"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Afdelingen</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <FormAddDepartment />
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
                @click="deleteDepartment(selected.id)"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!-- Dialog met afdeling gegevens -->
        <v-dialog v-model="dialogOpen" max-width="500px">
          <v-card>
            <v-icon
              class="mr-2 black--text float-right m-2 p-2"
              @click="closeOpen"
            >
              mdi-close
            </v-icon>
            <v-card-title class="text-h5">Afdeling gegevens </v-card-title>

            <v-card-text class="black--text text-body1">
              <v-col cols="12">
                <v-row>
                  {{ selected.name }}
                </v-row>
                <v-row>
                  {{ selected.location }}
                </v-row>
                <v-row>
                  {{ selected.phonenmbr }}
                </v-row>
                <v-row>
                  {{ selected.headattendant }}
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
        <!-- Dialog om afdeling te wijzigen -->
        <v-dialog v-model="dialogEdit" max-width="500px">
          <v-card>
            <v-card-title>
              <span class="text-h5">Afdeling Wijzigen</span>
            </v-card-title>
            <v-card-text>
              <v-form>
                <v-container>
                  <v-row>
                    <v-col cols="12">
                      <v-text-field
                        label="Afdelingnaam*"
                        v-model="selected.name"
                        prepend-icon="mdi-office-building"
                        required
                      ></v-text-field>
                    </v-col>

                    <v-col cols="12">
                      <v-text-field
                        label="Locatie*"
                        v-model="selected.location"
                        prepend-icon="mdi-map-marker"
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
                      <v-select
                        prepend-icon="mdi-account"
                        :items="names"
                        label="Hoofdbegeleider*"
                        v-model="selected.headattendant"
                      ></v-select>
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
                  @click="updateDepartment(selected)"
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
        mdi-menu
      </v-icon>
    </template>
    <!-- Geen data -->
    <template v-slot:no-data>
      <p>No data</p>
    </template>
  </v-data-table>
</template>

<script>
import { db } from "@/main";
import FormAddDepartment from "./FormAddDepartment.vue";
export default {
  components: {
    FormAddDepartment,
  },
  data: () => ({
    dialogEdit: false,
    dialogDelete: false,
    dialogOpen: false,
    selected: [],
    headers: [
      { text: "Naam", value: "name" },
      { text: "", value: "actions", sortable: false },
    ],
    departments: [],
    attendants: [],
    names: [],
  }),
  created() {
    this.getDepartments();
    this.getAttendants();
  },
  methods: {
    // Haalt afdelingen op uit firebase
    async getDepartments() {
      let snapshot = await db.collection("Afdelingen").get();
      let departments = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        departments.push(appData);
      });
      this.departments = departments;
    },
    // Haalt begeleiders op uit firebase
    async getAttendants() {
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
    // Verwijderd afdelingen in firebase
    async deleteDepartments(item) {
      await db
        .collection("Afdelingen")
        .doc(item)
        .delete();
      this.getDepartments();
      this.dialogDelete = false;
      this.dialogOpen = false;
    },
    // Update afdeling in firebase
    async updateDepartments(item) {
      await db
        .collection("Afdelingen")
        .doc(item.id)
        .update({
          name: item.name,
          location: item.location,
          phonenmbr: item.phonenmbr,
          headattendant: item.headattendant,
        });
      this.getDepartments();
      this.dialogEdit = false;
    },
    // Opent dialog om gegevens te bewerken
    editItem() {
      this.dialogEdit = true;
    },
    // Opent dialog met afdeling gegevens
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
