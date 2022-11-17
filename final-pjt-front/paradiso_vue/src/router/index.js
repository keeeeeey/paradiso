import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MovieView from '@/views/MovieView'
import SelectMovieView from '@/views/SelectMovieView'
import MovieDetial from '@/views/MovieDetail'
import ProfileView from '@/views/ProfileView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
  },

  {
    path: '/selectMovie',
    name: 'SelectMovieView',
    component: SelectMovieView
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetail',
    component: MovieDetial
  },
  {
    path: '/profile/:nickname',
    name: 'ProfileView',
    component: ProfileView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
