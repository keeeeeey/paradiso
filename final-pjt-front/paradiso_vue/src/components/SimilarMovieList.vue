<template>
  <div class="margin-by-fixed" style="position: relative">
    <h1>{{ moviedata?.title }}과 비슷한 영화</h1>
    <div class="d-flex poster-container p-2" id="now-playlist-box">
      <div v-for="similarmovie in similarmovies" :key="similarmovie.id" class="col-2 me-2" id="now-playlist-item">
        <SimilarMovieListItem :similarmovie="similarmovie" @click.native="goToMovie(similarmovie.id)" style="cursor:pointer"/>
      </div>
    </div>
    <i class="fa-solid fa-chevron-left fa-2x arrow-left cursor-pointer" @click="scrollLeft"></i>
    <i class="fa-solid fa-chevron-right fa-2x arrow-right cursor-pointer" @click="scrollRight"></i>
  </div>
</template>

<script>
import SimilarMovieListItem from '@/components/SimilarMovieListItem.vue'


export default {
  name: 'SimilarMovieList',
  data() {
    return{
    }
  },
  props: {
    similarmovies: Array,
    moviedata: Object,
  },
  components: {
    SimilarMovieListItem,
  },
  methods: {
    goToMovie(pk) {
      this.$router.push({ name: 'MovieDetail', params: {movieId: pk}})
    },
    scrollLeft() {
      const width = document.getElementById('now-playlist-box').clientWidth
      document.getElementById('now-playlist-box').scrollLeft -= width;
    },
    scrollRight() {
      const width = document.getElementById('now-playlist-box').clientWidth
      document.getElementById('now-playlist-box').scrollLeft += width;
    }
  }
}
</script>

<style>

</style>