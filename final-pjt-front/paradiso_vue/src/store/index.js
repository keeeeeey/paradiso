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
    user: null,
    isSelectView: false,
  },
  getters: {
  },
  mutations: {
    SAVE_USER(state, user_data) {
      state.user = user_data
    },

    DELETE_USER(state) {
      state.user = null
    },

    SELECT_VIEW(state, bool) {
      state.isSelectView = bool
    }
  },
  actions: {
    save_user(context, user_data) {
      context.commit("SAVE_USER", user_data)
    },

    delete_user(context) {
      context.commit("DELETE_USER")
    },

    select_view(context, bool) {
      context.commit("SELECT_VIEW", bool)
    },

    refresh(context) {
      const refreshToken = localStorage.getItem("refreshToken")
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/refresh/",
        data: {'refresh': refreshToken},
      })
        .then((res) => {
          localStorage.setItem("accessToken", res.data.access)
        })
        .catch((err) => {
          if (err.response.status === 401) {
            context.commit("DELETE_USER")
            localStorage.removeItem("accessToken")
            localStorage.removeItem("refreshToken")
            localStorage.removeItem("vuex")
            this.$router.push({ name: "LogInView" })
          }
        })
    }
  },
  modules: {
  }
})
