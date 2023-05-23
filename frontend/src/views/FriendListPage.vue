<template>
  <div class="friend_box">
    <div class="title_h">
      <h2 class="requests_h1" id="title">Friends List</h2>\
    </div>
    <friend-list :friends="friends" />
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
      this.$store.dispatch('friend/getFriendList', {'id': this.id}).then(
        response => this.friends = response
      )
    }
  },  
  mounted() {
    this.loadFriendList();
  }

}
</script>

<style>
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