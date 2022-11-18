<template>
  <div>
    <img :src="imgurl + playmovie.poster_path" alt="" class="img-fluid">
    <!-- <p>좋아요 개수: {{ likecount }}</p> -->
    <!-- <button @click="likeMovie" v-show="!islike">좋아요</button>
    <button @click="likeMovie" v-show="islike">좋아요 취소</button> -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'NowPlayListItem',
    props: {
      playmovie: Object,
    },
    data() {
      return {
        likecount: this.playmovie,
        islike: false,
        imgurl: 'https://image.tmdb.org/t/p/original'
      }
    },
    methods: {
      likeMovie(event) {
        event.stopPropagation()
        const token = localStorage.getItem('accessToken')
        if (token) {
          axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/${this.playmovie.id}/likes/`,
          headers: {'Authorization': `Bearer ${token}`},
          })
          .then((res) => {
            this.islike = res.data.is_liked
            this.likecount = res.data.like_users_count
          })
          .catch(() => {
            console.log('실패')
          })
        } else {
          alert('로그인이 필요합니다')
          this.$router.push({ name: 'LogInView' })
        }
      }
    },
    created() {
      const token = localStorage.getItem('accessToken')
      if (token) {
        axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.playmovie.id}/movies/islike/`,
        headers: {'Authorization': `Bearer ${token}`},
        })
        .then((res) => {
          this.islike = res.data.is_liked
        })
      } else {
        this.islike = false
      }

    }
}
</script>

<style>

</style>