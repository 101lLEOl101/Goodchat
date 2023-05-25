<template>
  <button :disabled="loading" @click="execute">{{ content }}</button>
</template>
<script>

export default {
  data() {
    return {
      loading: true,
      friendshipStatus: {},
    }
  },
  props: ['id'],
  methods: {
    loadFriendshipStatus() {
      this.$store.dispatch('friend/getFriendshipStatus', {id: this.id}).then(
        response => { 
          this.friendshipStatus = response;
          this.loading = false;
        } 
      );
    },
    send() {
      this.$store.dispatch('friend/sendFriendRequest', {id: this.id}).then(
        _ => this.loadFriendshipStatus()
      )
    },
    withdraw() {
      this.$store.dispatch('friend/withdrawFriendRequest', {id: this.id}).then(
        _ => this.loadFriendshipStatus()
      )
    },
    accept() {
      this.$store.dispatch('friend/acceptFriendRequest', {id: this.id}).then(
        _ => this.loadFriendshipStatus()
      )
    },
    decline() {
      this.$store.dispatch('friend/declineFriendRequest', {id: this.id}).then(
        _ => this.loadFriendshipStatus()
      )
    },
    refuse() {
      this.$store.dispatch('friend/refuseFriendship', {friend_id: this.id}).then(
        _ => this.loadFriendshipStatus()
      )
    },  
    async execute() {
      this.loading = true;
      if (this.state == 'refuse')
        this.refuse();
      else if (this.state == 'withdraw')
        this.withdraw();
      else if (this.state == 'accept')
        this.accept();
      else if (this.state == 'send')
        this.send();
    },
  },
  computed: {
    state() {
      if (this.friendshipStatus.are_friends){
        return 'refuse';
      }
      else if (this.friendshipStatus.you_invited) {
        return 'withdraw';
      }
      else if (this.friendshipStatus.friend_invited) {
        return 'accept';
      }
      else {
        return 'send';
      }
    },
    content() {
      if (this.state == 'refuse')
        return 'Refuse friendship';
      else if (this.state == 'withdraw')
        return 'Withdraw request';
      else if (this.state == 'accept')
        return 'Accept request';
      else if (this.state == 'send')
        return 'Offer friendship';
      return '';
    }
  },
  created() {
    if (this.id)
      this.loadFriendshipStatus();
  },
  watch: {
    id() {
      this.loadFriendshipStatus();
    }
  }
}
</script>