<template>
  <div>
    <h1>Profile 입니다.</h1>
    {{ nickname }}
    <div v-if="totalData">
      팔로잉: {{ totalData.userSerializer.followings_count }} | 팔로워: {{ followercount }}
    </div>
    <button @click="follow" v-if="!isfollow">팔로우</button>
    <button @click="follow" v-if="isfollow">언팔로우</button>
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
        followrcount: null,
      }
    },
    computed: {
      totalData() {
        return this.totaldata
      },
    },
    created() {
      const token = localStorage.getItem('accessToken')
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.nickname}/`,
      })
      .then(res => {
        console.log(res)
        this.totaldata = res.data.serializer
        this.followercount = res.data.serializer.userSerializer.followers_count
      })
      if (token) {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/${this.nickname}/isfollow/`,
          headers: {'Authorization': `Bearer ${token}`}
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
        const token = localStorage.getItem('accessToken')
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/accounts/${this.totaldata.userSerializer.id}/follow/`,
          headers: {'Authorization': `Bearer ${token}`}
        })
        .then((res) => {
          this.isfollow = res.data.is_followed
          this.followercount = res.data.followers_count
        })
      }
    }
}
</script>

<style>

</style>