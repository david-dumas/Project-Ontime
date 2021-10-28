
<template>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            Name
          </th>
          <th class="text-left">
            Time
          </th>
          <th class="text-left">
            Date
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in afspraken"
          :key="item.name"
        >
          <td>{{ item.name }}</td>
          <td>{{ item.time }}</td>
          <td>{{ item.date }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
  export default {
    data () {
      return {
        afspraken: [
          {
            name: 'Dokter',
            time: '13.30pm-14.00pm',
            date: '27-10-2021'
          },
          {
            name: 'Boodschappen',
            time: '16.30pm-18.00pm',
            date: '28-10-2021'
          },
          {
            name: 'Fysio',
            time: '10.00am-20.00pm',
            date: '29-10-2021'
          },
          {
            name: 'Opstaan',
            time: '9.10am-10.00am',
            date: '29-10-2021'
          },
        ],
      }
    },
  }
</script>

