<template>
    <div class="comment-container">
        <p><b @click="goToMovieDetail" style="cursor: pointer">{{ comment.movie.title }}</b></p>
        <div class="d-flex justify-content-between">
            <p style="margin: 0;">{{ comment.content }}</p>
            <p style="margin: 0;">좋아요 수 : {{ comment.like_users_count }}</p>
        </div>
        
    </div>
</template>

<script>

export default {
    name: 'ProfileCommentListItem',
    props: {
        comment: Object,
    },
    methods: {
        goToMovieDetail() {
            console.log(this.comment.movie)
            this.$router.push({ name: 'MovieDetail', params: {movieId: this.comment.movie.id}})
        }
    }
}
</script>

<style scoped>
    .comment-container {
        text-align: left;
        box-sizing: border-box;
        padding: 5px;
    }
</style>