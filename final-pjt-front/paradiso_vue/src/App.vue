<template>
  <div id="app" class="min-vh-100">
    <nav class="navbar navbar-expand-lg position-fixed" style="width:70%">
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
            <!-- <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled">Disabled</a>
            </li> -->
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <!-- <button class="btn btn-outline-success" type="submit">Search</button> -->
            <i type="submit" class="fa-solid fa-magnifying-glass fa-2x nav-icon"></i>
          </form>
        </div>
      </div>
    </nav>
    <router-view @Login="isLoggedIn=true" :key="$route.fullPath"/>

  </div>
</template>

<script>


export default {
  name: 'App',
  data() {
    return {
      movies: null,
      isLoggedIn: false,
    }
  },
  computed: {
    userInfo() {
      return this.$store.state.user
    }
  },
  created: function() {
    const token = localStorage.getItem("accessToken");
    if (token) {
      this.isLoggedIn = true;
    }
  },
  methods: {
    LogOut() {
      this.$store.dispatch("delete_user")
      localStorage.removeItem("accessToken")
      localStorage.removeItem("vuex")
      this.isLoggedIn = false
      this.$router.push({ name: "LogInView" })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* padding-left: 15%;
  padding-right: 15%; */
  width: 70%;
  margin: 0 auto;
  background-color: white;
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
</style>
