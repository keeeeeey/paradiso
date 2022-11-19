<template>
    <div class="comment-container">
        <p><b>{{ comment.movie.title }}</b></p>
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
}
</script>

<style>
    .comment-container {
        text-align: left;
        box-sizing: border-box;
        padding: 5px;
    }
</style>