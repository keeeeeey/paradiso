<template>
    <div class="margin-by-fixed" style="position: relative">
      <h1>사람들이 가장 많이 선택한 영화</h1>
      <div class="d-flex poster-container" id="most-favorite-box">
        <div v-for="mostFavorite in mostFavorites" :key="mostFavorite.id" class="col-2" id="most-favorite-item">
          <MostFavoriteListItem :mostFavorite="mostFavorite" @click.native="goToMovie(mostFavorite.id)" style="cursor:pointer"/>
        </div>
      </div>
      <i class="fa-solid fa-chevron-left fa-2x arrow-left cursor-pointer" @click="scrollLeft"></i>
      <i class="fa-solid fa-chevron-right fa-2x arrow-right cursor-pointer" @click="scrollRight"></i>
    </div>
  </template>
  
  <script>
  import MostFavoriteListItem from '@/components/MostFavoriteListItem'
  import axios from 'axios'
  
  export default {
    name: 'MostFavoriteList',
    components: {
        MostFavoriteListItem,
    },
    data() {
      return {
        mostFavorites: null,
      }
    },
    created() {
        axios({
            method: "get",
            url: "http://127.0.0.1:8000/accounts/mostfavorite/",
        })
            .then((res) => {
                this.mostFavorites = res.data
            })
            .catch((err) => {
                console.log(err)
            })
    },
    methods: {
      goToMovie(pk) {
        this.$router.push({ name: 'MovieDetail', params: {movieId: pk}})
      },
      scrollLeft() {
        const width = document.getElementById('most-favorite-box').clientWidth
        document.getElementById('most-favorite-box').scrollLeft -= width;
      },
      scrollRight() {
        const width = document.getElementById('most-favorite-box').clientWidth
        document.getElementById('most-favorite-box').scrollLeft += width;
      }
    }
  }
  </script>
  
  <style>
  .poster-container {
   overflow-x: auto;
   scroll-behavior: smooth;
  }
  
  .poster-container::-webkit-scrollbar {
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