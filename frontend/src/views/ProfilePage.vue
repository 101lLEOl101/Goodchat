<template>
  <input type="checkbox" id="toggle">
  <div class="profile_page">
    <post-feed v-if="posts" :posts="posts" :isTemplate="true" />
    <div v-else-if="userIsMe" class="zero_bookmarks">
      <p class="alarm_posts">This user has no posts :c</p>
    </div>
    <div v-else class="zero_bookmarks">
      <p class="alarm_posts">You don't have any posts yet :c</p>
      <router-link to="/addpost" class="btn_add">Add Post</router-link>
    </div>
  </div>

  <profile-card v-if="user" :user="user" :userIsMe="userIsMe" />
</template>

<script>
import ProfileCard from '@/components/cards/ProfileCard';
import PostFeed from '@/components/post/PostFeed.vue';

export default {
  components: {
    ProfileCard,
    PostFeed,
  },
  props: ['id'],
  data() {
    return {
      user: {},
      userIsMe: false,
      posts: []
    }
  },
  methods: {
    async loadUserData() {
      let userId = this.$route.params.id;
      await this.$store.dispatch('user/getUser', { id: userId })
        .then(
          response => {
            this.user = response;
          }
        )
        .catch(
          reason => {
            this.$router.push(`/profilenotfound`);
            console.log(reason);
          }
        )
      //console.log(this.user)
      this.$store.dispatch('user/isUserSelf', { id: this.user.id })
        .then(
          response => this.userIsMe = response,
          error => console.log(error)
        );
      this.$store.dispatch('post/getUserPosts', { id: this.id })
        .then(response => this.posts = response);
    },
  },
  created() {
    this.loadUserData();
  },
  watch: {
    id() {
      this.loadUserData();
    }
  }
}
</script>

<style>
.btn_profile {
  background-color: #000000;
  border-radius: 12px;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #8270F2;
  width: 50%;
  font-size: 20px;
  transition: all 0.5s;
  margin: 10px 20%;
  display: inline-block;
  text-align: center;
  transition: all 1s;
}

.btn_profile:hover {
  background-color: #000000;
  border-radius: 12px;
  border: #000000 solid 2px;
  box-shadow: 0px 0px 33px #8270F2;
}

.profile_page {
  width: 85%;
  border-radius: 5px;
  margin-top: 7vh;
  margin-bottom: 50px;
  margin-left: 0;
  transition: all 1s;
}

#toggle {
  appearance: none;
}

#toggle:checked~.profile-card {
  transition: all 1s;
  width: 35%;
}

#toggle:checked~.profile_page {
  transition: all 1s;
  width: 70%;
}

.zero_bookmarks {
  background-color: black;
  width: 200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0px 0px 25px #8270F2;

}

.alarm_posts {
  color: white;
}

.btn_posts {
  color: white;
}

.btn_add {
  background-color: #000000;
  border-radius: 12px;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #8270F2;
  width: 100%;
  font-size: 20px;
  transition: all 0.7s;
  cursor: pointer;
  font-weight: bold;
  text-align: center;
}

.btn_add:hover {
  background: linear-gradient(to top left, #9f49ff, #19087d);
  border-radius: 12px;
  color: white;
  font-weight: bold;
}

#toggle:checked~.profile-card>.user-nickname {
  transition: all 1s;
  width: 30%;
}

#toggle:checked~.profile-card>.user-info {
  transition: all 1s;
  width: 35%;
  right: 0;
  top: 55%;
  position: absolute;
}

#toggle:checked~.profile-card>.profile-pic {
  width: 30%;
  margin: 0 35%;
  border-radius: 100%;
  box-shadow: 0px 0px 30px #8270f2;
  transition: all 1s;
}

.hiddenunckecked {
  overflow: hidden;
  margin: 0 15%;
  padding: 0;
  font-size: 0;
  transition: all 1s;
}

.unhidden {
  transition: all 1s;
  overflow: hidden;
}

#toggle:checked~.profile-card .hiddenunckecked {
  width: 70%;
  margin: 10px 15%;
  padding: 15px 0;
  font-size: 100%;
}

#toggle:checked~.profile-card .user-info {
  height: 85%;
}

#toggle:checked~.profile-card .top {
  margin-bottom: 5px;
}

#toggle:checked~.profile-card .bottom {
  margin-top: 5px;
}


#toggle:checked~.profile-card .unhidden {
  height: 0;
  margin: 0 15%;
  padding: 0;
  font-size: 0;
}

.left {
  width: 100%;
  transition: all 1s;
}

.right {
  overflow: hidden;
  width: 0%;
  transition: all 1s;
}

#toggle:checked~.profile-card .left,
#toggle:checked~.profile-card .right {
  width: 50%;
}

.row {
  display: flex;
}
</style>