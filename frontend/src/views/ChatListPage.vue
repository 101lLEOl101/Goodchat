<template>
  <div class="chat_box">
    <router-link to="/multychatcreate" class="create_chat"><i class="fa-solid fa-comment-medical create"></i></router-link>
    <h2 style="text-align:center;"> Personal Chats </h2>
    <chat-list v-if="chats.length != 0" :chats="chats" />
    <div v-else class="chat_item">
      <div class="chat_texts" style="margin: auto;">
        You don't have any chat yet :c
      </div>
    </div>
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
  },
  mounted() {
    if (document.getElementsByClassName("now-side_icon").length != 0) {
      let icon = document.getElementsByClassName("now-side_icon")[0];
      let icona = document.getElementsByClassName("now-icona")[0];
      icona.classList.remove("now-icona");
      icon.classList.remove("now-side_icon");
      icona.classList.add("icona");
      icon.classList.add("side_icon");
    }
    document.getElementById("mes").classList.add("now-side_icon");
    document.getElementById("mes").classList.remove("side_icon");
    document.getElementById("mes").childNodes[0].childNodes[0].classList.add("now-icona");
    document.getElementById("mes").childNodes[0].childNodes[0].classList.remove("icona");
    document.title = "chat-list";
  },
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
 