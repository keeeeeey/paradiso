<template>
  <div>
    <h1>Profile 입니다.</h1>
    {{ nickname }}
    {{ totaldata.serializer.isFollowd }}
    팔로우: {{ totaldata }}
    <button @click="follow" v-show="!isfollow">팔로우</button>
    <button @click="follow" v-show="isfollow">언팔로우</button>
  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'ProfileView',
    data() {
      return {
        nickname: String(this.$route.params.nickname),
        totaldata: null,
        isfollow: false,
      }
    },
    created() {
      const token = localStorage.getItem('accessToken')
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.nickname}/`,
      })
      .then(res => {
        console.log(res.data)
        this.totaldata = res.data
      })
      if (token) {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/${this.nickname}/isfollow/`,
          headers: {'Authorization': `Bearer ${token}`},
        })
        .then(res => {
          this.isfollow = res.data.is_followed
        })
      } else {
        this.isfollow = true
      }
  
    },
    methods: {
      follow() {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/accounts/${this.totaldata}/follow/`
        })
        .then(() => {
          
        })
      }
    }
}
</script>

<style>

</style>