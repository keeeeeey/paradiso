<template>
    <div style="text-align: center">
        
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