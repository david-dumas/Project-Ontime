<template>
  <div>
    <h1 v-if="isLoading">
      Dit laadt
    </h1>
    <v-simple-table class="table" fixed-header height="350px" v-else>
      <template v-slot:default>
        <thead>
          <tr>
            <th>
              <div class="float-left text-h5 black--text pt-1">
                Begeleiders
              </div>
              <div class="float-right">
                <FormAddAttendant />
              </div>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in attendants"
            :key="item.firstname"
            class="black--text body-1"
          >
            <td>{{ item.firstname }} {{ item.lastname }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
import FormAddAttendant from "../components/FormAddAttendant.vue";
import { db } from "@/main";
export default {
  name: "AttendantTable",
  components: {
    FormAddAttendant,
  },
  data() {
    return {
      isLoading: true,
    };
  },
  async created() {
    this.getAttendant();
  },
  methods: {
    async getAttendant() {
      let snapshot = await db.collection("begeleiderDB").get();
      let attendants = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        attendants.push(appData);
      });
      this.attendants = attendants;
      this.isLoading = false;
    },
  },
};
</script>