<template>
  <div class="friendlist_item" id="friend_item">
    <img :src="friend.avatar" class="friend-avatar image_avatar">
    <router-link class="friend_name" :to="`/profile/${friend.id}`">{{ friend.name }} {{ friend.surname }}</router-link>
    <button @click="this.$emit('deleteFriend', friend.id)" v-if=IsFriend type="button" class="button_write accept">Delete</button>
    <dialog-button v-if=IsFriend class="button_write accept" :id="friend.id" />
    <button @click="$emit('acceptFriendRequest', friend.id)" v-if=!IsFriend type="button" class="button_write accept" >Accept</button>
    <button @click="$emit('declineFriendRequest', friend.id)" v-if=!IsFriend type="button" class="button_write accept" >Decline</button>
  </div>
</template>

<script>
import DialogButton from '@/components/chat/DialogButton.vue';

export default {
  components: {
    DialogButton,
  },
  props: {
    friend: Object,
    IsFriend: Boolean,
  },
  methods: {
    deleteFriend() {
      this.$emit('deleteFriend', this.friend.id);
    }
  },
}
</script>

<style>
.button_write {
  display: block;
  padding: 10px;
  border-radius: 5px;
  background-color: black;
  border: solid 1px #8270F2;
  color: #8270F2;
  text-align: center;
  box-shadow: 0px 0px 10px #8270F2;
  transition: all 0.3s;
  position: relative;
  left: 40%;
}

.button_write:hover {
  box-shadow: 0px 0px 40px #8270F2;
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

.accept {
  left: 44%;
}

.reject {
  left: 45%;
}
</style>