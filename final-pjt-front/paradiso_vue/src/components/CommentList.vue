<template>
    <div>
      <div class="w-75 mx-auto">
        <CommentListItem v-for="comment in comments" :key="comment.id" :comment="comment" @updatecomment="updateComment"/>
      </div>
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
      console.log(res.data)
    })
    .catch(() => {
      console.log('댓글 가져오기 실패')
    })
  },
  methods: {
    updateComment() {
      this.$emit('updatecomment')
    }
  }
}
</script>

<style>

</style>