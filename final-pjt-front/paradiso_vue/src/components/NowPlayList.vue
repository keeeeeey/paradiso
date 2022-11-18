<template>
  <div>
    <h1>상영중인 영화</h1>
    <div class="d-flex poster-container">
      <div v-for="playmovie in playlist" :key="playmovie.id" class="col-3">
        <NowPlayListItem :playmovie="playmovie" @click.native="goToMovie(playmovie.id)"/>
      </div>
    </div>
  </div>
</template>

<script>
import NowPlayListItem from '@/components/NowPlayListItem';
import axios from 'axios'

export default {
  name: 'NowPlayList',
  components: {
    NowPlayListItem,
  },
  data() {
    return {
      playlist: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/',
    })
    .then(res => {
      console.log(res)
    })
    .catch(err => {
      console.log(err)
    })
    axios({
      method: 'get',
      url: 'https://api.themoviedb.org/3/movie/now_playing?api_key=9adec2ecce07845598e041a9836861b2&language=en-US&page=1&region=KR',
    })
    .then((res) => {
      this.playlist = res.data.results
    })
    .catch(err => {
      console.log(err)
    })
  },
  methods: {
    goToMovie(pk) {
      this.$router.push({ name: 'MovieDetail', params: {movieId: pk}})
    }
  }
}
</script>

<style>
.poster-container{
 overflow-x: auto;
}
.poster-container::-webkit-scrollbar{
  display: none;
}
</style>