<template>
  <div class="container404">
    <h1>404: Not found</h1>
  </div>
</template>

<script>
export default {
  mounted() {
    if (document.getElementsByClassName("now-side_icon").length != 0) {
      let icon = document.getElementsByClassName("now-side_icon")[0];
      let icona = document.getElementsByClassName("now-icona")[0];
      icona.classList.remove("now-icona");
      icon.classList.remove("now-side_icon");
      icona.classList.add("icona");
      icon.classList.add("side_icon");
    }
    document.title = "404";
  },
}
</script>

<style scoped>
.container404 {
  width: 100%;
  text-align: center;
  padding: 10rem;
  margin: auto;
}

h1 {
  color: pink;
}
</style>