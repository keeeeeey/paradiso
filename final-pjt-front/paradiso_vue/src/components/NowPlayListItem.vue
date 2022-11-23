<template>
  <div class="a" style="height: 100%">
    <img :src="imgurl + playmovie.poster_path" alt="" class="img-fluid" style="height: 100%">
  </div>
</template>

<script>


export default {
    name: 'NowPlayListItem',
    props: {
      playmovie: Object,
    },
    data() {
      return {
        imgurl: 'https://image.tmdb.org/t/p/original'
      }
    },
}
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