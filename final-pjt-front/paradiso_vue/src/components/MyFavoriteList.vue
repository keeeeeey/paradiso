<template>
  <div class="margin-by-fixed" style="position: relative">
    <h2 class="ms-3 mb-4">좋아할만한 영화</h2>
    <div
      v-if="myFavorites"
      class="d-flex poster-container pe-2"
      id="my-favorite-box"
    >
      <div
        v-for="myFavorite in myFavorites"
        :key="myFavorite.id"
        class="col-2"
        id="my-favorite-item"
      >
        <MyFavoriteListItem
          :myFavorite="myFavorite"
          @click.native="goToMovie(myFavorite.id)"
          style="cursor: pointer"
        />
      </div>
    </div>
    <i
      class="fa-solid fa-chevron-left fa-2x arrow-left"
      @click="scrollLeft"
    ></i>
    <i
      class="fa-solid fa-chevron-right fa-2x arrow-right"
      @click="scrollRight"
    ></i>
  </div>
</template>
  
  <script>
import MyFavoriteListItem from "@/components/MyFavoriteListItem";
import axios from "axios";
const token = localStorage.getItem("accessToken");

export default {
  name: "MyFavoriteList",
  components: {
    MyFavoriteListItem,
  },
  data() {
    return {
      myFavorites: null,
    };
  },
  created() {
    if (token) {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/accounts/userfavorites/",
        headers: { Authorization: `Bearer ${token}` },
      })
        .then((res) => {
          this.myFavorites = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
  methods: {
    goToMovie(pk) {
      this.$router.push({ name: "MovieDetail", params: { movieId: pk } });
    },
    scrollLeft() {
      const width = document.getElementById("my-favorite-box").clientWidth;
      document.getElementById("my-favorite-box").scrollLeft -= width;
    },
    scrollRight() {
      const width = document.getElementById("my-favorite-box").clientWidth;
      document.getElementById("my-favorite-box").scrollLeft += width;
    },
  },
};
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