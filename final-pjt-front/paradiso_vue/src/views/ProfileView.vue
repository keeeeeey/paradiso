<template>
  <div>
    <h1>Profile 입니다.</h1>
    {{ nickname }}
    {{ totaldata }}
  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'ProfileView',
    data() {
      return {
        nickname: String(this.$route.params.nickname),
        totaldata: null,
      }
    },
    created() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/profile/${this.nickname}/`
      })
      .then(res => {
        this.totaldata = res.data
      })
    }
}
</script>

<style>

</style>