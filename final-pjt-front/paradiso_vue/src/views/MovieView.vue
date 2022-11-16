<template>
  <div id="movie-view">
    <h1>MovieView</h1>
    <label for="comment">댓글: </label>
    <input type="text" v-model="comment">
    <button @click="inputComment">작성</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "MovieView",
    data() {
      return{
        comment: null,
        movie_id: 1,
      }
    },
    methods: {
      inputComment() {
        const token = localStorage.getItem('accessToken')
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/movies/1/comments/',
          data: {
            content: this.comment,
            movie_id: this.movie_id,
          },
          headers: {'Authorization': `Bearer ${token}`},
        })
        .then(res => {
          console.log(res)
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