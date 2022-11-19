<template>
  <div class="margin-by-fixed">
    <div class="detail-nav" :style="{ backgroundImage : `url(https://www.themoviedb.org/t/p/w1920_and_h800_multi_faces${this.moviedata?.backdrop_path})`}">
      <div class="detail-nav-box d-flex">
        <img :src="imgurl + moviedata?.poster_path" alt="" v-if="moviedata" class="col-3 m-3">
        <div>
          <p><span>{{ moviedata?.title }}</span><span> ({{ releaseYear }})</span></p>
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
    <label for="comment">댓글: </label>
    <input type="text" v-model="comment">
    <button @click="inputComment">작성</button>
    <CommentList :movieid="movie_id"/>
  </div>
</template>
<script>
import axios from 'axios'
import CommentList from '@/components/CommentList.vue'

export default {
    name: 'MovieDetail',
    data() {
        return {
            movie_id: Number(this.$route.params.movieId),
            comment: null,
            moviedata: null,
            imgurl: 'https://image.tmdb.org/t/p/original',
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
          console.log(res.data)
            this.moviedata = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    methods: {
      inputComment() {
        const token = localStorage.getItem('accessToken')
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
          console.log('댓글작성 성공')
        })
        .catch(err => {
          console.log(err)
        })
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
</style>