<template>
    <div>
       <chat-item 
       v-for="chat in chats" 
       :key="chat.id"
       :chat = "chat"
       />
   </div>
 </template>
 
 <script>
 import ChatItem from '@/components/chat/ChatsItem.vue'

 export default {
  components: {
    ChatItem
  },
  props:{
    chats: Array,
  }
}
 </script>
 
 <style>
 
 </style>
 