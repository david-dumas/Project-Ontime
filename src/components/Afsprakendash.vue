<template>
    <v-container>
        <v-card
            class="mx-auto"
            max-width="1000"
        >
            <v-toolbar
      color="#006027"
      dark
    >
    <v-toolbar-title>Afspraken</v-toolbar-title>

    </v-toolbar>

            <v-container fluid>
            <v-row dense>
                
                <v-card>

                    <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar
          flat
        > 
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="prev"
          >
            <v-icon small>
              mdi-chevron-left
            </v-icon>
          </v-btn>
          <v-btn
            fab
            text
            small
            color="grey darken-2"
            @click="next"
          >
            <v-icon small>
              mdi-chevron-right
            </v-icon>
          </v-btn>
          <v-toolbar-title v-if="$refs.calendar">
            {{ $refs.calendar.title }}
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-menu
            bottom
            right
          >
            
          </v-menu>
        </v-toolbar>
      </v-sheet>

      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="#018245"
          :events="events"
          :event-color="getEventColor"
          :type="type"
          @click:event="showEvent"
          @click:more="viewDay"
          @click:date="viewDay"
          @change="updateRange"
        ></v-calendar>
        
        <!-- AFSPRAAK DETAILS  -->
        
        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card
            color="grey lighten-4"
            min-width="350px"
            flat
          >
            <v-toolbar
              :color="selectedEvent.color"
              dark
            >
              <v-btn @click="deleteEvent(selectedEvent.id)" icon>
                <v-icon>mdi-delete</v-icon>
              </v-btn>
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>

            <v-card-text>
              <form v-if="currentlyEditting !== selectedEvent.id">
                {{selectedEvent.details}}
              </form>

              <form v-else>
                <textarea-autosize
                v-model="selectedEvent.details"
                type="text"
                style="width= 100%"
                :min-height="100"
                placeholder="add note"
                > </textarea-autosize>
              </form>

            </v-card-text>
            <v-card-actions>

              <v-btn text color="secondary" @click="selectedOpen = false">Annuleren</v-btn>

              <v-btn text v-if="currentlyEditting !== selectedEvent.id" 
              @click.prevent="editEvent(selectedEvent)">Edit</v-btn>

              <v-btn text v-else @click.prevent="updateEvent(selectedEvent)">Opslaan</v-btn>

            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
    </v-col>
  </v-row>
                    
                </v-card>
            </v-row>
            </v-container>
        </v-card>
    </v-container>
</template>

<script>
import { db } from '@/main';

  export default {
    data: () => ({
      today: new Date().toISOString().substr(0, 10),
      focus: new Date().toISOString().substr(0, 10),
      type: "day",
      typeToLabel: {
        day: "Day",
      },
      name: null,
      details: null,
      start: null,
      end: null,
      color: "#1976D2",
      currentlyEditting: null,
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      events: [],
      dialog: false,

    }),
    
    mounted() {
      this.getEvents();
    },

    /* ----------- AFSPRAKEN OPHALEN -----------*/

    methods: {
      async getEvents(){
        let snapshot = await db.collection("calEvent").get();
        let events = [];
        snapshot.forEach(doc => {
          let appData = doc.data();
          appData.id = doc.id;
          events.push(appData);
        });
        this.events = events;
      },
      
      viewDay ({ date }) {
        this.focus = date
        this.type = 'day'
      },
      setToday () {
        this.focus = ''
      },
      prev () {
        this.$refs.calendar.prev()
      },
      next () {
        this.$refs.calendar.next()
      },
      editEvent(ev){
        this.currentlyEditting = ev.id;
      },
      showEvent ({ nativeEvent, event }) {
        const open = () => {
          this.selectedEvent = event
          this.selectedElement = nativeEvent.target
          requestAnimationFrame(() => requestAnimationFrame(() => this.selectedOpen = true))
        }

        if (this.selectedOpen) {
          this.selectedOpen = false
          requestAnimationFrame(() => requestAnimationFrame(() => open()))
        } else {
          open()
        }

        nativeEvent.stopPropagation()
      },
      updateRange ({ start, end }) {
        const events = []

        const min = new Date(`${start.date}T00:00:00`)
        const max = new Date(`${end.date}T23:59:59`)
        const days = (max.getTime() - min.getTime()) / 86400000
        const eventCount = this.rnd(days, days + 20)

        for (let i = 0; i < eventCount; i++) {
          const allDay = this.rnd(0, 3) === 0
          const firstTimestamp = this.rnd(min.getTime(), max.getTime())
          const first = new Date(firstTimestamp - (firstTimestamp % 900000))
          const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
          const second = new Date(first.getTime() + secondTimestamp)

          events.push({
            name: this.names[this.rnd(0, this.names.length - 1)],
            start: first,
            end: second,
            color: this.colors[this.rnd(0, this.colors.length - 1)],
            timed: !allDay,
          })
        }

        this.events = events
      },
      rnd (a, b) {
        return Math.floor((b - a + 1) * Math.random()) + a
      },
    }
  };

</script>