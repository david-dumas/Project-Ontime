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
              Afdelingen
            </div>
            <div class="float-right">
              <FormAddDepartment />
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in departments"
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
import FormAddDepartment from '../components/FormAddDepartment.vue'
  export default {
    name: 'DepartmentTable',
    components: {
      FormAddDepartment,
    },
    data () {
      return {
        departments: [
          {
            name: 'Slechtziend',
          },
          {
            name: 'Blind',
          },
          {
            name: 'Kokerzicht',
          },
          {
            name: 'Jongeren onder 18',
          },
          {
            name: 'Meerdere beperkingen',
          },
        ],
      }
    },
  }
</script>