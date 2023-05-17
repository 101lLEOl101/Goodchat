<template>
    <div class = "main_page">
        <div class = "main_page_post">
            <PostTemplate />
        </div>
</div>
  </template>
  
  <script>
  import PostTemplate from '@/components/post/PostTemplate.vue';
  
  export default {
    components: {
      PostTemplate
    },
    data() {
      return {
        message: {},
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