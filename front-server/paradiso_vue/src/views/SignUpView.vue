<template>
    <div id="sign-up-view">
      <h1>Sign Up Page</h1>
      <form @submit.prevent="signUp">
        <label for="username">username : </label>
        <input type="text" id="username" v-model="username"><br>

        <label for="email">email : </label>
        <input type="text" id="email" v-model="email"><br>
  
        <label for="nickname">nickname : </label>
        <input type="text" id="nickname" v-model="nickname"><br>

        <label for="password"> password : </label>
        <input type="password" id="password" v-model="password"><br>

        <label for="passwordConfirm"> password confirmation : </label>
        <input type="password" id="passwordConfirm" v-model="passwordConfirm">
        
        <input type="submit" value="SignUp">
      </form>
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      email: null,
      nickname: null,
      password: null,
      passwordConfirm: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const email = this.email
      const nickname = this.nickname
      const password = this.password
      const passwordConfirm = this.passwordConfirm
      
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, email, nickname, password, passwordConfirm
        }
      })
        .then(() => {
          this.$router.push({ name: "LogInView" })
        })
        .catch((err) => console.log(err))
    }
  }
}
</script>