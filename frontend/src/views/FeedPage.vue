<template>
  <div class="main_page">
    <post-feed :posts="posts" :isTemplate="true" />
  </div>
</template>
  
<script>
import PostFeed from '@/components/post/PostFeed';

export default {
  components: {
    PostFeed,
  },
  data() {
    return {
      message: {},
      posts: []
    }
  },
  created() {
    this.$store.dispatch('post/getFeed').then(
      posts => this.posts = posts
    )
  },
  mounted() {
    if (document.getElementsByClassName("now-side_icon").length != 0) {
      let icon = document.getElementsByClassName("now-side_icon")[0];
      let icona = document.getElementsByClassName("now-icona")[0];
      icona.classList.remove("now-icona");
      icon.classList.remove("now-side_icon");
      icona.classList.add("icona");
      icon.classList.add("side_icon");
    }
    document.getElementById("glob").classList.add("now-side_icon");
    document.getElementById("glob").classList.remove("side_icon");
    document.getElementById("glob").childNodes[0].childNodes[0].classList.add("now-icona");
    document.getElementById("glob").childNodes[0].childNodes[0].classList.remove("icona");
  },
}
</script>
  
<style>
.main_page {
  margin: auto;
  margin-top: 7vh;
  margin-bottom: 50px;
}
</style>