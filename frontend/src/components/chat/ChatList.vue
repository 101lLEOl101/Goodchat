<template>
  <div>
    <chat-list-item 
      v-for="chat in chats" 
      :key="chat.id" 
      :chat="chat" 
    />
  </div>
</template>
 
<script>
import ChatListItem from '@/components/chat/ChatListItem.vue'

export default {
  components: {
    ChatListItem
  },
  props: {
    chats: Array,
  }
}
</script>
 
<style></style>
 