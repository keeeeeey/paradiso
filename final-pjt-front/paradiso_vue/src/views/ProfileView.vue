<template>
  <div class="margin-by-fixed">
    <div class="profile-data-box">
      <div class="profile-img-box">
        <img src="../assets/defaultprofileimg.jpeg" alt="profile-img" class="profile-img">        
      </div>
      <i class="fa-solid fa-camera fa-2x profile-img-update"></i>
      <div class="d-flex justify-content-center align-items-center">
        <h1>{{ nickname }}</h1>
        <div v-if="!isMypage" style="margin-left: 10px;">
          <button @click="follow" v-if="!isfollow" class="btn btn-primary">팔로우</button>
          <button @click="follow" v-if="isfollow" class="btn btn-primary">언팔로우</button>
        </div>
      </div>
      <div v-if="totalData">
        팔로잉: {{ totalData.userSerializer.followings_count }} | 팔로워: {{ followercount }}
      </div>
      <br>
    </div>    
    <ProfileLikeMovieList :likeMovieList="totaldata?.movieSerializer"/>
    <h1 class="text-center mt-5 mt-1">작성한 댓글</h1>
    <ProfileCommentList :commentList="totaldata?.commentSerializer"/>
    <h1 class="text-center mt-5 mt-1">좋아요한 댓글</h1>
    <ProfileCommentList :commentList="totaldata?.likeCommentSerializer"/>
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
        isMypage: false,
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
          this.isMypage = res.data.is_mypage
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
.profile-img-box {
  width: 25%;
  border: solid 2px gray; 
  border-radius: 50%;
  margin: 10px auto;
  aspect-ratio: 1 / 1;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.profile-img {
  width: 100%;
}

.profile-data-box {
  text-align: center;
  margin-top: 50px;
}
</style>