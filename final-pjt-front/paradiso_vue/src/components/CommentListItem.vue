<template>
  <div>
    <p>
      <router-link :to="{ name: 'ProfileView', params: { nickname: comment.user.nickname} }">{{ comment.user.nickname }}: </router-link>
      {{ comment.content }} | 좋아요 개수 : {{ likecount }}
      <button @click="likeComment" v-show="!islike">좋아요</button>
      <button @click="likeComment" v-show="islike">좋아요 취소</button>
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
      likecount: this.comment.like_users_count,
      islike: false
    }
  },
  methods: {
    likeComment() {
      const token = localStorage.getItem('accessToken')
      if (token) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/likes/`,
          headers: {'Authorization': `Bearer ${token}`},
        })
        .then((res) => {
          this.islike = res.data.is_liked
          this.likecount = res.data.like_users_count
        })
        .catch(() => {
          console.log('좋아요 실패')
        })
      } else {
        alert('로그인이 필요합니다')
        this.$router.push({ name: 'LogInView' })
      }
  
    }
  },
  created() {
    const token = localStorage.getItem('accessToken')
    if (token) {
      axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/${this.comment.id}/comments/islike/`,
      headers: {'Authorization': `Bearer ${token}`},
    })
    .then(res => {
      this.islike = res.data.is_liked
    })
    } else {
      this.islike = false
    }
  }
}
</script>

<style>

</style>