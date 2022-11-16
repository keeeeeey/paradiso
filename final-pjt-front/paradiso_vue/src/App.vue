<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'MovieView' }">MovieView</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
      <router-link :to="{ name: 'LogInView' }">LogInPage</router-link>
    </nav>
    <router-view/>
    <h3>최신영화</h3>
    <LatestMovieView/>

  </div>
</template>

<script>
import LatestMovieView from './views/LatestMovieView.vue'
import axios from 'axios'


export default {
  name: 'MovieList',
  components: {
    LatestMovieView,
  },
  data() {
    return {
      movies: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: 'https://api.themoviedb.org/3/movie/latest?api_key=9adec2ecce07845598e041a9836861b2&language=kr-KR',
    })
    .then(res => {
      console.log(res.data)
    })
    .catch(err => {
      console.log(err)
    })
  }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
