import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        isAuthenticated: false,

    },
    getters: {

    },
    actions: {

    },
    mutations: {
        setAuthentication(state, status) {
            state.isAuthenticated = status;
        }
    }
})

export default store