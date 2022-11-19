<template>
    <div style="text-align: center">
        <h1 class="mt-5 mt-1">좋아요한 영화</h1>
        <div class="d-flex poster-container">
            <div v-for="likeMovie in likeMovieList" :key="likeMovie.id" class="col-2">
                <ProfileLikeMovieListItem :likeMovie="likeMovie" @click.native="goToMovie(likeMovie.id)" />
            </div>
        </div>
    </div>
</template>
  
<script>
import ProfileLikeMovieListItem from '@/components/ProfileLikeMovieListItem.vue'

export default {
    name: 'ProfileLikeMovieList',
    components: {
        ProfileLikeMovieListItem,
    },
    props: {
        likeMovieList: Array,
    },
    methods: {
        goToMovie(pk) {
            this.$router.push({ name: 'MovieDetail', params: { movieId: pk } })
        }
    },
}
</script>
  
<style>
.poster-container {
    overflow-x: auto;
}

.poster-container::-webkit-scrollbar {
    display: none;
}
</style>