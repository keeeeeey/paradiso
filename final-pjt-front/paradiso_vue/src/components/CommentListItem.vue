<template>
  <div id="comment-item">
      <p @click="goToProfile(comment.user.nickname)" style="text-align:left;"><b>{{ comment.user.nickname }}</b></p>
      <div class="d-flex justify-content-between">
          <span>{{ comment.content }}</span>
          <span class="d-flex flex-column">
            <div>
              <button @click="deleteComment" class="btn btn-danger comment-delete-button">삭제</button>
              <button @click="likeComment" v-show="!islike" class="btn btn-primary comment-like-button">좋아요</button>
              <button @click="likeComment" v-show="islike" class="btn btn-primary comment-like-button">좋아요 취소</button>
            </div>
            <span style="text-align:right">좋아요 수 : {{ likecount }}</span>
          </span>
          
      </div>
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
  
    },
    deleteComment() {
      const token = localStorage.getItem('accessToken')
      if (token) {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/`,
          headers: {'Authorization': `Bearer ${token}`},
        })
        .then(() => {
          document.getElementById("comment-item").remove()
        })
        .catch(err => {
          console.log(err)
        })
      } else {
        alert('로그인이 필요합니다')
        this.$router.push({ name: 'LogInView' })
      }
    },
    goToProfile(nickname) {
      this.$router.push({ name: "ProfileView", params: {"nickname": nickname} })
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
.comment-like-button{

}
.comment-delete-button{
  margin-top: 0;
}

</style>