<template>
  <post-card :post="post"/>
</template>

<script>
import PostCard from '@/components/post/PostCard';

export default {
  components: {
    PostCard,
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