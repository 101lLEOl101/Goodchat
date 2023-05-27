<template>
  <div v-bind:class="{ 'post-margin post-box': !isTemplate, 'post-box': isTemplate }">
    <div class="post-header">
      <div class="btn_box_post">
        <router-link v-if=isTemplate :to="`/post/${post.id}`" class="round open" title="Open Full">
          <div class="arrow"></div>
          <div class="arrow_diff"></div>
        </router-link>
        <button @click="addDeleteBookmark" v-if=isTemplate to="/bookmarks" class="round"
          :class="{ in_zakladka: post.isBookmark, zakladka: !post.isBookmark }" title="Bookmark" />
        <router-link v-if="!isTemplate && post.author.id == this.$store.getters['auth/user'].id" :to="`/editpost/${post.id}`" class="round edit" title="Edit" />
        <button @click="deletePost" v-if="!isTemplate && post.author.id == this.$store.getters['auth/user'].id" class="round delete" title="Delete" />
      </div>
      <mini-user-profile :user="post.author" />
    </div>
    <div class="text-wrap">
      <div class="post-text">{{ post.content }}</div>
    </div>
    <img v-if="post.photo" :src="post.photo" class="post-image">
    <slot name="comments"></slot>
  </div>
</template>
<script>
import MiniUserProfile from '@/components/post/MiniUserProfile.vue';

export default {
  components: {
    MiniUserProfile,
  },
  data() {
    return {}
  },
  props: {
    post: Object,
    isTemplate: Boolean
  },
  methods: {
    deletePost() {
      this.$store.dispatch('post/deletePost', {id: this.post.id}).then(
        _ => this.$router.push(`/profile/${this.$store.getters['auth/user'].id}`)
      )
    },
    addDeleteBookmark() {
      this.$emit('addDeleteBookmark', this.post.id)
    },
  }
}
</script>
<style>
.edit {
  background-color: #36C849;
}

.delete {
  background-color: #FD5754;
}

.delete:hover {
  background-image: url("@/assets/trash.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-size: 14px 14px;
}

.edit:hover {
  background-image: url("@/assets/pencil.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-size: 28px 28px;
}

.round {
  width: 22px;
  height: 22px;
  border-radius: 100%;
  margin-right: 10px;
  margin-left: 10px;
}

.heart {
  background-color: #FD5754;
}

.zakladka {
  background-color: #36C849;
}

.in_zakladka {
  background-color: #36C849;
  background-image: url("@/assets/bookmark.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-size: 14px 14px;
}


.in_zakladka:hover {
  background-image: none;
}

.open {
  background-color: #FEBB40;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.5s;
}

.heart:hover {
  background-color: #FD5754;
  background-image: url("@/assets/heart.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-size: 14px 14px;
}

.zakladka:hover {
  background-image: url("@/assets/bookmark.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  background-size: 14px 14px;
}

.open:hover .arrow_diff {
  background-color: #FEBB40;
  display: block;
}

.open:hover .arrow {
  background-color: #FEBB40;
  display: block;
}

.btn_box_post {
  display: flex;
  width: 130px;
  margin-left: 2%;
}

.arrow {
  display: none;
  width: 4px;
  height: 4px;
  border-top: 4px solid black;
  border-right: 4px solid black;
  position: relative;
  left: 6px;
  bottom: 3px;
}

.arrow_diff {
  display: none;
  width: 4px;
  height: 4px;
  border-top: 4px solid black;
  border-right: 4px solid black;
  position: relative;
  right: 6px;
  top: 3px;
  transform: rotate(180deg);
}

.post-box {
  background: rgba(0, 0, 0, 0.75);
  border-radius: 37px;
  overflow: hidden;
  width: 65%;
  margin-top: 2%;
  margin-right: auto;
  margin-left: auto;
  box-shadow: 0px 10px 10px #8270f2;
}

.post-margin {
  margin-top: 9vh;
}

.post-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(0, 0, 0, 0.75);
  border-bottom: solid 3px #8270F2;
  border-radius: 37px 37px 0px 0px;
}

.text-wrap {
  display: inline-flex;
  justify-content: space-between;
  margin-top: 2%;
  width: 100%;
  margin-bottom: 2%;
  word-wrap: break-word;
  -webkit-hyphens: auto;
  -moz-hyphens: auto;
  -ms-hyphens: auto;
}

.post-text {
  background: black;
  border: solid 1px white;
  color: white;
  width: 90%;
  border-radius: 14px;
  margin-left: 3%;
  padding: 2%;
  white-space: pre-wrap;
}

.post-image {
  max-width: 90%;
  margin-left: 5%;
  border: solid 1px white;
  border-radius: 27px;
  margin-bottom: 4%;
}

.text-wrap {
  display: inline-flex;
  justify-content: space-between;
  margin-top: 2%;
  width: 100%;
  margin-bottom: 2%;
}

.post-bookmark {
  color: white;
  font-size: 40px;
  margin: 5px;
}

.img-marks {
  background-image: url("https://cdn-icons-png.flaticon.com/512/58/58516.png");
  width: 38px;
  height: 38px;
  background-size: contain;
  background-repeat: no-repeat;
  margin-top: 18px;
  cursor: pointer;
}

.post-text {
  background: black;
  border: solid 1px white;
  color: white;
  width: 90%;
  border-radius: 14px;
  margin-left: 3%;
  padding: 2%;
}

.zero_bookmarks {
  background-color: black;
  width: 250px;
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
</style>