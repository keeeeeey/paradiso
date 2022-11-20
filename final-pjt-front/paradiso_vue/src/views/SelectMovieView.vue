<template>
  <div id="select-movie-view" class="margin-by-fixed">
    <h1>SelectMovieView</h1>
    <form @submit.prevent="submitFavorite">
      <input type="submit" class="btn btn-primary" value="선택완료">
      <div class="row">
        <div v-for="movie in movies" :key="movie.id" :id="movie.id" class="select-movie-box p-0 col-2">
          <img :src="IMG_URL + movie.poster_path" alt="" :id="movie.id + 'img'" class="mw-100" style="height: 100%" @click="selectFavoriteMovie(movie.id)">
        </div>
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
        my_favorite_movies: [],
        IMG_URL: "https://image.tmdb.org/t/p/original",
      }
    },
    methods: {
      selectFavoriteMovie(id) {
        if (this.my_favorite_movies.length === 10) {
          alert("영화 선택은 10개 까지만 가능합니다.")
          return false
        }

        const selectedMovie = document.getElementById(id)
        const selectedMovieImg = document.getElementById(id + "img")
        
        if (selectedMovie.className.includes("checked-box")) {
          selectedMovie.classList.remove("checked-box")
          selectedMovieImg.classList.remove("checked")
        } else {
          selectedMovie.classList.add("checked-box")
          selectedMovieImg.classList.add("checked")
        }

        if (this.my_favorite_movies.includes(id)) {
          const idx = this.my_favorite_movies.indexOf(id)
          this.my_favorite_movies.splice(idx, 1)
          console.log(this.my_favorite_movies)
        } else {
          this.my_favorite_movies.push(id)
          console.log(this.my_favorite_movies)
        }

      },

      submitFavorite() {
        const my_favorite = this.my_favorite_movies
        const token = localStorage.getItem('accessToken')

        axios({
          method: "post",
          url: `${API_URL}/accounts/addfavoritemovies/`,
          headers: {'Authorization': `Bearer ${token}`},
          data: { my_favorite },
        })
          .then(() => {
            console.log("성공")
            this.$router.push({ name: "MovieView" })
          })
          .catch((err) => {
            console.log(err)
          })
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
.checked-box {
    box-shadow: 0 0 .2rem #fff, 0 0 .2rem #fff, 0 0 2rem #1f87c3, 0 0 2rem #1f87c3, 0 0 2rem #1f87c3;
    z-index: 1;
}

.checked {
  scale: 1.1;
}

.select-movie-box {
  overflow: hidden;
  border-radius: 10px;
}

.select-movie-box img {
  transition: all 0.2s linear;
}
</style>