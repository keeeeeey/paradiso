<template>
  <div>
    <p>제목: {{ movie.title }}</p>
    <p>ID: {{ movie.id }}</p>
    <button @click="likeMovie">좋아요</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MovieListItem',
    props: {
      movie: Object,
    },
    methods: {
      likeMovie(event) {
        event.stopPropagation()
        const token = localStorage.getItem('accessToken')
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/${this.movie.id}/likes/`,
          headers: {'Authorization': `Bearer ${token}`},
        })
        .then(() => {
          console.log('좋아요 성공');
        })
        .catch(() => {
          console.log('실패')
        })
      }
    }
}
</script>

<style>

</style>