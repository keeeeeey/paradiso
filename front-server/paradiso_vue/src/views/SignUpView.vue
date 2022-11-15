<template>
    <div id="sign-up-view">
      <h1>Sign Up Page</h1>
      <form @submit.prevent="signUp">
        <label for="username">username : </label>
        <input type="text" id="username" v-model="username"><br>

        <label for="email">email : </label>
        <input type="text" id="email" v-model="email"><br>
  
        <label for="password"> password : </label>
        <input type="password" id="password" v-model="password"><br>

        <label for="passwordConfirm"> password confirmation : </label>
        <input type="password" id="passwordConfirm" v-model="passwordConfirm">
        
        <input type="submit" value="SignUp">
      </form>
    </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      email: null,
      password: null,
      passwordConfirm: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const email = this.email
      const password = this.password
      const passwordConfirm = this.passwordConfirm
      
      const payload = {
        username, email, password, passwordConfirm
      }
      
      this.$store.dispatch("signUp", payload)
    }
  }
}
</script>