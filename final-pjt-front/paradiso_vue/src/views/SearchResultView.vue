<template>
  <div id="search-result-view" class="margin-by-fixed px-5">
    <h1 class="mt-5">{{ keyWord }} 검색 결과</h1>
    <div class="mt-3 p-2" v-if="the_movie">
        <h2>영화 정보</h2>
        <div class="the-movie-container">
            <div class="the-movie-container-left col-3">
                <img src="" alt="">
            </div>
            <div class="the-movie-container-right col-9">
                {{ the_movie.title }}
            </div>
        </div>
    </div>
    <div>
        {{ search_result }}
    </div>
  </div>
</template>

<script>
import axios from "axios"


export default {
    name: "SearchResultView",
    data() {
        return {
            keyWord: String(this.$route.params.keyWord),
            the_movie: null,
            search_result: null,
            imgurl: 'https://image.tmdb.org/t/p/original',
        }
    },
    created() {
        console.log("create!!")
        console.log(this.keyWord)

        axios({
            method: "get",
            url: `http://127.0.0.1:8000/movies/search/${this.keyWord}`
        })
            .then((res) => {
                console.log(res.data)
                this.the_movie = res.data.the_movie_serializer
                this.search_result = res.data.serializer
            })
            .catch((err) => {
                console.log(err)
            })
    }
}
</script>

<style>
.the-movie-container {
    width: 100%;
    background-color: lightgray;
    display: flex;
}
</style>