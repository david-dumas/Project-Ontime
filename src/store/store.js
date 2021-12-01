import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        isAuthenticated = false,

    },
    getters: {

    },
    actions: {

    },
    mutations: {
        setAuthentication (state, status) {
            state.isAuthenticated = false;
        }
    }
})
