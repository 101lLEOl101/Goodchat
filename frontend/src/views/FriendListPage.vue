<template>
  <div class="friend_box">
    <div class="title_h">
      <h2 class="requests_h1" id="title">Friends List</h2>
      <router-link v-if="id == $store.state.auth.user.id" to="/requestlist/" class="btn_request_h2" id="btn">
        Friend Requests
      </router-link>
    </div>
    <div v-if="friends.length == 0" class="message_none" style="display:flex;">No friends yet</div>
    <friend-list @deleteFriend="deleteFriend" :friends="friends" :IsFriends=true />
  </div>
</template>

<script>
import FriendList from '@/components/friendlist/FriendList';

export default {
  props: ['id'],
  components: {
    FriendList,
  },
  data() {
    return {
      friends: [],
    }
  },
  methods: {
    loadFriendList() {
      this.$store.dispatch('friend/getFriendList', { 'id': this.id }).then(
        response => this.friends = response
      )
    },
    deleteFriend(friend_id) {
      this.$store.dispatch('friend/refuseFriendship', { friend_id: friend_id });
      this.friends = this.friends.filter(friend => friend.id != friend_id);
    },
  },
  mounted() {
    this.loadFriendList();
    if (document.getElementsByClassName("now-side_icon").length != 0) {
      let icon = document.getElementsByClassName("now-side_icon")[0];
      let icona = document.getElementsByClassName("now-icona")[0];
      icona.classList.remove("now-icona");
      icon.classList.remove("now-side_icon");
      icona.classList.add("icona");
      icon.classList.add("side_icon");
    }
    document.getElementById("friend").classList.add("now-side_icon");
    document.getElementById("friend").classList.remove("side_icon");
    document.getElementById("friend").childNodes[0].childNodes[0].classList.add("now-icona");
    document.getElementById("friend").childNodes[0].childNodes[0].classList.remove("icona");
    document.title = "friend-list-page";
  },

}
</script>

<style>
.message_none {
  display: flex;
  justify-content: start;
  align-items: center;
  text-align: center;
  color: white;
  width: 98%;
  padding: 50px;
  background-color: black;
  border: 1px solid #8270F2;
  border-radius: 10px;
  margin: 10px auto;
  box-shadow: 0px 0px 5px #8270F2;
}

.btn_request_h2 {
  color: black;
  margin-left: 10px;
  font-weight: bold;
  padding: 10px;
  background-color: rgba(131, 113, 242, 0.70);
  border: none;
  border-radius: 5px;
  box-shadow: 0px 0px 10px #8270F2;
  cursor: pointer;
}

.requests_h1 {
  display: block;
  cursor: default;
  color: white;
  text-align: center;
}

.title_h {
  display: flex;
  align-items: center;
}

.friend_box {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  width: 110vh;
  background-color: rgba(0, 0, 0, 50%);
  box-shadow: 0px 0px 10px #8270F2;
  border: black solid 5px;
  border-radius: 14px;
  margin: 0 auto;
  position: relative;
  top: 15vh;
  padding: 20px;
}
</style>