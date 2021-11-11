<template>
    <v-container>
  <v-card
    class="mx-auto"
    max-width="500"
  >

    <v-toolbar
      color="#006027"
      dark
    >
    <v-toolbar-title>Clienten</v-toolbar-title>

    </v-toolbar>

    <v-container fluid>

        <v-simple-table>
            <template v-slot:default>
            <thead>
                <tr>
                <th class="text-left">
                    Naam
                </th>
                <th class="text-left">
                    Afdeling
                </th>
                </tr>
            </thead>
            <tbody>
                <tr
                v-for="item in desserts"
                :key="item.name"
                >
                <td>{{ item.name }}</td>
                <td>{{ item.calories }}</td>
                </tr>
            </tbody>
            </template>
        </v-simple-table>
      
    </v-container>
  </v-card>

    </v-container>
</template>

<script>
export default {
    data () {
      return {
        desserts: [
          {
            name: 'Henk de Vries',
            calories: 'A',
          },
          {
            name: 'Adriana van Volhoven',
            calories: 'C',
          },
          {
            name: 'Emma van Vught',
            calories: 'D',
          },
          {
            name: 'Daan Berghuis',
            calories: 'B',
          },
          {
            name: 'Freek Someren',
            calories: 'D',
          },
          {
            name: 'Karen de boer',
            calories: 'C',
          },
          {
            name: 'Hidde de Lange',
            calories: 'A',
          },
          {
            name: 'Harmen Pastoor',
            calories: 'A',
          },
          {
            name: 'Sanne Kok',
            calories: 'B',
          },
          {
            name: 'Loraine Voskuilen',
            calories: 'C',
          },
        ],
      }
    },
  }
</script>