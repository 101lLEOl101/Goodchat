<template>
  <div 
    class="friendlist_item" 
    v-for="(user) in users"
    :key="user.id"
    >
    <img class="friend-avatar" :src="user.avatar">
    <router-link class="friend_name" :to="`/profile/${user.id}`"></router-link>
    <span class="friend_name">{{ user.name }} {{ user.surname }}</span>
    <input type="checkbox" name="members-checkbox-form" v-model="user.checked">
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
    }
  },
  props: {
    // users: Array,
    checked: Array
  },
  methods: {
    updateChecked() {
      console.log('checked')
      this.$emit('update:checked', this.users);
    }
  },
  created() {
    this.users = this.checked;
  },
  watch: {
    users() {
      this.updateChecked();
    } 
  }
}
</script>

<style>
.friend-avatar {
  margin-left: 2%;
  object-fit: cover;
  aspect-ratio: 1/1;
  width: 10%;
  border-radius: 100%;
}

.friend_name {
  color: #8270F2;
  width: 20%;
  text-align: center;
}

.friendlist_item {
  display: flex;
  justify-content: start;
  align-items: center;
  width: 98%;
  background-color: black;
  border: 1px solid #8270F2;
  padding: 10px;
  border-radius: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  box-shadow: 0px 0px 5px #8270F2;
}
</style>