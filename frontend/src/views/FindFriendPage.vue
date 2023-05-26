<template>
  <div class="search-wrapper">
    <p class="search-user-id-input">Your ID: {{ $store.state.auth.user.id }}</p>
    <div class="other_users_search">
      <find-friend-form @find="sendQuerry" />
      <friend-card v-for="profile in profiles" :key="profile.id" :profile="profile" />
    </div>
    <p class="friend_error" v-if="profiles.length == 0 && querryProvided">Oops! The user does not exist!</p>
  </div>
</template>
<script>
import FindFriendForm from '@/components/find_friend/FindFriendForm.vue';
import FriendCard from '@/components/find_friend/FriendCard.vue';

export default {
  components: {
    FindFriendForm,
    FriendCard,
  },
  props: {
  },
  data() {
    return {
      profiles: [],
      querryProvided: false,
    }
  },
  methods: {
    sendQuerry(querry) {
      this.$store.dispatch('user/findUser', { querry: querry }).then(
        response => {
          this.profiles = response;
          this.querryProvided = true;
        }
      )
    }
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
    document.getElementById("f").classList.add("now-side_icon");
    document.getElementById("f").classList.remove("side_icon");
    document.getElementById("f").childNodes[0].childNodes[0].classList.add("now-icona");
    document.getElementById("f").childNodes[0].childNodes[0].classList.remove("icona");
    document.title = "find-users-page";
  },
}
</script>
<style>
.search-wrapper {
  max-width: 1000px;
  position: relative;
  width: 50%;
  min-width: 700px;
  top: 20vh;
  margin: 0 auto;
  background: rgba(0, 0, 0, 0.85);
  border: 5px solid #000000;
  box-shadow: 0px 4px 20px #8270F2;
  border-radius: 14px;
}

.other_users_search {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.search-user-id-input {
  margin-left: 5%;
  color: white;
  font-size: 250%;

}

.ur-id-search {
  color: white;
  font-size: 5%;
}

.user-card-search {
  margin-top: 5%;
  margin-right: 2%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  width: 35%;
  min-width: 250px;
  height: 419px;
  background: #000000;
  border: 1px solid #FFFFFF;
  border-radius: 50px;

}

.nickname-search {
  box-sizing: border-box;
  width: 85%;
  height: 49px;
  text-align: center;
  background: #FFFFFF;
  border: 2px solid #000000;
  border-radius: 16px;
  padding-top: 4%;
}

.info-search {
  box-sizing: border-box;
  padding-top: 3%;
  width: 85%;
  text-align: center;
  height: 43%;
  background: #FFFFFF;
  border: 2px solid #000000;
  border-radius: 12px;
}

.find_box {
  background-color: rgba(0, 0, 0, 60%);
  width: 800px;
  height: 100vh;
  margin: 0 auto;
  color: white;
  padding-top: 120px;
  border-radius: 50px;
  box-shadow: 0px 0px 33px #8270F2;
}

.find_item {
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: start;
  width: 99%;
  height: 120px;
  transform: scale(0.8, 0.8);
  transition: all 0.5s;
  border-radius: 20px;
  border: 2px solid #8270F2;
  color: white;
}

.find_item:hover {
  border-radius: 12px;
  border: #000000 solid 3px;
  box-shadow: 0px 0px 33px #8270F2;
}

.friend_error {
  color: red;
  text-align: center;
}

.chat-user-pic {
  width: 100px;
  height: 100px;
  margin-left: 5%;
  margin-right: 30px;
  border: 2px solid #000;
  border-radius: 100%;
}
</style>