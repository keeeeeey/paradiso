<template>
  <div id="select-movie-view" class="margin-by-fixed">
    <h1>SelectMovieView</h1>
    <form @submit.prevent="submitFavorite">
      <input type="text" class="btn btn-primary" value="선택완료">
      <div class="row">
        <SelectMovieItem v-for="movie in movies" :key="movie.id" :movie=movie class="p-0 col-2" @from-select-movie-item=fromSelectMovieItem />
      </div>
    </form>
  </div>
</template>

<script>
import SelectMovieItem from "@/components/SelectMovieItem"
import axios from "axios"
const API_URL = "http://127.0.0.1:8000"

export default {
    name: "SelectMovieView",
    components: {
      SelectMovieItem
    },
    data() {
      return {
        movies: null,
        my_favorite_movies: []
      }
    },
    methods: {
      fromSelectMovieItem(id) {
        if (this.my_favorite_movies.length === 10) {
          alert("영화 선택은 10개 까지만 가능합니다.")
        }

        if (this.my_favorite_movies.includes(id)) {
          const idx = this.my_favorite_movies.indexOf(id)
          this.my_favorite_movies.splice(idx, 1)
          console.log(this.my_favorite_movies)
        } else {
          this.my_favorite_movies.push(id)
          console.log(this.my_favorite_movies)
        }

        
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