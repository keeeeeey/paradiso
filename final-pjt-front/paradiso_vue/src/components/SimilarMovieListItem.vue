<template>
  <div class="a" style="height: 100%">
    <img :src="imgurl + similarmovie.poster_path" alt="" class="img-fluid" style="height: 100%">
  </div>
</template>

<script>
export default {
  name: 'SimilarMovieListItem',
  props: {
    similarmovie: Object,
  },
  data() {
    return {
      imgurl: 'https://image.tmdb.org/t/p/original'
    }
  }
}
</script>

<style>

</style>