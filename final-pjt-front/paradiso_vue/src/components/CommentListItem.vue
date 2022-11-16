<template>
  <div>
    <p>
      {{ comment.content }} | 좋아요 개수 : {{ comment.like_users_count }}
      <button @click="likeComment">좋아요</button>
    </p>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  methods: {
    likeComment() {
      
    }
  }
}
</script>

<style>

</style>