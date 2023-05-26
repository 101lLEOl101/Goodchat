<template>
  <friend-item 
    v-for="friend in friends" 
    :key="friend.id" 
    :friend="friend"
    :IsFriend=IsFriends
    @deleteFriend="deleteFriend"
    @acceptFriendRequest="acceptFriendRequest"
    @declineFriendRequest="declineFriendRequest"/>
</template>

<script>
import FriendItem from '@/components/friendlist/FriendItem.vue'

export default {
  components: {
    FriendItem,
  },
  props: {
    friends: Array,
    IsFriends: Boolean,
  },
  methods: {
    deleteFriend(friend_id) {
      this.$emit('deleteFriend', friend_id);
    },
    acceptFriendRequest(friend_id) {
      this.$emit('acceptFriendRequest', friend_id);
    },
    declineFriendRequest(friend_id) {
      this.$emit('declineFriendRequest', friend_id);
    },
  }
}
</script>

<style></style>