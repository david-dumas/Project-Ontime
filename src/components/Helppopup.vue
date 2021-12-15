<template>
    <v-col cols="auto">
      <v-dialog
        transition="dialog-top-transition"
        max-width="80em"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="#FFFFFF"
            v-bind="attrs"
            v-on="on"
            class="helpbtn"
          >Help</v-btn>
        </template>
        <template v-slot:default="dialog">
          <v-card>
            <v-toolbar
              color="#1B5E20"
              dark
            >Help</v-toolbar>
            
      <v-container
      width="100%">
        <v-layout>

              <v-expansion-panels class="expensionpanels">
                <v-card>
                  <v-card-title>
                    Veelgestelde vragen:
                  </v-card-title>
                <v-expansion-panel>
                  <v-expansion-panel-header 
                  class="font-weight-medium">
                    Hoe kan ik mezelf of een ander aanmelden?
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                   U kunt zich het beste aanmelden door te bellen met één van de medewerkers van de Bartiméus  via nummer 088 88 99 888 (lokaal tarief)
                  </v-expansion-panel-content>
                  
                  
                </v-expansion-panel>
                <v-expansion-panel>
                  <v-expansion-panel-header 
                  class="font-weight-medium">
                    Hoe blijf ik op de hoogte van alle nieuwtjes?
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                   Nieuws kunt u dagelijks volgen via onze homepage. U kunt zich ook aanmelden voor één van de gratis nieuwsbrieven en/of u kunt ons volgen via onze officiële social media kanalen: Facebook, Twitter en YouTube.
                  </v-expansion-panel-content>
                </v-expansion-panel>
                </v-card>
              </v-expansion-panels>

        </v-layout>
      </v-container>


      <v-container> 
        <v-layout>       
          <v-flex>
            <v-card>
              <v-card-title>
                Contact gegevens:
                <v-card-text class="font-weight-medium">
                  Telefoonnummer: 088 - 88 99 888
                  <br>
                  Locatie: Boswijklaan 44 941 ZN Doorn
                </v-card-text>
              </v-card-title>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>

      
            <v-card-actions class="justify-end">
              <v-btn
                text
                color="#1B5E20"
                @click="dialog.value = false"
              >Close</v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-dialog>
    </v-col>
  </v-row>


  

</template>


<script>
export default {
    
}
</script>

<style scoped>
.expensionpanels {
  display: block;
}
.helpbtn {
  text-transform: none;
}
</style> 