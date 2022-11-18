<template>
  <div class="margin-by-fixed">
    <h1>상영 예정 영화</h1>
    <div class="d-flex poster-container">
      <div v-for="upcomingmovie in upcominglist" :key="upcomingmovie.id" class="col-3 take-movies">
        <UpcomingMovieListItem :upcomingmovie="upcomingmovie" @click.native="goToMovie(upcomingmovie.id)"/>
      </div>
    </div>
  </div>
</template>

<script>
import UpcomingMovieListItem from '@/components/UpcomingMovieListItem'
import axios from 'axios'


export default {
    name: 'UpcomingMovieList',
    components: {
      UpcomingMovieListItem,
    },
    data() {
      return {
        upcominglist: null,
      }
    },
    created() {
        axios({
            method: "get",
            url: "https://api.themoviedb.org/3/movie/upcoming?api_key=9adec2ecce07845598e041a9836861b2&language=en-US&page=1"
        })
          .then((res) => {
            this.upcominglist = res.data.results
          })
          .catch(err => {
            console.log(err)
          })
    },
    methods: {
    goToMovie(pk) {
      this.$router.push({ name: 'MovieDetail', params: {movieId: pk}})
    }
  }
}
</script>

<style>
.take-movies{
}
</style>