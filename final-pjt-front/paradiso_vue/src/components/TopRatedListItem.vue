<template>
  <div @click="goToMovie" style="height: 600px">  
    <img :src="imgurl + playmovie.backdrop_path" class="d-block w-100" alt="...">
    <p class="play-list-title position-absolute">{{ playmovie.title }}</p>
  </div>

</template>

<script>
export default {
  name: 'TopRatedListItem',
  data() {
    return {
      imgurl: 'https://www.themoviedb.org/t/p/w1280_and_h720_bestv2'
    }
  },
  props: {
    playmovie: Object,
  },
  methods: {
    goToMovie() {
      this.$router.push({ name: 'MovieDetail', params: {movieId: this.playmovie.id}})
    }
  }
}
</script>

<style>
.play-list-title {
  color: white;
  font-weight: bold;
  font-size: 40px;
  left: 10%;
  bottom: 10%;
  text-shadow: 1px 1px 1px grey;
}
</style>