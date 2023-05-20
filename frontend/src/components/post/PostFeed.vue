<template>
  <div class="post-feed">
    <post-card 
      v-for="post in posts"
      :key="post.id" 
      :post="post"
    />
  </div>
</template>
<script>
import PostCard from '@/components/post/PostCard';

export default {
  components: {
    PostCard,
  },
  props: {
    posts: Array,
  }
}
</script>
<style>

</style>