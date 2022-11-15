import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
// import createPersistedState from 'vuex-persistedstate'

const API_URL = "http://127.0.0.1:8000"

Vue.use(Vuex)

export default new Vuex.Store({
  // plugins: [
  //   createPersistedState(),
  // ],
  state: {
    accessToken: null
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    SAVE_TOKEN(state, accessToken) {
      localStorage.setItem("accessToken", accessToken)
      router.push({ name: "MovieView" })
    },
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const email = payload.email
      const password = payload.password
      const passwordConfirm = payload.passwordConfirm

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, email, password, passwordConfirm
        }
      })
        .then(() => {
          router.push({ name: "LogInView" })
        })
        .catch((err) => console.log(err))
    },

    logIn(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: "post",
        url: `${API_URL}/api/token/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.access)
        })
        .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
