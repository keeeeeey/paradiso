<template>
    <div>
        <h1>작성한 댓글</h1>
        <div>
            <div v-for="comment in commentList" :key="comment.id" class="col-2">
                <ProfileCommentListItem :comment="comment" />
            </div>
        </div>
    </div>
</template>
  
<script>
import ProfileCommentListItem from '@/components/ProfileCommentListItem.vue'

export default {
    name: 'ProfileCommentList',
    components: {
        ProfileCommentListItem,
    },
    props: {
        commentList: Array,
    },
}
</script>
  
<style>
/* .poster-container {
    overflow-x: auto;
}

.poster-container::-webkit-scrollbar {
    display: none;
} */
</style>