<template>
  <div id="movie-view" class="margin-by-fixed">
    <TopRatedList/>
    <NowPlayList/>
    <LatestMovieView/>
  </div>
</template>

<script>
import LatestMovieView from '@/views/LatestMovieView'
import NowPlayList from '@/components/NowPlayList'
import TopRatedList from '@/components/TopRatedList'

export default {
    name: "MovieView",
    components: {
      LatestMovieView,
      NowPlayList,
      TopRatedList
    },
    data() {
      return{
        comment: null,
        movie_id: 1,
      }
    },
    created() {
      
    }
}
</script>

<style>

</style>