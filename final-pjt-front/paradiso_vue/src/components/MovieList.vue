<template>
  <div>
    <h1>영화리스트</h1>
    <MovieListItem/>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue';
import axios from 'axios'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data() {
    return {
      movies: null,
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
  }
}
</script>

<style>

</style>