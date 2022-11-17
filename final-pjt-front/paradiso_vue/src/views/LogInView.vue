<template>
    <div id="login-view">
      <h1>LogIn Page</h1>
      <form @submit.prevent="logIn">
        <label for="username">username : </label>
        <input type="text" id="username" v-model="username"><br>
  
        <label for="password"> password : </label>
        <input type="password" id="password" v-model="password"><br>
  
        <input type="submit" value="logIn">
      </form>
    </div>
</template>
  
<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      axios({
        method: "post",
        url: `${API_URL}/api/token/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          console.log(res)
          localStorage.setItem("accessToken", res.data.access)
          if (res.data.isFirst) {
            this.$router.push({ name: "SelectMovieView" })
          } else {
            this.$router.push({ name: "MovieView" })
          }
        })
        .catch((err) => console.log(err))
    }
  }
}
</script>