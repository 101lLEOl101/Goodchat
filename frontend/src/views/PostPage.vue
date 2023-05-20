<template>
  <post-card-page :post="post"/>
</template>

<script>
import PostCardPage from '@/components/post/PostCardPage';

export default {
  components: {
    PostCardPage,
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
      }
    }
  },
  mounted() {
    this.$store.dispatch('post/getPost', {id: this.id})
      .then(
        response => {
          this.post = response;
        }
      );
  }

}
</script>