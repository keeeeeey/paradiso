<template>
    <div class="margin-by-fixed" style="position: relative">
      <h1>좋아할만한 영화</h1>
      <div class="d-flex poster-container" id="my-favorite-box">
        <div v-for="myFavorite in myFavorites" :key="myFavorite.id" class="col-2" id="my-favorite-item">
          <MyFavoriteListItem :myFavorite="myFavorite" @click.native="goToMovie(myFavorite.id)" style="cursor:pointer"/>
        </div>
      </div>
      <i class="fa-solid fa-chevron-left fa-2x arrow-left" @click="scrollLeft"></i>
      <i class="fa-solid fa-chevron-right fa-2x arrow-right" @click="scrollRight"></i>
    </div>
  </template>
  
  <script>
  import MyFavoriteListItem from '@/components/MyFavoriteListItem'
  import axios from 'axios'
  const token = localStorage.getItem('accessToken')
  
  export default {
    name: 'MyFavoriteList',
    components: {
      MyFavoriteListItem,
    },
    data() {
      return {
        myFavorites: null,
      }
    },
    created() {
      if (token) {
        axios({
            method: "get",
            url: "http://127.0.0.1:8000/accounts/userfavorites/",
            headers: {'Authorization': `Bearer ${token}`},
        })
            .then((res) => {
                console.log(res.data)
                this.myFavorites = res.data
                // return res.data.favorite_movies
            })
            // .then((myFavorites) => {
            //     console.log(myFavorites)
            //     myFavorites.forEach((myFavorite) => {
            //         axios({
            //             method: 'get',
            //             url: `https://api.themoviedb.org/3/movie/${myFavorite}/similar?api_key=fc9c1f07b9650d1ec4f98fb39efa792e&language=ko-KR&page=1`,
            //         })
            //         .then((res) => {
            //             console.log(res.data)
            //         })
            //         .catch(err => {
            //             console.log(err)
            //         })      
            //     })  
            // })
            .catch((err) => {
                console.log(err)
            })
      }
    },
    methods: {
      goToMovie(pk) {
        this.$router.push({ name: 'MovieDetail', params: {movieId: pk}})
      },
      scrollLeft() {
        const width = document.getElementById('my-favorite-box').clientWidth
        document.getElementById('my-favorite-box').scrollLeft -= width;
      },
      scrollRight() {
        const width = document.getElementById('my-favorite-box').clientWidth
        document.getElementById('my-favorite-box').scrollLeft += width;
      }
    }
  }
  </script>
  
  <style>
  .poster-container{
   overflow-x: auto;
   scroll-behavior: smooth;
  }
  
  .poster-container::-webkit-scrollbar{
    display: none;
  }
  
  .arrow-left {
    color: white;
    z-index: 9999;
    position: absolute;
    top: 57.5%;
    left: 2.5%;
  }
  
  .arrow-right {
    color: white;
    z-index: 9999;
    position: absolute;
    top: 57.5%;
    right: 2.5%;
  }
  </style>