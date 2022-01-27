import Vuex from 'vuex';
import Vue from 'vue';
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const store = new Vuex.Store({

   plugins: [createPersistedState({
       paths: ['isAuthenticated']
   })],

    state: {
        isAuthenticated: false,
        selected: new Array()
    },
    getters: {
        
    },
    actions: {

    },
    mutations: {
        setAuthentication(state, status) {
            state.isAuthenticated = status;
        },
        mutateSelected(state, id) {
            let index = state.selected.indexOf(id);

            if (index == -1) {
                state.selected.push(id);
                return;
            }

            state.selected.splice(index, 1);
        }
    }
})

export default store