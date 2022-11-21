<template>
  <div class="margin-by-fixed">
    <div class="detail-nav" :style="{ backgroundImage : `url(https://www.themoviedb.org/t/p/w1920_and_h800_multi_faces${this.moviedata?.backdrop_path})`}" v-if="moviedata">
      <div class="detail-nav-box d-flex">
        <div class="col-3 p-3">
          <img :src="imgurl + moviedata?.poster_path" alt="" v-if="moviedata" class="w-100 mb-3" @onmouseover="play-video">
          <!-- Button trigger modal -->
          <button type="button" class="play-btn w-100" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="turnOn">
            예고편
          </button>
        </div>
        <div class="mt-3 me-3 mb-3">
          <p>
            <span>{{ moviedata?.title }}</span>
            <span> ({{ releaseYear }})</span>
            <i @click="movieLike" v-show="!isliked" class="fa-regular fa-heart m-1"></i>
            <i @click="movieLike" v-show="isliked" class="fa-solid fa-heart m-1" style="color: red"></i>
            <span> {{ like_count }}</span>
          </p>
          <p>{{ releaseYear }}/{{ releaseMonth }}/{{ releaseDay }} ● {{ genreList }} ● {{ runtimeHour }}h {{ runtimeMinute }}m</p>
          점수 
          <div class="progress w-75">
            <div class="progress-bar" :style="{ width : `${voteAverage}%`}" role="progressbar" aria-label="Basic example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" id="progressbar-fill-color">{{ voteAverage }}%</div>
            </div><br>
          <p>"{{ moviedata?.tagline }}"</p>
          <div>줄거리</div>
          <p>{{ moviedata?.overview }}</p>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-center my-5 align-items-center">
      <div class="input-group flex-nowrap w-75">
        <span class="input-group-text" id="addon-wrapping">댓글</span>
        <input v-model="comment" type="text" class="form-control">
        <button @click="inputComment" class="input-group-text" id="addon-wrapping">등록하기</button>
      </div>
    </div>
    <CommentList :movieid="movie_id" :key="componenetRerender" @updatecomment="updateComment"/>

    <!-- Modal -->
    <div class="modal fade modal-lg" style="margin-top: 100px;" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <span style="font-size: large"><b>{{ moviedata.title }} 예고편</b></span>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="turnOff"></button>
          </div>
          <div class="modal-body modal-box">
            <iframe
                v-if="isTurn"
                id="youtube-player" 
                type="text/html"
                width="100%"
                height="100%"
                :src="videourl + videodata?.results[0].key + '?mute=1&autoplay=1'" 
                frameborder="0"
                allowfullscreen="allowfullscreen"
            >
            </iframe>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import CommentList from '@/components/CommentList.vue'
const token = localStorage.getItem('accessToken')

export default {
    name: 'MovieDetail',
    data() {
        return {
            movie_id: Number(this.$route.params.movieId),
            comment: null,
            moviedata: null,
            imgurl: 'https://image.tmdb.org/t/p/original',
            componenetRerender: 0,
            isliked: false,
            like_count: 0,
            videodata: null,
            videourl: "https://www.youtube-nocookie.com/embed/",
            isTurn: false,
        }
    },
    computed: {
      releaseYear() {
        return this.moviedata?.release_date.slice(0, 4)
      },
      releaseMonth() {
        return this.moviedata?.release_date.slice(5, 7)
      },
      releaseDay() {
        return this.moviedata?.release_date.slice(8)
      },
      voteAverage() {
        return (Number(this.moviedata?.vote_average) * 10).toFixed(2)
      },
      genreList() {
        let result = ''
        if (this.moviedata?.genres) {
          for (const genre of this.moviedata?.genres) {
          result = result + genre.name + ', '
          }
        }
        return result.slice(0, -2)
      },
      runtimeHour() {
        return parseInt(this.moviedata?.runtime/60)
      },
      runtimeMinute() {
        return this.moviedata?.runtime%60
      }
    },
    components: {
      CommentList,
    },
    created() {
      axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/movie/${this.movie_id}?api_key=9adec2ecce07845598e041a9836861b2&language=ko-KR`
      })
      .then(res => {
        this.moviedata = res.data
      })
      .catch(err => {
        console.log(err)
      })

      if (token) {
        axios({
          method: "get",
          url: `http://127.0.0.1:8000/accounts/${this.movie_id}/movies/islike/`,
          headers: {'Authorization': `Bearer ${token}`},
        })
          .then((res) => {
            this.isliked = res.data.is_liked
            this.like_count = res.data.like_count
          })
          .catch((err) => {
            console.log(err)
          })
      }

      axios({
          method: "get",
          url: `https://api.themoviedb.org/3/movie/${this.movie_id}/videos?api_key=fc9c1f07b9650d1ec4f98fb39efa792e&language=ko-KR`
        })
          .then((res) => {
            this.videodata = res.data
            console.log(this.videodata.results)
          })
    },
    methods: {
      movieLike() {
        if (token) {
          axios({
            method: "post",
            url: `http://127.0.0.1:8000/movies/${this.movie_id}/likes/`,
            headers: {'Authorization': `Bearer ${token}`},
          })
            .then((res) => {
              this.isliked = res.data.is_liked
              this.like_count = res.data.like_users_count
            })
            .catch((err) => {
              console.log(err)
            })
        } else {
          alert('로그인이 필요합니다.')
          this.$router.push({ name: 'LogInView' })
        }
        
      },
      inputComment() {
        if (token) {
          axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/${this.movie_id}/comments/`,
          data: {
            content: this.comment,
            movie_id: this.movie_id,
          },
          headers: {'Authorization': `Bearer ${token}`},
          })
          .then(() => {
            this.componenetRerender += 1
            this.comment = null
          })
          .catch(err => {
            console.log(err)
          })
        } else {
          alert('로그인이 필요합니다.')
          this.$router.push({ name: 'LogInView' })
        }
        
      },

      updateComment() {
        this.componenetRerender += 1
      },

      turnOn() {
        this.isTurn = true
      },

      turnOff() {
        this.isTurn = false
      }
    }
}
</script>

<style>
#progressbar-fill-color{
  background: linear-gradient(90deg, rgba(190,46,221,1) 0%, rgba(255,82,121,1) 41%, rgba(255,201,77,1) 100%);
}

.detail-nav{
  color: white;
}

.detail-nav-box{
  background-image: linear-gradient(to right, rgba(31.5, 31.5, 31.5, 1) 150px, rgba(31.5, 31.5, 31.5, 0.84) 100%);
}

.play-btn {
  color: white;
  font-weight: bold;
  /* width: 75px; */
  height: 40px;
  background-color: rgb(31, 135, 195);
  border: solid 1px rgb(31, 135, 195);
  border-radius: 5px;
}

.modal-box {
  width: 100%;
  aspect-ratio: 16 / 9;
}
</style>