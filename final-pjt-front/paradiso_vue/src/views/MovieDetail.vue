<template>
  <div>
    <h1>detail</h1>
    <p>{{ movie_id }}</p>
  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'MovieDetail',
    data() {
        return {
            movie_id: this.$route.params.movieId
        }
    },
    created() {
        axios({
            method: 'get',
            url: `http://127.0.0.1:8000/movies/${this.movie_id}`,
        })
        .then(res => {
            console.log(res)
        })
    }
}
</script>

<style>

</style>