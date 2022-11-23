<template>
  <div class="a ms-2" style="height: 100%; border-radius: 10px;">
    <img
      :src="imgurl + mostFavorite.poster_path"
      alt=""
      class="img-fluid"
      style="height: 100%;"
    />
  </div>
</template>
  
  <script>
export default {
  name: "MostFavoriteListItem",
  props: {
    mostFavorite: Object,
  },
  data() {
    return {
      imgurl: "https://image.tmdb.org/t/p/original",
    };
  },
};
</script>
  
  <style>
.a {
  overflow: hidden;
}

.a img {
  transition: all 0.2s linear;
}

.a:hover img {
  transform: scale(1.1);
}
</style>