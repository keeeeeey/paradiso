<template>
  <div id="select-movie-view" class="margin-by-fixed">
    <h1 class="my-5">좋아하는 영화를 선택해주세요.</h1>
    <form @submit.prevent="submitFavorite">
      <div class="favorit-select-btn-box">
        <input type="submit" class="btn btn-primary" value="선택완료">
      </div>
      <div class="row" style="margin: 0">
        <div v-for="movie in movies" :key="movie.id" :id="movie.id" class="select-movie-box p-0 col-2">
          <img :src="IMG_URL + movie.poster_path" alt="" :id="movie.id + 'img'" class="mw-100" style="height: 100%" @click="selectFavoriteMovie(movie.id)">
        </div>
      </div>
    </form>
    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
  </div>
</template>

<script>
import axios from "axios"
import InfiniteLoading from "vue-infinite-loading"
const API_URL = "http://127.0.0.1:8000"

export default {
    name: "SelectMovieView",
    components: {
      InfiniteLoading
    },
    data() {
      return {
        movies: [],
        my_favorite_movies: [],
        IMG_URL: "https://image.tmdb.org/t/p/original",
        startindex: 0, 
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

        if (my_favorite.length < 3) {
          alert("영화를 3개 이상 선택해주세요.")
          return
        } 

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
      },

      infiniteHandler($state) {
        console.log(this.startindex)
        axios({
          method: "get",
          url: `${API_URL}/movies/${this.startindex + 40}/${this.startindex}`,
        })
          .then(({ data }) => {
            console.log(data.length)
            if (data.length) {
              this.startindex += 40;
              this.movies.push(...data);
              $state.loaded();
            } else {
              $state.complete();
            }
          });
      },
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

.favorit-select-btn-box {
  width: 150px;
  position: fixed;
  top: 25%;
  right: 1%;
  text-align: center;
  box-sizing: border-box;
  padding: 10px;
}
</style>