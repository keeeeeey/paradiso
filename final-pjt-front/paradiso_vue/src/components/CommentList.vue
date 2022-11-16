<template>
  <div>
    <h1>댓글 리스트</h1>
    <CommentListItem v-for="comment in comments" :key="comment.id" :comment="comment"/>
  </div>
</template>

<script>
import CommentListItem from './CommentListItem.vue';
import axios from 'axios'


export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  props: {
    movieid: Number,
  },
  data() {
    return {
      comments: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.movieid}/comments/`,
    })
    .then(res => {
      this.comments = res.data
    })
    .catch(() => {
      console.log('댓글 가져오기 실패')
    })
  }
}
</script>

<style>

</style>