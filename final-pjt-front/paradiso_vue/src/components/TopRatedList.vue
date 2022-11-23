<template>
  <div id="top-rated-list">
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="true">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" aria-label="Slide 4"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="4" aria-label="Slide 5"></button>
      </div>
      <div class="carousel-inner" v-if="playlist">
        <div class="carousel-item active">
          <TopRatedListItem :playmovie="playlist[0]" style="cursor:pointer"/>
        </div>
        <div class="carousel-item">
          <TopRatedListItem :playmovie="playlist[1]" style="cursor:pointer"/>
        </div>
        <div class="carousel-item">
          <TopRatedListItem :playmovie="playlist[2]" style="cursor:pointer"/>
        </div>
        <div class="carousel-item">
          <TopRatedListItem :playmovie="playlist[3]" style="cursor:pointer"/>
        </div>
        <div class="carousel-item">
          <TopRatedListItem :playmovie="playlist[4]" style="cursor:pointer"/>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import TopRatedListItem from '@/components/TopRatedListItem'
import _ from 'lodash'

export default {
    name: "TopRatedList",
    data() {
      return {
        playlist: null,
      }
    },
    components: {
      TopRatedListItem,
    },
    created() {
        axios({
            method: "get",
            url: "https://api.themoviedb.org/3/movie/top_rated?api_key=9adec2ecce07845598e041a9836861b2&language=ko-KR&page=1&region=KR"
        })
          .then((res) => {
            this.playlist = _.sampleSize(res.data.results, 5)
          })
    }
}
</script>

<style>

</style>