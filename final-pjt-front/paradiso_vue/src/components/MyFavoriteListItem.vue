<template>
  <div class="a ms-2" style="height: 100%; border-radius: 10px;">
    <img
      :src="imgurl + myFavorite.poster_path"
      alt=""
      class="img-fluid"
      style="height: 100%"
    />
  </div>
</template>
  
  <script>
export default {
  name: "MyFavoriteListItem",
  props: {
    myFavorite: Object,
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