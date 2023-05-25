<template>
  <friend-item 
    v-for="friend in friends" 
    :key="friend.id" 
    :friend="friend"
    :isFriend="isFriends"
    @deleteFriend="deleteFriend"/>
</template>

<script>
import FriendItem from '@/components/friendlist/FriendItem.vue'

export default {
  components: {
    FriendItem,
  },
  props: {
    friends: Array,
    isFriends: Boolean,
  },
  methods: {
    deleteFriend(friend_id) {
      this.$store.dispatch('friend/refuseFriendship', {friend_id: friend_id})
    } 
  }
}
</script>

<style></style>