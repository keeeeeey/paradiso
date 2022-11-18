<template>
  <div class="poster-container" style="height: 100%">
    <img :src="imgurl + upcomingmovie.poster_path" alt="" class="mw-100" style="height: 100%">
  </div>
</template>

<script>
export default {
  name: 'UpcomingMovieListItem',
  props: {
    upcomingmovie: Object,
  },
  data() {
    return{
      imgurl: 'https://image.tmdb.org/t/p/original'
    }
  }

}
</script>

<style>
.poster-container{

}
</style>