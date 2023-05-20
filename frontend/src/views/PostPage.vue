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
          this.post.comments = [
          {
            id: 1,
            author: 'vafin',
            content: 'foffofofoofof',
            date: '2134325',
          },
          {
            id: 2,
            author: 'vafin',
            content: 'fof325325fof',
            date: '2134s325',
          },
          {
            id: 3,
            author: 'vafas23in',
            content: '325090923jfksdkvnsdfofofoofof',
            date: '213asd4325',
          }
        ]
        }
      );
  }

}
</script>