<template>
  <div class="select-movie-box" :class="{ 'checked-box' : isChecked }">
    <img :src="IMG_URL + movie.poster_path" alt="" class="mw-100" style="height: 100%" @click="selectFavoriteMovie(movie.id)" :class="{checked : isChecked}">
  </div>
</template>

<script>

export default {
    name: "SelectMovieView",
    props: {
        movie: Object
    },
    data() {
        return {
            IMG_URL: "https://image.tmdb.org/t/p/original",
            isChecked: false,
        }
    },
    methods: {
      selectFavoriteMovie(id) {
        this.isChecked = !this.isChecked
        this.$emit("from-select-movie-item", id)
      }
    },
}
</script>

<style>
.checked-box {
    box-shadow: 0 0 .2rem #fff, 0 0 .2rem #fff, 0 0 2rem #1f87c3, 0 0 0.8rem #1f87c3, 0 0 2.8rem #1f87c3;
    z-index: 1;
}

.checked {
  scale: 1.1;
}

.select-movie-box {
  overflow: hidden;
  border-radius: 10px;
}

.select-movie-box img {
  transition: all 0.2s linear;
}

</style>