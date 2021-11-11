<template>
    <div classname="adashboard">
      <AHeader />
      <h1>Admin Dashboard</h1>
      <div class="tables">
        <v-container>
        <v-row>
          <v-col>
              <DepartmentTable />
          </v-col>
          <v-col>
              <AttendantTable />
          </v-col>
          <v-col>
              <ClientTable />
          </v-col>
        </v-row>
      </v-container>
      </div>
      <Footer />
  </div>
</template>

<script>
import AHeader from '../components/AHeader.vue';
import Footer from '../components/Footer.vue';
import AttendantTable from '../components/AttendantTable.vue';
import ClientTable from '../components/ClientTable.vue';
import DepartmentTable from '../components/DepartmentTable.vue';

export default {
    name: 'Adashboard',
    components: {
      Footer,
      AHeader,
      AttendantTable,
      ClientTable,
      DepartmentTable
  }
}
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 1em;
}
v-col {
  width: 300px;
}
</style>