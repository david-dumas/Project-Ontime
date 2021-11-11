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
import FormAddAttendant from  '../components/FormAddAttendant.vue';

  export default {
    name: 'AttendantTable',
    components: {
      FormAddAttendant,
    },
    data () {
      return {
        attendants: [
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