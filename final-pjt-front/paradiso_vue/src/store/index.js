import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    user: null
  },
  getters: {
  },
  mutations: {
    SAVE_USER(state, user_data) {
      state.user = user_data
    },

    DELETE_USER(state) {
      state.user = null
    }
  },
  actions: {
    save_user(context, user_data) {
      context.commit("SAVE_USER", user_data)
    },

    delete_user(context) {
      context.commit("DELETE_USER")
    }
  },
  modules: {
  }
})
