<template>
  <div class="margin-by-fixed">
    <div class="profile-data-box">
      <div class="profile-img-box">
        <img src="../assets/defaultprofileimg.jpeg" alt="profile-img" class="profile-img">        
      </div>
      <i class="fa-solid fa-camera fa-2x profile-img-update" data-bs-toggle="modal" data-bs-target="#exampleModal"></i>
      <div class="d-flex justify-content-center align-items-center">
        <h1>{{ nickname }}</h1>
        <div v-if="!isMypage" style="margin-left: 10px;">
          <button @click="follow" v-if="!isfollow" class="btn btn-primary">팔로우</button>
          <button @click="follow" v-if="isfollow" class="btn btn-primary">언팔로우</button>
        </div>
      </div>
      <div v-if="totalData">
        <span @click="getFollowings">팔로잉: {{ totalData.userSerializer.followings_count }}</span> | <span @click="getFollowers">팔로워: {{ followercount }}</span>
      </div>
      <br>
    </div>
    <ProfileLikeMovieList :likeMovieList="totaldata?.movieSerializer"/>
    <h1 class="text-center mt-5 mt-1">작성한 댓글</h1>
    <ProfileCommentList :commentList="totaldata?.commentSerializer"/>
    <h1 class="text-center mt-5 mt-1">좋아요한 댓글</h1>
    <ProfileCommentList :commentList="totaldata?.likeCommentSerializer"/>

    <!-- Modal -->
    <div class="modal fade modal-lg" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" style="margin-top: 200px;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">사진 선택</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form method="post" enctype="multipart/form-data">
              <input type="file" id="chooseFile" name="chooseFile" ref="serveyImage" @change="loadFile()">
            </form>
            <div class="fileContainer">
              <div class="fileInput">
                <p>FILE NAME: </p>
                <p id="fileName"></p>
              </div>
              <div class="button ms-3 me-2">
                <label for="chooseFile">
                  CLICK HERE!
                </label>
              </div>
              <div class="buttonContainer">
                <div class="submitButton" id="submitButton">SUBMIT</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileLikeMovieList from '@/components/ProfileLikeMovieList'
import ProfileCommentList from '@/components/ProfileCommentList'
import axios from 'axios'


export default {
    name: 'ProfileView',
    components: {
      ProfileLikeMovieList,
      ProfileCommentList
    },
    data() {
      return {
        nickname: String(this.$route.params.nickname),
        totaldata: null,
        isfollow: false,
        followrcount: null,
        isMypage: false,
      }
    },
    computed: {
      totalData() {
        return this.totaldata
      },
    },
    created() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.nickname}/`,
      })
      .then(res => {
        console.log(res)
        this.totaldata = res.data.serializer
        this.followercount = res.data.serializer.userSerializer.followers_count
      })
      this.getIsFollow()
    },
    methods: {
      follow() {
        const token = localStorage.getItem('accessToken')
        if (token) {
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/accounts/${this.totaldata.userSerializer.id}/follow/`,
            headers: {'Authorization': `Bearer ${token}`}
          })
          .then((res) => {
            this.isfollow = res.data.is_followed
            this.followercount = res.data.followers_count
          })
          .catch((err) => {
            // console.log(err)
            if (err.response.status === 401) {
              this.$store.dispatch("refresh")
              this.follow()
            }
          })
        } else {
          alert('로그인이 필요합니다.')
          this.$router.push({ name: 'LogInView' })
        }
      },

      getFollowings() {
        this.$router.push({ name: "UserFollowListView", params: { "nickname": this.nickname, "follow": "팔로잉" } })
      },

      getFollowers() {
        this.$router.push({ name: "UserFollowListView", params: { "nickname": this.nickname, "follow": "팔로워" } })
      },

      loadFile() {
        console.log(this.$refs)
        let name = document.getElementById('fileName');
        name.textContent = this.$refs.serveyImage.files[0].name;
      },

      getIsFollow() {
        const token = localStorage.getItem('accessToken')
        if (token) {
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/${this.nickname}/isfollow/`,
            headers: {'Authorization': `Bearer ${token}`}
          })
          .then(res => {
            this.isfollow = res.data.is_followed
            this.isMypage = res.data.is_mypage
          })
          .catch((err) => {
            if (err.response.status === 401) {
              this.$store.dispatch("refresh")
              this.getIsFollow()
            }
          })
        } else {
          this.isfollow = false
        } 
      }
    }
}
</script>

<style>
.profile-img-box {
  width: 25%;
  border: solid 2px gray; 
  border-radius: 50%;
  margin: 10px auto;
  aspect-ratio: 1 / 1;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.profile-img {
  width: 100%;
}

.profile-data-box {
  text-align: center;
  margin-top: 50px;
}

.button {
    display: flex;
    justify-content: center;
}

label {
    cursor: pointer;
    font-size: 1em;
}

#chooseFile {
    visibility: hidden;
}

.fileContainer {
    display: flex;
    justify-content: center;
    align-items: center;
}

.fileInput {
    display: flex;
    align-items: center;
    border-bottom: solid 2px black;
    width: 60%;
    height: 30px;
}

#fileName {
    margin-left: 5px;
}

.buttonContainer {
    width: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 10px;
    background-color: rgb(31, 135, 195);;
    color: white;
    border-radius: 30px;
    padding: 5px;
    font-weight: bold;
    cursor: pointer;
}
</style>