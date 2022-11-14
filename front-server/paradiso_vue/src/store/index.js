import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

const API_URL = "http://127.0.0.1:8000"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: null
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: "ArticleView" })
    },
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key)
        })
        .catch((err) => console.log(err))
    },

    logIn(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key)
        })
        .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
