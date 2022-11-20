<template>
  <div class="margin-by-fixed">
    <h1>상영중인 영화</h1>
    <div class="d-flex poster-container" id="now-playlist-box">
      <div v-for="playmovie in playlist" :key="playmovie.id" class="col-2" id="now-playlist-item">
        <NowPlayListItem :playmovie="playmovie" @click.native="goToMovie(playmovie.id)" style="cursor:pointer"/>
      </div>
    </div>
    <button @click="scrollLeft">&lt;</button>
    <button @click="scrollRight">&gt;</button>
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
      url: 'https://api.themoviedb.org/3/movie/now_playing?api_key=9adec2ecce07845598e041a9836861b2&language=ko-KR&page=1&region=KR',
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
    },
    scrollLeft() {
      const width = document.getElementById('now-playlist-box').clientWidth
      document.getElementById('now-playlist-box').scrollLeft -= width;
    },
    scrollRight() {
      const width = document.getElementById('now-playlist-box').clientWidth
      document.getElementById('now-playlist-box').scrollLeft += width;
    }
  }
}
</script>

<style>
.poster-container{
 overflow-x: auto;
 scroll-behavior: smooth;
}
.poster-container::-webkit-scrollbar{
  display: none;
}
</style>