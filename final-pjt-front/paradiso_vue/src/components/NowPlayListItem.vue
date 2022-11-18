<template>
  <div>
    {{ playmovie.title }}
  </div>
</template>

<script>
export default {
  name: 'NowPlayListItem',
  props: {
    playmovie: Object,
  }
}
</script>

<style>

</style>