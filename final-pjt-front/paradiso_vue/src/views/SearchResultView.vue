<template>
  <div id="search-result-view" class="margin-by-fixed px-5">
    <h1 class="mt-5">{{ keyWord }} 검색 결과</h1>
    <div class="mt-3 p-2" v-if="the_movie">
        <h2 class="mb-3">영화 정보</h2>
        <div class="the-movie-container p-3">
            <div class="the-movie-inner-container">
                <div class="the-movie-container-left p-3">
                    <img :src="imgurl + the_movie?.poster_path" alt="" class="w-100">
                </div>
                <div class="the-movie-container-right pt-3 pb-3 pe-3">
                    <h3 @click="goToMovie(the_movie.id)"><b>{{ the_movie.title }}</b></h3>
                    <p><span>개봉일 : {{ the_movie.release_date }}</span> ● <span>평점 : {{ the_movie.vote_average }}</span></p>
                    <h5>줄거리</h5>
                    <p>{{ the_movie.overview }}</p>
                </div>
            </div>
        </div>
    </div>
    <div v-for="result in search_result" :key="result.id" class="result-list-box m-2 p-3" @click="goToMovie(result.id)">
        <div class="result-list-box-left">
            <img :src="imgurl + result.poster_path" alt="" class="w-100">
        </div>
        <div class="result-list-box-right ps-2 pe-2">
            <h5><b>{{ result.title }}</b></h5>
            <p><span>개봉일 : {{ result.release_date }}</span> ● <span>평점 : {{ result.vote_average }}</span></p>
            <p><b>줄거리</b></p>
            <p>{{ result.overview }}</p>
        </div>
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
    },
    destroyed() {
        this.$emit("search-bar-reset")
    },
    methods: {
        goToMovie(pk) {
            this.$router.push({ name: 'MovieDetail', params: {movieId: pk}})
        },
    }
}
</script>

<style>
.the-movie-container {
    width: 100%;
    background-color: lightgray;
    box-sizing: border-box;
    border-radius: 5px;
}

.the-movie-inner-container {
    display: flex;
    background: white;
    border-radius: 5px;
}

.the-movie-container-left {
    width: 30%;
}

.the-movie-container-right {
    width: 70%;
}

.the-movie-container-right p {
    width: 100%;
    text-overflow: ellipsis;
    overflow: hidden;
    word-break: break-word;
    
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical
}

.result-list-box {
    border: solid 5px lightgray;
    border-radius: 5px;
    display: flex;
}

.result-list-box-left {
    width: 10%;
}

.result-list-box-right {
    width: 90%;
}

.result-list-box-right p {
    widows: 100%;
    overflow: hidden;
    white-space:nowrap;
    text-overflow: ellipsis;
}
</style>