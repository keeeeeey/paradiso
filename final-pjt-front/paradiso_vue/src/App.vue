<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light w-100 position-fixed">
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{ name: 'MovieView' }">
          <img src="./assets/logo.png" alt="Bootstrap" width="30" height="24">
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'MovieView' }">Home</router-link>
            </li>
            <li v-if="!isLoggedIn" class="nav-item">
              <router-link class="nav-link" :to="{ name: 'SignUpView' }">SignUpPage</router-link>
            </li>
            <li v-else class="nav-item">
              <router-link class="nav-link" :to="{ name: 'SignUpView' }">MyPage</router-link>
            </li>
            <li v-if="!isLoggedIn" class="nav-item">
              <router-link class="nav-link" :to="{ name: 'LogInView' }">LogInPage</router-link>
            </li>
            <li v-else class="nav-item">
              <router-link class="nav-link" @click.native="LogOut" :to="{ name: 'MovieView' }">LogOut</router-link>
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
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
    <router-view @Login="isLoggedIn=true"/>

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
  created: function() {
    const token = localStorage.getItem("accessToken");
    if (token) {
      this.isLoggedIn = true;
    }
  },
  methods: {
    LogOut() {
      localStorage.removeItem("accessToken")
      this.isLoggedIn = false
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
}

nav{
  z-index: 1;
}

.margin-by-fixed {
  padding-top: 56px;
}
</style>
