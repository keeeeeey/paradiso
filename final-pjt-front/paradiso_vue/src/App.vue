<template>
  <div id="app" class="min-vh-100">
    <nav v-if="!isSelectView" class="navbar navbar-expand-lg position-fixed" style="width:70%">
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{ name: 'MovieView' }">
          <img src="./assets/logo.png" alt="Bootstrap" width="40">
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'MovieView' }"><i class="fa-solid fa-house fa-lg"></i></router-link>
            </li>
            <li v-if="!isLoggedIn" class="nav-item">
              <router-link class="nav-link" :to="{ name: 'SignUpView' }"><b>SIGN UP</b></router-link>
            </li>
            <li v-else class="nav-item">
              <router-link class="nav-link" :to="{ name: 'ProfileView', params: { nickname: userInfo?.nickname } }"><i class="fa-solid fa-user fa-lg"></i></router-link>
            </li>
            <li v-if="!isLoggedIn" class="nav-item">
              <router-link class="nav-link" :to="{ name: 'LogInView' }"><b>SIGN IN</b></router-link>
            </li>
            <li v-else class="nav-item">
              <router-link class="nav-link" @click.native="LogOut" :to="{ name: 'MovieView' }"><b>SIGN OUT</b></router-link>
            </li>
            <li class="nav-item dropdown">
              <a id="genre-nav-bar" class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="font-weight: bold">
                {{ genre }}
              </a>
              <ul class="dropdown-menu">
                <li v-for="genre in genres" :key="genre.id" @click="movieByGenre(genre.name)"><span class="dropdown-item cursor-pointer">{{ genre.name }}</span></li>
              </ul>
            </li>
          </ul>
          <form @submit.prevent="doSearch" class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model.trim="keyWord">
            <i type="submit" class="fa-solid fa-magnifying-glass fa-2x nav-icon" @click="doSearch"></i>
          </form>
        </div>
      </div>
    </nav>
    <router-view @Login="isLoggedIn=true" @reset-genre="resetGenre" :key="$route.fullPath" @search-bar-reset="searchBarReset" />

  </div>
</template>

<script>
import axios from "axios"


export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      genres: null,
      genre: "GENRES",
      keyWord: null,
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.user
    },
    isSelectView() {
      return this.$store.state.isSelectView
    }
  },
  created: function() {
    const token = localStorage.getItem("accessToken")

    if (token) {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/verify/",
        data: {'token': token}
      })
        .then(() => {
          this.isLoggedIn = true;
        })
        .catch((err) => {
          if (err.response.status === 401) {
            this.$store.dispatch("refresh")
            this.isLoggedIn = true;
            this.$router.go()
          }
        })
    }

    axios({
      method: "get",
      url: "http://127.0.0.1:8000/movies/genres/"
    })
      .then((res) => {
        this.genres = res.data
      }) 
      .catch((err) => {
        console.log(err)
      })
  },
  methods: {
    LogOut() {
      this.$store.dispatch("delete_user")
      localStorage.removeItem("accessToken")
      localStorage.removeItem("refreshToken")
      localStorage.removeItem("vuex")
      this.isLoggedIn = false
      this.$router.push({ name: "LogInView" })
    },

    movieByGenre(genre) {
      this.genre = genre
      this.$router.push({ name: "MoviesByGenreView", params: { "genre": genre } })
    },

    resetGenre() {
      this.genre = "GENRES"
    },

    doSearch() {
      const keyWord = this.keyWord
      if (keyWord) {
        this.$router.push({ name: "SearchResultView", params: { "keyWord": keyWord } }).catch(()=>{})
      } else {
        alert("검색어를 입력해주세요.")
      }
    },

    searchBarReset() {
      this.keyWord = null
    }
  }
}
</script>

<style>
#app {
  font-family: 'NanumSquareNeo-Variable';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 70%;
  margin: 0 auto;
  background-color: white;
  padding-bottom: 100px;
}

nav{
  z-index: 9999;
  background-color: rgb(31, 135, 195);
}

.nav-link{
  color: white;
}

.margin-by-fixed {
  padding-top: 56px;
}

.nav-icon {
  color: white;
  box-sizing: border-box;
  margin: 5px
}
.cursor-pointer{
  cursor: pointer;
}

@font-face {
  font-family: 'NanumSquareNeo-Variable';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/NanumSquareNeo-Variable.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
</style>
