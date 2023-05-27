<template>
  <div class="post-feed">
    <post-card @addDeleteBookmark="addDeleteBookmark"
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
  },
  methods: {
    addDeleteBookmark(id) {
      this.$emit('addDeleteBookmark', id);
    }
  }
}
</script>
<style>

</style>