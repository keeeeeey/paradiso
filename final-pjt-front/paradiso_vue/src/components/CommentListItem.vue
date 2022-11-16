<template>
  <div>
    <p>
      {{ comment.content }} | 좋아요 개수 : {{ likecount }}
      <button @click="likeComment">좋아요</button>
    </p>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  data() {
    return {
      likecount: this.comment.like_users_count
    }
  },
  methods: {
    likeComment() {
      const token = localStorage.getItem('accessToken')
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/likes/`,
        headers: {'Authorization': `Bearer ${token}`},
      })
      .then((res) => {
        if (res.data.is_liked) {
            this.likecount += 1
          } else {
            this.likecount -= 1
          }
      })
      .catch(() => {
        console.log('좋아요 실패')
      })
    }
  }
}
</script>

<style>

</style>