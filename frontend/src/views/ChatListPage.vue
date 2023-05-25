<template>
  <div class="chat_box">
    <a href="" class="create_chat"><i class="fa-solid fa-comment-medical create"></i></a>
    <h2 style="text-align:center;"> Personal Chats </h2>
    <chat-list :chats="chats" />
  </div>
</template>
 
<script>
import ChatList from '@/components/chat/ChatList'

export default {
  components: {
    ChatList,
  },
  data() {
    return {
      chats: [],
    }
  },
  methods: {
    loadChats() {
      this.$store.dispatch('chat/getChatlist').then(
        response => this.chats = response
      );
    }
  },
  created() {
    this.loadChats();
    this.interval = setInterval(this.loadChats, 1.5 * 1000);
  },
  beforeUnmount() {
    clearInterval(this.interval);
  }
}
</script>
 
<style>
.chat_box {
  background-color: rgba(0, 0, 0, 60%);
  width: 800px;
  min-height: 100vh;
  margin: 0 auto;
  color: white;
  padding-top: calc(7vh + 5px);
  border-radius: 50px;
  box-shadow: 0px 0px 33px #8270F2;
}

.create {
  color: white;
  font-size: 200%;
  border: #8270F2 solid 2px;
  padding: 10px;
  margin: 10px;
  margin-bottom: 0px;
  border-radius: 200px;
  transition: 0.5s;
}

.create_chat {
  position: relative;
  left: 90%;
}

.create:hover {
  color: black;
  background-color: white;
  transition: 0.5s;
}
</style>
 