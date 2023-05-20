<template>
  <div class="main_page">
    <post-feed :posts="posts"/>
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
      posts: [
        {
          id: 1,
          content: 'FFKFJFLJJDJLFJLSDF LD JScontent',
          photo: '0000',
          isBookmark: true,
          author: {
            name: 'Egor',
            surname: 'Nazaikin',
            photo: '9328535',
          }
        },
        {
          id: 2,
          content: 'FFKFJFLJJDJLFJLSDF LD JScontent',
          photo: '0000',
          isBookmark: true,
          author: {
            name: 'Egor',
            surname: 'Nazaikin',
            photo: '9328535',
          }
        },
        {
          id: 3,
          content: 'FFKFJFLJJDJLFJLSDF LD JScontent',
          photo: '0000',
          isBookmark: true,
          author: {
            name: 'Egor',
            surname: 'Nazaikin',
            photo: '9328535',
          }
        },
      ]
    }
  },

}
</script>
  
<style>
.reg-header {
  color: white;
  text-align: center;

}

.reg_box {
  display: flex;
  margin-top: 50px;
  align-items: center;
  justify-content: center;
  position: fixed;
  transform: translate(-50%, -50%) scale(0.9);
  left: 50%;
  top: 50%;
}

.auth-link {
  text-decoration: none;
  color: #8270F2;
  margin-top: 10px;
  font-size: 13px;
  text-shadow:
    -0 -1px 6px #000000,
    0 -1px 6px #000000,
    -0 1px 6px #000000,
    0 1px 6px #000000,
    -1px -0 6px #000000,
    1px -0 6px #000000,
    -1px 0 6px #000000,
    1px 0 6px #000000,
    -1px -1px 6px #000000,
    1px -1px 6px #000000,
    -1px 1px 6px #000000,
    1px 1px 6px #000000,
    -1px -1px 6px #000000,
    1px -1px 6px #000000,
    -1px 1px 6px #000000,
    1px 1px 6px #000000;
}
</style>