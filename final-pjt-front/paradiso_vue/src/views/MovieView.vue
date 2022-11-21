<template>
  <div id="movie-view" class="margin-by-fixed">
    <TopRatedList/>
    <MostFavoriteList/>
    <MyFavoriteList v-if="isLoggedIn"/>
    <NowPlayList/>
    <UpcomingMovieList/>
  </div>
</template>

<script>
import TopRatedList from '@/components/TopRatedList'
import NowPlayList from '@/components/NowPlayList'
import UpcomingMovieList from '@/components/UpcomingMovieList'
import MyFavoriteList from '@/components/MyFavoriteList'
import MostFavoriteList from '@/components/MostFavoriteList'

export default {
    name: "MovieView",
    components: {
      TopRatedList,
      NowPlayList,
      UpcomingMovieList,
      MyFavoriteList,
      MostFavoriteList,
    },
    data() {
      return{
        isLoggedIn: localStorage.getItem("accessToken")
      }
    },
}
</script>

<style>

</style>