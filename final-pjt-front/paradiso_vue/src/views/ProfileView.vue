<template>
  <div class="margin-by-fixed">
    <img src="../assets/logo.png" alt="profile-img" id="profile-img">
    <h1>{{ nickname }}</h1>

    <div v-if="totalData">
      팔로잉: {{ totalData.userSerializer.followings_count }} | 팔로워: {{ followercount }}
      <button @click="follow" v-if="!isfollow">팔로우</button>
      <button @click="follow" v-if="isfollow">언팔로우</button>
    </div>
    <h2>좋아하는 영화</h2>
    <ProfileLikeMovieList :likeMovieList="totaldata?.movieSerializer"/>
    <ProfileCommentList :commentList="totaldata?.commentSerializer"/>
  </div>
</template>

<script>
import ProfileLikeMovieList from '@/components/ProfileLikeMovieList'
import ProfileCommentList from '@/components/ProfileCommentList'
import axios from 'axios'


export default {
    name: 'ProfileView',
    components: {
      ProfileLikeMovieList,
      ProfileCommentList
    },
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
        this.isfollow = false
      }
  
    },
    methods: {
      follow() {
        const token = localStorage.getItem('accessToken')
        if (token) {
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/accounts/${this.totaldata.userSerializer.id}/follow/`,
            headers: {'Authorization': `Bearer ${token}`}
          })
          .then((res) => {
            this.isfollow = res.data.is_followed
            this.followercount = res.data.followers_count
          })
        } else {
          alert('로그인이 필요합니다.')
          this.$router.push({ name: 'LogInView' })
        }
   
      }
    }
}
</script>

<style>
#profile-img {
  width: 200px;
  border: solid 2px gray;
  border-radius: 50%;
}
</style>