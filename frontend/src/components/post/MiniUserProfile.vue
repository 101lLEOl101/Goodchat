<template>
    <img class="author_avatar" :src="user.avatar">
    <router-link 
      :to="`/profile/${user.id}`" 
      class="post-author">
      {{ user.name }} {{ user.surname }}
    </router-link>
</template>
<script>
export default {
  data() {
    return {}
  },
  props: {
    user: Object,
  }

}
</script>
<style>
.post-author {
  color: white;
  margin-right: 4%;
  cursor: pointer;
  text-decoration: none;
}

.author_avatar {
  margin: 5.125px 30px;
  aspect-ratio: 1/1;
  object-fit: cover;
  height: 40px;
  width: 40px;
  border-radius: 100%;
  margin-left: auto;
}
</style>