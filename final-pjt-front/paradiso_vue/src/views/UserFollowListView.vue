<template>
  <div id="user-follow-list-view" class="margin-by-fixed px-5">
    <h1 class="mt-5 mb-4">{{ nickname }}님의 {{ follow }}</h1>
    <div v-for="person in follow_list" :key="person.id" class="user-follow-list-box m-2 p-3">
        <div class="user-follow-list-box-left">
            <img src="../assets/defaultprofileimg.jpeg" alt="">
        </div>
        <div class="user-follow-list-box-right">
            <span @click="goToProfile(person.nickname)">{{ person.nickname }}</span>
            <div>
                <span>팔로잉: {{ person.followings_count }} | 팔로워: {{ person.followers_count }}</span>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"


export default {
    name: "UserFollowListView",
    data() {
        return {
            nickname: String(this.$route.params.nickname),
            follow: String(this.$route.params.follow),
            follow_list: null,
        }
    },
    created() {
        if (this.follow === "팔로잉") {
            axios({
              method: "get",
              url: `http://127.0.0.1:8000/accounts/${this.nickname}/getfollowings/`
            })
              .then((res) => {
                console.log(res.data)
                this.follow_list = res.data
              })
              .catch((err) => {
                console.log(err.data)
              })
        } else if (this.follow === "팔로워") {
            axios({
              method: "get",
              url: `http://127.0.0.1:8000/accounts/${this.nickname}/getfollowers/`
            })
              .then((res) => {
                this.follow_list = res.data
              })
              .catch((err) => {
                console.log(err.data)
              })
        }
    },
    methods: {
        goToProfile(nickname) {
            this.$router.push({ name: "ProfileView", params: {"nickname": nickname} })
        }
    }
}
</script>

<style>
.user-follow-list-box {
    border: solid 5px lightgray;
    border-radius: 5px;
    display: flex;
    align-items: center;
}

.user-follow-list-box-left {
    width: 5%;
    margin-right: 10px;
}

.user-follow-list-box-left img {
    width: 100%;
    border-radius: 50%;
}

.user-follow-list-box-right {
    width: 95%;
    display: flex;
    justify-content: space-between;
}
</style>