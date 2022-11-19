<template>
    <div id="profile-like-movie-list-item" class="a">
        <img :src="imgurl + likeMovie.poster_path" alt="" class="img-fluid" style="height: 100%">
    </div>
</template>
  
<script>

export default {
    name: 'ProfileLikeMovieListItem',
    props: {
        likeMovie: Object,
    },
    data() {
        return {
            imgurl: 'https://image.tmdb.org/t/p/original'
        }
    },
}
</script>
  
<style>
#profile-like-movie-list-item {
    height: 100%;
}

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