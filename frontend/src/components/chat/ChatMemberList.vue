<template>
  <div>
    <chat-member-item 
      v-for="member in members" 
      :key="member.id" 
      :member="member" />
  </div>
</template>


<script>
import ChatMemberItem from '@/components/chat/ChatMemberItem';

export default {
  components: {
    ChatMemberItem,
  },
  props: {
    members: Array,
  }
}
</script>