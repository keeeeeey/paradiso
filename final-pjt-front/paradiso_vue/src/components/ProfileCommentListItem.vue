<template>
    <div class="comment-container">
        <p><b>{{ comment.movie.title }}</b></p>
        <p style="margin: 0;">{{ comment.content }}</p>
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