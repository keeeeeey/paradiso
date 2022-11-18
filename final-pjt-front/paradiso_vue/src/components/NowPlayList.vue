<template>
  <div id="now-play-list">
    <h1>NowPlayList</h1>
  </div>
</template>

<script>
import axios from "axios"

export default {
    name: "NowPlayList",
    created() {
        axios({
            method: "get",
            url: "https://api.themoviedb.org/3/movie/now_playing?api_key=fc9c1f07b9650d1ec4f98fb39efa792e&language=ko-KR&page=1"
        })
            .then((res) => {
                console.log(res.data.results)
            })
    }
}
</script>

<style>

</style>