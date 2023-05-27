<template>
  <div class="container">
    <multi-chat-settings-form 
      :IsEdit=true 
      :defaultAvatar="chat.avatar"
      v-model:name="chat.name"
      :oldMembers="members"
      :oldInvitable="friends"
      :id="chat.id"
      />
  </div>
</template>
<script>
import MultiChatSettingsForm from "@/components/multichat/MultiChatSettingsForm"
export default {
  components: {
    MultiChatSettingsForm,
  },
  data() {
    return {
      chat: {},
      members: [],
      friends: [],
    }
  },
  props: {
    id: Number,
  },
  methods: {
    loadChat() {
      return this.$store.dispatch('chat/getChatInfo', {id: this.id}).then(
        response => {
          this.chat = response.chat;
          this.members = response.members;
          this.$store.dispatch('chat/getChatAccessMode', {id: this.id}).then(
            mode => {
              if (mode < 3) this.$router.push('/chatlist');
            }
          )
          return response;
        }
      )
    },
    friendNotInMembers(friend) {
      for(let i = 0; i < this.members.length; ++i) {
        if (this.members[i].id == friend.id) return false;
      }
      return true;
    },
    loadFriends() {
      return this.$store.dispatch('friend/getFriendList', {id: this.$store.getters['auth/user'].id}).then(
        response => {
          this.friends = response;
          return response;
        }
      )
    },
    filterInvitable() {
      this.friends = this.friends.filter(friend => this.friendNotInMembers(friend));
    },
    addCheckedFields() {
      this.friends.forEach(friend => {
        friend.checked = false;
      });
      this.members.forEach(friend => {
        friend.checked = true;
      })
    },
  },
  created() {
    this.loadChat().then(
      _ => {
        this.loadFriends().then(
          _o => {
            this.filterInvitable();
            this.addCheckedFields();
            if (!this.chat.isMulty) 
              this.$router.push('/chatlist');
          }
        )
      }
    )
  },
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
</style>