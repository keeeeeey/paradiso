<template>
  <div id="select-movie-view" class="margin-by-fixed">
    <h1>SelectMovieView</h1>
    <form @submit.prevent="submitFavorite" class="row">
      <div v-for="movie in movies" :key="movie.id" class="p-0 col-2">
        <!-- <input type='checkbox' :name='movie.id' :value='movie.id' />
        {{ movie.title }} -->
        <img :src="API_URL + movie.poster_path" alt="" class="mw-100" style="height: 100%" @click="selectFavoriteMovie(movie.id)">
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios"
const API_URL = "http://127.0.0.1:8000"

export default {
    name: "SelectMovieView",
    data() {
      return {
        movies: null,
        API_URL: "https://image.tmdb.org/t/p/original",
        my_favorite_movies: []
      }
    },
    methods: {
      selectFavoriteMovie(id) {
        if (this.my_favorite_movies.length === 10) {
          alert("영화는 ")
        } 
        
        this.my_favorite_movies.push(id)
        console.log(this.my_favorite_movies)
      }
    },
    created() {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
        .then((res) => {
          console.log(res.data)
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
}
</script>

<style>

</style>