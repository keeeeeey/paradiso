<template>
    <div id="sign-up-view" class="margin-by-fixed w-25 m-auto">
      <h1 class="mt-5">회원가입</h1>
      <form @submit.prevent="signUp">
        <div class="mb-3">
          <label for="username" class="form-label">아이디</label>
          <input type="text" class="form-control" id="username" v-model.trim="username" @keyup.enter="idCheck" @blur="idCheck">
          <div id="idMessage" class="form-text"></div>
        </div>

        <div class="mb-3">
          <label for="email" class="form-label">이메일</label>
          <input type="email" class="form-control" id="email" v-model.trim="email" @keyup.enter="emailCheck" @blur="emailCheck">
          <div id="emailMessage" class="form-text"></div>
        </div>

        <div class="mb-3">
          <label for="nickname" class="form-label">닉네임</label>
          <input type="text" class="form-control" id="nickname" v-model.trim="nickname" @keyup.enter="nicknameCheck" @blur="nicknameCheck">
          <div id="nicknameMessage" class="form-text"></div>
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">비밀번호</label>
          <input type="password" class="form-control" id="password" v-model="password" @keyup.enter="passwordCheck" @blur="passwordCheck">
          <div id="passwordMessage" class="form-text"></div>
        </div>

        <div class="mb-3">
          <label for="passwordConfirm" class="form-label">비밀번호 확인</label>
          <input type="password" class="form-control" id="passwordConfirm" v-model="passwordConfirm">
        </div>
        <!-- <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div> -->
        <button type="submit" class="btn btn-primary" @click="signUp">회원가입</button>
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
      id_boolean: false,
      email_boolean: false,
      nickname_boolean: false,
      password_boolean: false,
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

    idCheck(event) {
      event.stopPropagation()
      const username = this.username

      const message = document.querySelector("#idMessage")
      if (!username) {
        message.innerText = "아이디를 입력해주세요."
        message.style.color = "red"
        this.id_boolean = false
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
            this.id_boolean = false
          } else {
            message.innerText = "사용 가능한 아이디입니다."
            message.style.color = "green"
            this.id_boolean = true
          }
        })

      document.querySelector("#email").focus()
    },

    emailCheck() {
      const email = this.email

      const message = document.querySelector("#emailMessage")
      if (!email) {
        message.innerText = "이메일를 입력해주세요."
        message.style.color = "red"
        this.email_boolean = false
        return
      }

      axios({
        method: "get",
        url: `${API_URL}/accounts/emailcheck/${email}`,
      })
        .then((res) => {
          if (res.data.email_exist) {
            message.innerText = "이미 존재하는 이메일입니다."
            message.style.color = "red"
            this.email_boolean = false
          } else {
            message.innerText = "사용 가능한 이메일입니다."
            message.style.color = "green"
            this.email_boolean = true
          }
        })

      document.querySelector("#nickname").focus()
    },

    nicknameCheck() {
      const nickname = this.nickname

      const message = document.querySelector("#nicknameMessage")
      if (!nickname) {
        message.innerText = "닉네임을 입력해주세요."
        message.style.color = "red"
        this.nickname_boolean = false
        return
      }

      axios({
        method: "get",
        url: `${API_URL}/accounts/nicknamecheck/${nickname}`,
      })
        .then((res) => {
          if (res.data.nickname_exist) {
            message.innerText = "이미 존재하는 닉네임입니다."
            message.style.color = "red"
            this.nickname_boolean = false
          } else {
            message.innerText = "사용 가능한 닉네임입니다."
            message.style.color = "green"
            this.nickname_boolean = true
          }
        })

        document.querySelector("#password").focus()
    },

    passwordCheck() {
      const password = this.password

      let number = password.search(/[0-9]/g);
      let english = password.search(/[a-z]/ig);
      let spece = password.search(/[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/gi);

      const message = document.querySelector("#passwordMessage")
      if (!password) {
        message.innerText = "비밀번호를 입력해주세요."
        message.style.color = "red"
        this.password_boolean = false
        return
      }

      if (number < 0 || english < 0 || spece < 0) {
        message.innerText = "사용 가능한 비밀번호가 아닙니다."
        message.style.color = "red"
        this.password_boolean = false
      } else {
        message.innerText = "사용 가능한 비밀번호 입니다."
        message.style.color = "green"
        this.password_boolean = true
      }

      document.querySelector("#passwordConfirm").focus()
    }

  }
}
</script>