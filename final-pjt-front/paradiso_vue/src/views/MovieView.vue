<template>
  <div id="movie-view" class="margin-by-fixed">
    <TopRatedList/>
    <NowPlayList/>
    <UpcomingMovieList/>
  </div>
</template>

<script>
import TopRatedList from '@/components/TopRatedList'
import NowPlayList from '@/components/NowPlayList'
import UpcomingMovieList from '@/components/UpcomingMovieList'

export default {
    name: "MovieView",
    components: {
      TopRatedList,
      NowPlayList,
      UpcomingMovieList,
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