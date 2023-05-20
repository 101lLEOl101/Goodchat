<template>
  <div class="main_page">
    <post-feed :posts="posts" :isTemplate="true"/>
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
  }
}
</script>
  
<style>
.main_page{
    margin: auto;
    margin-top: 7vh;
    margin-bottom: 50px;
}
</style>