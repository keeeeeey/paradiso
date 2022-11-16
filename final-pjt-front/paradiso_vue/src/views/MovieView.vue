<template>
  <div id="movie-view">
    <h1>home</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
    name: "MovieView",
    components: {
      MovieList,
    },
    data() {
      return{
        comment: null,
        movie_id: 1,
      }
    },
}
</script>

<style>

</style>