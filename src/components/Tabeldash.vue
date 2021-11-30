<template>

  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            Name
          </th>
          <th class="text-left">
            Calories
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in client"
          :key="item.firstname"
        >
          <td>{{ item.firstname }}</td>
          <td>{{ item.lastname }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>

  
</template>

<script>
import { db } from "@/main";
export default {
  name: "Tabeldash",
  components: {
  },
  data() {
    return {
    };
  },
async created() {
    this.getClients();
  },
  methods: {
    async getClients() {
      let snapshot = await db.collection("cliëntenDB").get();
      let client = [];
      snapshot.forEach((doc) => {
        let appData = doc.data();
        appData.id = doc.id;
        client.push(appData);
      });
      this.client = client;
      this.isLoading = false;
      console.log(client)
    },
  },
};
</script>

