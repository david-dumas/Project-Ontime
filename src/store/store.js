import Vuex from 'vuex';
import Vue from 'vue';
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const store = new Vuex.Store({

    plugins: [createPersistedState()],

    state: {
        isAuthenticated: false,
        isSelected: false,
    },
    getters: {

    },
    actions: {

    },
    mutations: {
        setAuthentication(state, status) {
            state.isAuthenticated = status;
        },
        setSelection(state, status) {
            state.isSelected = status;
        },
    }
})

export default store