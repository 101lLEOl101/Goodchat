<template>
  <div class="friendlist_item">
    <img :src="member.avatar" class="friend-avatar">
    <router-link class="friend_name" :to="`/profile/${member.id}`">{{ member.name }} {{ member.surname }}</router-link>
    <span class="friend_name">{{ member.access_description }}</span>
  </div>
</template>

<script>
export default {
  props: {
    member: Object,
  }
}
</script>

<style>
.friendlist_item {
  display: flex;
  justify-content: start;
  align-items: center;
  width: 98%;
  background-color: black;
  border: 1px solid #8270F2;
  padding: 10px;
  border-radius: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  box-shadow: 0px 0px 5px #8270F2;
}

.friend_name {
  color: white;
  width: 20%;
  text-align: center;
}

.friend-avatar {
  margin-left: 2%;
  width: 10%;
  border-radius: 100%;
  object-fit: cover;
  aspect-ratio: 1/1;
}
</style>