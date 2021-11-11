<template>
  <v-simple-table 
    class="table"
    fixed-header
    height="500px"
  >
    <template v-slot:default>
      <thead>
        <tr>
          <th>
            <div class="float-left text-h5 black--text pt-1">
              Cliënten
            </div>
            <div class="float-right">
              <FormAddClient />
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in clienten"
          :key="item.name"
          class="black--text body-1"
        >
          <td>{{ item.name }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
import FormAddClient from '../components/FormAddClient.vue'
  export default {
    name: 'ClientTable',
    components: {
      FormAddClient,
    },
    data () {
      return {
        clienten: [
          {
            name: 'David',
          },
          {
            name: 'Casper',
          },
          {
            name: 'Rianne',
          },
          {
            name: 'Hanne',
          },
          {
            name: 'David',
          },
          {
            name: 'Casper',
          },
          {
            name: 'Rianne',
          },
          {
            name: 'Hanne',
          },
          {
            name: 'David',
          },
          {
            name: 'Casper',
          },
          {
            name: 'Rianne',
          },
          {
            name: 'Hanne',
          },
        ],
      }
    },
  }
</script>