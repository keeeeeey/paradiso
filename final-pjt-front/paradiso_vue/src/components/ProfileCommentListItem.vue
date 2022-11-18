<template>
    <div id="profile-comment-list-item">
        {{ comment.content }}
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
</style>