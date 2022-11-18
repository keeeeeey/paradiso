<template>
  <div id="movie-view" class="margin-by-fixed">
    <h1>home</h1>
    <NowPlayList/>
    <MovieList/>
    <LatestMovieView/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import LatestMovieView from '@/views/LatestMovieView'
import NowPlayList from '@/components/NowPlayList'
import axios from 'axios'

export default {
    name: "MovieView",
    components: {
      MovieList,
      LatestMovieView,
      NowPlayList
    },
    data() {
      return{
        comment: null,
        movie_id: 1,
      }
    },
    created() {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/latest?api_key=9adec2ecce07845598e041a9836861b2&language=kr-KR',
      })
      .then((res) => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
}
</script>

<style>

</style>