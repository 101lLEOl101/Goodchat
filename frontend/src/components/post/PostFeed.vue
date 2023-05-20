<template>
  <div class="post-feed">
    <post-card 
      v-for="post in posts"
      :key="post.id" 
      :post="post"
      :isTemplate="isTemplate"
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
    isTemplate: Boolean,
  }
}
</script>
<style>

</style>