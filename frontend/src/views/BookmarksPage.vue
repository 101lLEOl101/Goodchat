<template>
  <div class="main_page">
    <post-feed @addDeleteBookmark="addDeleteBookmark" v-if="posts.length!=0" :posts="posts" :isTemplate="true"/>
    <div v-else class="zero_bookmarks">
      <p class="alarm_posts">You don't have any bookmark posts yet :c</p>
      <router-link to="/feed" class="btn_add">Add Bookmark Post</router-link>
    </div>
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
      posts: []
    }
  },
  methods: {
    addDeleteBookmark(id) {
      this.$store.dispatch('post/addDeleteBookmark', {id: id}).then(
        response => {
          let idx = this.posts.indexOf(this.posts.find(post => post.id == id));
          console.log(idx);
          this.posts[idx].isBookmark = response;
        }
      )
    },
  },
  mounted() {
    if(document.getElementsByClassName("now-side_icon").length != 0){
      let icon = document.getElementsByClassName("now-side_icon")[0];
      let icona = document.getElementsByClassName("now-icona")[0];
      icona.classList.remove("now-icona");
      icon.classList.remove("now-side_icon");
      icona.classList.add("icona");
      icon.classList.add("side_icon");
    }
    document.getElementById("book").classList.add("now-side_icon");
    document.getElementById("book").classList.remove("side_icon");
    document.getElementById("book").childNodes[0].childNodes[0].classList.add("now-icona");
    document.getElementById("book").childNodes[0].childNodes[0].classList.remove("icona");
    document.title = "bookmark";
  },
  created() {
    this.$store.dispatch('post/getBookmarks').then(
      posts => this.posts = posts
    )
  }
}
</script>
  
<style>
.main_page{
    margin: auto;
    margin-top: 7vh;
    margin-bottom: 50px;
}
</style>