<template>
  <div class="messenger_box" id="messenger_box">
    <h2 style="text-align:center;"> messages </h2>
    <chat-header :info="chat.info" />
    <message-container :messages="chat.messages" />
    <message-form @send="send" />
  </div>
</template>
  
<script>
import ChatHeader from '@/components/chat/ChatHeader';
import MessageContainer from '@/components/chat/MessageContainer';
import MessageForm from '@/components/chat/MessageForm';

export default {
  components: {
    ChatHeader,
    MessageContainer,
    MessageForm
  },
  data() {
    return {
      chat: {
        info: {},
        messages: [],
      },
    }
  },
  props: ['id'],
  methods: {
    send(content) {
      this.$store.dispatch('chat/sendMessage', {
        chat_id: this.chat.info.id,
        content: content,
      }).then(
        response => this.chat.messages.push(response)
      )
    },
    loadChat() {
      this.$store.dispatch('chat/getChat', { id: this.id }).then(
        response => this.chat = response
      );
    },
  },
  created() {
    this.loadChat();
    this.interval = setInterval(this.loadChat, 2 * 1000);
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
    function Start() {
      document.getElementById("messenger_box").scrollTop = document.getElementById("messenger_box").scrollHeight;
    }
    setTimeout(Start, 70);
    document.title = "chat";
  },
}
</script>
  
<style>
.messenger_box {
  background-color: rgba(0, 0, 0, 60%);
  width: 70%;
  height: 84vh;
  margin: 0 auto;
  color: white;
  padding-top: calc(7vh + 5px);
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  box-shadow: 0px 0px 33px #8270F2;
  overflow-y: auto;
  overflow-x: hidden;
  font-size: smaller;
}

.messenger_box::-webkit-scrollbar {
  width: 10px;
}

.messenger_box::-webkit-scrollbar-track {
  background-color: rgba(0, 0, 0, 0);
  border-bottom-right-radius: 100px;
}

.messenger_box::-webkit-scrollbar-thumb {
  border-top-right-radius: 100px;
  border-top-left-radius: 100px;
  border-bottom-right-radius: 300px;
  background-color: rgba(130, 112, 242, 70%);
}
</style>
  