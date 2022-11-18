<template>
  <div id="now-play-list">
    <NowPlayListItem v-for="nowplay in playlist" :key="nowplay.id" :playmovie="nowplay"/>
  </div>
</template>

<script>
import axios from "axios"
import NowPlayListItem from '@/components/NowPlayListItem'
import _ from 'lodash'

export default {
    name: "NowPlayList",
    data() {
      return {
        playlist: null,
      }
    },
    components: {
      NowPlayListItem,
    },
    created() {
        axios({
            method: "get",
            url: "https://api.themoviedb.org/3/movie/now_playing?api_key=fc9c1f07b9650d1ec4f98fb39efa792e&language=ko-KR&page=1"
        })
            .then((res) => {
              console.log(res.data)
                this.playlist = _.sampleSize(res.data.results, 5)
            })
    }
}
</script>

<style>

</style>