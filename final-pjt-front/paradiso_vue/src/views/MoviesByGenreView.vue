<template>
  <div id="movie-by-genre-view" class="margin-by-fixed">
    <h1 class="my-5">{{ genre }}</h1>
    <div class="row" style="margin: 0">
      <div
        v-for="movie in movies"
        :key="movie.id"
        :id="movie.id"
        class="movies-by-genre-box p-0 col-2"
      >
        <img
          :src="IMG_URL + movie.poster_path"
          alt=""
          :id="movie.id + 'img'"
          class="mw-100"
          style="height: 100%"
        />
      </div>
    </div>
    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
  </div>
</template>
  
  <script>
import axios from "axios";
import InfiniteLoading from "vue-infinite-loading";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MoviesByGenreView",
  components: {
    InfiniteLoading,
  },
  data() {
    return {
      movies: [],
      genre: String(this.$route.params.genre),
      IMG_URL: "https://image.tmdb.org/t/p/original",
      startindex: 0,
    };
  },
  methods: {
    infiniteHandler($state) {
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/${this.genre}/${this.startindex + 40}/${
          this.startindex
        }`,
      }).then(({ data }) => {
        console.log(data.length);
        if (data.length) {
          this.startindex += 40;
          this.movies.push(...data);
          $state.loaded();
        } else {
          $state.complete();
        }
      });
    },
  },
  destroyed() {
    this.$emit("reset-genre");
  },
};
</script>
  
  <style>
.movies-by-genre-box {
  overflow: hidden;
  border-radius: 10px;
}
</style>