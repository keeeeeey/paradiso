<template>
  <div id="movie-view" class="margin-by-fixed">
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
        url: 'https://api.themoviedb.org/3/movie/now_playing?api_key=9adec2ecce07845598e041a9836861b2&language=en-US&page=1&region=KR',
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