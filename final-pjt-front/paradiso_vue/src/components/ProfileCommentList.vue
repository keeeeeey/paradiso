<template>
    <div style="text-align: center">
        <h1 class="mt-5 mt-1">작성한 댓글</h1>
        <div class="w-50 mx-auto">
            <div v-for="comment in commentList" :key="comment.id">
                <ProfileCommentListItem :comment="comment" />
                <hr>
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
</style>