<template>
  <div>
    <h1>detail</h1>
    <p>{{ movie_id }}</p>
    <label for="comment">댓글: </label>
    <input type="text" v-model="comment">
    <button @click="inputComment">작성</button>

  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'MovieDetail',
    data() {
        return {
            movie_id: this.$route.params.movieId,
            comment: null,
        }
    },
    created() {
        axios({
            method: 'get',
            url: `http://127.0.0.1:8000/movies/${this.movie_id}`,
        })
        .then(res => {
            console.log(res)
        })
    },
    methods: {
      inputComment() {
        const token = localStorage.getItem('accessToken')
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/${this.movie_id}/comments/`,
          data: {
            content: this.comment,
            movie_id: this.movie_id,
          },
          headers: {'Authorization': `Bearer ${token}`},
        })
        .then(() => {
          console.log('댓글작성 성공')
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
}
</script>

<style>

</style>