<template>
    <div id="sign-up-view" class="margin-by-fixed w-25 m-auto">
      <h1 class="mt-5">회원가입</h1>
      <form @submit.prevent="signUp">
        <div class="mb-3">
          <label for="username" class="form-label">아이디</label>
          <input type="text" class="form-control" id="username" aria-describedby="emailHelp" v-model.trim="username" @blur="idCheck">
          <div id="idMessage" class="form-text"></div>
        </div>

        <div class="mb-3">
          <label for="email" class="form-label">이메일</label>
          <input type="email" class="form-control" id="email" v-model="email">
        </div>

        <div class="mb-3">
          <label for="nickname" class="form-label">닉네임</label>
          <input type="text" class="form-control" id="nickname" v-model="nickname">
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">비밀번호</label>
          <input type="password" class="form-control" id="password" v-model="password">
        </div>

        <div class="mb-3">
          <label for="passwordConfirm" class="form-label">비밀번호 확인</label>
          <input type="password" class="form-control" id="passwordConfirm" v-model="passwordConfirm">
        </div>
        <!-- <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div> -->
        <button type="submit" class="btn btn-primary">회원가입</button>
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
    },

    idCheck() {
      const username = this.username

      const message = document.querySelector("#idMessage")
      if (!username) {
        message.innerText = "아이디를 입력해주세요."
        message.style.color = "red"
        return
      }

      axios({
        method: "get",
        url: `${API_URL}/accounts/idcheck/${username}`,
      })
        .then((res) => {
          if (res.data.id_exist) {
            message.innerText = "이미 존재하는 아이디입니다."
            message.style.color = "red"
          } else {
            message.innerText = "사용 가능한 아이디입니다."
            message.style.color = "green"
          }
        })
    }
  }
}
</script>