<template>
  <div id="select-movie-view">
    <h1>SelectMovieView</h1>
  </div>
</template>

<script>
import axios from "axios"
const API_URL = "http://127.0.0.1:8000"

export default {
    name: "SelectMovieView",
    created() {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
        .then((res) => {
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
}
</script>

<style>

</style>