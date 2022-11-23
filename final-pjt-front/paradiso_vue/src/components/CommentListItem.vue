<template>
  <div id="comment-item">
    <div class="d-flex align-items-center mb-3">
      <img src="../assets/defaultprofileimg.jpeg" alt="" class="comment-profile-img me-2">
      <p @click="goToProfile(comment.user.nickname)" style="text-align:left; cursor: pointer; margin: 0"><b>{{ comment.user.nickname }}</b></p><span style="font-size: 12px; margin-left: 10px;">{{ comment.created_at }}</span>
    </div>
    <div class="d-flex justify-content-between">
      <span>{{ comment.content }}</span>
      <span class="d-flex flex-column">
        <div>
          <i @click="updateCommentForm" v-if="user && user.nickname === comment.user.nickname" class="fa-solid fa-pen m-1"></i>
          <i @click="deleteComment" v-if="user && user.nickname === comment.user.nickname" class="fa-solid fa-trash m-1"></i>
          <i @click="likeComment" v-show="!islike" class="fa-regular fa-heart m-1"></i>
          <i @click="likeComment" v-show="islike" class="fa-solid fa-heart m-1" style="color: red;"></i>
          <span class="m-1" style="text-align:right">{{ likecount }}</span>
        </div>
      </span>  
    </div>
    <div class="input-group flex-nowrap w-100 mt-3" v-show="updateForm">
      <input v-model="updatedComment" type="text" class="form-control">
      <button @click="updateComment" class="input-group-text" id="addon-wrapping">수정하기</button>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  data() {
    return {
      likecount: this.comment.like_users_count,
      islike: false,
      updateForm: false,
      updatedComment: this.comment.content,
      componentRerender: 0,
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
        .catch((err) => {
          // console.log(err)
          if (err.response.status === 401) {
            this.$store.dispatch("refresh")
            this.likeComment()
          }
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
          if (err.response.status === 401) {
            this.$store.dispatch("refresh")
            this.deleteComment()
          }
        })
      } else {
        alert('로그인이 필요합니다')
        this.$router.push({ name: 'LogInView' })
      }
    },
    updateCommentForm() {
      this.updateForm = !this.updateForm
    },
    updateComment() {
      const updatedComment = this.updatedComment
      const token = localStorage.getItem('accessToken')
      
      axios({
        method: "put",
        url: `http://127.0.0.1:8000/movies/comments/${this.comment.id}/`,
        headers: {'Authorization': `Bearer ${token}`},
        data: {
          content: updatedComment,
        }
      })
        .then((res) => {
          console.log(res)
          this.updateForm = false
          this.$emit('updatecomment')
        })
        .catch((err) => {
          if (err.response.status === 401) {
            this.$store.dispatch("refresh")
            this.updateComment()
          }
        })

    },
    goToProfile(nickname) {
      this.$router.push({ name: "ProfileView", params: {"nickname": nickname} })
    },
    getIsLikeComment() {
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
        .catch((err) => {
          if (err.response.status === 401) {
            this.$store.dispatch("refresh")
            this.getIsLikeComment()
          }
        })
      } else {
        this.islike = false
      }
    }
  },
  created() {
    this.getIsLikeComment()
  }
}
</script>

<style>
.comment-delete-button {
  margin-top: 0;
}

.comment-profile-img {
  width: 5%; 
  border-radius: 50%;
}
</style>