<template>
  <h1 v-if="comments.length > 0" style="text-align:center; color:white;"> Comments </h1>
  <comment-card
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"
    />
</template>
<script>
import CommentCard from '@/components/comments/CommentCard.vue';

export default {
  components: {
    CommentCard,
  },
  props: {
    comments: Array,
  }
}
</script>
<style></style>