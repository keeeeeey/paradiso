<template>
  <div class="margin-by-fixed">
    <h1>상영 예정 영화</h1>
    <div class="d-flex poster-container" id="upcoming-movielist">
      <div v-for="upcomingmovie in upcominglist" :key="upcomingmovie.id" class="col-2 take-movies">
        <UpcomingMovieListItem :upcomingmovie="upcomingmovie" @click.native="goToMovie(upcomingmovie.id)" style="cursor: pointer;"/>
      </div>
    </div>
    <button @click="scrollLeft">&lt;</button>
    <button @click="scrollRight">&gt;</button>
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
            url: "https://api.themoviedb.org/3/movie/upcoming?api_key=9adec2ecce07845598e041a9836861b2&language=ko-KR&page=1"
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
    },
    scrollLeft() {
      const width = document.getElementById('upcoming-movielist').clientWidth
      document.getElementById('upcoming-movielist').scrollLeft -= width;
    },
    scrollRight() {
      const width = document.getElementById('upcoming-movielist').clientWidth
      document.getElementById('upcoming-movielist').scrollLeft += width;
    }
  }
}
</script>

<style>
</style>