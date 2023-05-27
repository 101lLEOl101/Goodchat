<template>
  <div class="container">
    <multi-chat-settings-form :IsEdit=false :oldInvitable="friends" v-model:name="name"/>
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
      friends: [],
      name: '',
    }
  },
  methods: {
    loadFriends() {
      return this.$store.dispatch('friend/getFriendList', {id: this.$store.getters['auth/user'].id}).then(
        response => {
          this.friends = response;
          return response;
        }
      )
    },
    addCheckedFields() {
      this.friends.forEach(friend => {
        friend.checked = false;
      });
    },
  },
  created() {
    this.loadFriends().then(
      response => {
        this.addCheckedFields();
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