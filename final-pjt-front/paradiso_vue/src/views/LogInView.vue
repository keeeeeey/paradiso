<template>
    <div id="login-view" class="margin-by-fixed m-auto" style="width: 370px;">
      <h1 style="margin-top: 200px">로그인</h1>
      <form @submit.prevent="logIn">
        <div class="mb-3">
          <label for="username" class="form-label">아이디</label>
          <input type="text" class="form-control" id="username" v-model="username">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">비밀번호</label>
          <input type="password" class="form-control" id="password" v-model="password">
        </div>
        <button type="submit" class="btn btn-primary">로그인</button>
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

      if (!username) {
        alert("아이디를 입력해주세요.")
        return
      } else if (!password) {
        alert("비밀번호를 입력해주세요.")
        return
      }

      axios({
        method: "post",
        url: `${API_URL}/api/token/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          this.$store.dispatch("save_user", res.data)
          localStorage.setItem("accessToken", res.data.access)
          localStorage.setItem("refreshToken", res.data.refresh)
          this.$emit("Login")

          if (res.data.isFirst) {
            this.$router.push({ name: "SelectMovieView" })
          } else {
            this.$router.push({ name: "MovieView" })
          }
        })
        .catch((err) => {
          console.log(err)
          alert("아이디나 비밀번호가 일치하지 않습니다.")
        })
    }
  }
}
</script>