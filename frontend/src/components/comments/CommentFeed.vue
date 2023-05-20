<template>
<h1 style="text-align:center; color:white;"> Comments </h1>
<comment-card /> 
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
<style>

</style>