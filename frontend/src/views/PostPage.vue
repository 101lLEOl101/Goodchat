<template>
    <post-card :post="post" :isTemplate="false" > 
      <template #comments>
        <comment-form />
        <comment-feed :comments="comments" />
      </template>
    </post-card>
</template>

<script>
import PostCard from '@/components/post/PostCard';
import CommentForm from '@/components/comments/CommentForm.vue';
import CommentFeed from '@/components/comments/CommentFeed.vue';

export default {
  components: {
    PostCard,
    CommentForm,
    CommentFeed,
  },
  props: ['id'],
  data() {
    return {
      post: {
        id: 0,
        content: '',
        author: {
          id: '',
          name: '',
          surname: '',
        },
        photo: '',
      },
      comments: [],
    }
  },
  async mounted() {
    await this.$store.dispatch('post/getPost', {id: this.id})
      .then(
        response => this.post = response
      );

    this.$store.dispatch('comment/getComments', {post_id: this.post.id})
      .then(
        response => this.comments = response
      )
  }

}
</script>
<style>
</style>