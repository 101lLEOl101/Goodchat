<template>
  <div class="container">
    <h1 class="chat-info-title">Info</h1>
    <div class="input-img">
      <h2 class="chat-name">Name: {{ chat.name }}</h2>
      <img :src="chat.avatar" class="chat-avatar-info">
    </div>
    <chat-member-list :members="members"/>
    <router-link to="/multychatsettings" class="btn-save" href="/chat/settings/1">Edit</router-link>
    <router-link to="/chatlist" class="btn-discard" href="/chat/leave/1">Exit Chat</router-link>
  </div>
</template>

<script>
import ChatMemberList from '@/components/chat/ChatMemberList';

export default {
  components: {
    ChatMemberList,
  },
  data() {
    return {
      chat: {},
      members: [],
    }
  },
  props: ['id'],
  methods: {
    loadChat() {
      console.log('execute')
      this.$store.dispatch('chat/getChatInfo', {id: this.id}).then(
        response => {
          this.chat = response.chat;
          this.members = response.members;
        }
      )
    }
  },
  created() {
    this.loadChat();
  }
}
</script>

<style>
.container {
  display: block;
  height: 80%;
  width: 80%;
  color: white;
  background-color: black;
  border: solid 2px #8270F2;
  border-radius: 20px;
  padding: 3rem;
  margin: auto;
  margin-top: 5%;
}

.chat-info-title {
  text-align: center;
  color: #8270F2;
}

.input-img {
  display: grid;
  justify-content: center;
  margin-top: 2em;
}

.chat-name {
  text-align: center;
}

.chat-avatar-info {
  margin-left: 2%;
  width: 200px;
  border: solid 2px #8270F2;
  border-radius: 100%;
  object-fit: cover;
  aspect-ratio: 1/1;
  margin: 0 auto;
}
</style>