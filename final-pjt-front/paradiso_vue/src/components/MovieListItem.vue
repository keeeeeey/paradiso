<template>
  <div>
    <p>제목: {{ movie.title }}</p>
    <p>ID: {{ movie.id }}</p>
  </div>
</template>

<script>
export default {
    name: 'MovieListItem',
    props: {
      movie: Object,
    }
}
</script>

<style>

</style>