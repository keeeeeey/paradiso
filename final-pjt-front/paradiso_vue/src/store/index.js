import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'

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
    },

    refresh() {
      const refreshToken = localStorage.getItem("refreshToken")

      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/refresh/",
        data: {'refresh': refreshToken},
      })
        .then((res) => {
          localStorage.setItem("accessToken", res.data.access)
          this.isLoggedIn = true;
        })
        .catch(() => {
          localStorage.removeItem("accessToken")
          localStorage.removeItem("refreshToken")
          this.$router.push({ name: "LogInView" })
        })
    },
  },
  modules: {
  }
})
