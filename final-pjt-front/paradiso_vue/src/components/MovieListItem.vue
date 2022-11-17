<template>
  <div>
    <p>제목: {{ movie.title }}</p>
    <p>ID: {{ movie.id }}</p>
    <p>좋아요 개수: {{ likecount }}</p>
    <button @click="likeMovie" v-show="!islike">좋아요</button>
    <button @click="likeMovie" v-show="islike">좋아요 취소</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MovieListItem',
    props: {
      movie: Object,
    },
    data() {
      return {
        likecount: this.movie.like_users_count,
        islike: false
      }
    },
    methods: {
      likeMovie(event) {
        event.stopPropagation()
        const token = localStorage.getItem('accessToken')
        if (token) {
          axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/${this.movie.id}/likes/`,
          headers: {'Authorization': `Bearer ${token}`},
          })
          .then((res) => {
            console.log(this.movie)
            if (res.data.is_liked) {
              this.likecount += 1
            } else {
              this.likecount -= 1
            }
            this.islike = res.data.is_liked
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
        url: `http://127.0.0.1:8000/accounts/${this.movie.id}/islike/`,
        headers: {'Authorization': `Bearer ${token}`},
        })
        .then((res) => {
          this.islike = res.data
        })
      } else {
        this.islike = false
      }
   
    }
}
</script>

<style>

</style>