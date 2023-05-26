<template>
  <div class="profile-card">
    <img :src="user.avatar" class="profile-pic image_avatar" />
    <div class="row">
      <div class="left">
        <div class="user-nickname" id="usernick">Name: {{ user.name }} </div>
        <div class="user-nickname top" id="usersurname">Lastname: {{ user.surname }}</div>
        <div class="user-info unhidden">About: <br> {{ user.about }} </div>
        <div class="user-nickname bottom" id="userlike">Hobbies: {{ user.hobby }}</div>
        <div class="user-nickname hiddenunckecked">City: {{ user.city }}</div>
        <div class="user-nickname hiddenunckecked">Education: {{ user.education }}</div>
        <div class="user-nickname hiddenunckecked">Company: {{ user.company }}</div>
      </div>
      <div class="right">
        <div class="user-info">About: <br> {{ user.about }} </div>
      </div>
    </div>

    <dialog-button v-if="user && !userIsMe" class="btn_profile" :id="user.id" />
    <friend-state-button v-if="!userIsMe" class="btn_profile" :id="user.id"/>

    <label for="toggle" class="btn_profile">More</label>
  </div>
</template>

<script>
import DialogButton from '@/components/chat/DialogButton';
import FriendStateButton from '@/components/friendlist/FriendStateButton';

export default {
  components: {
    DialogButton,
    FriendStateButton,
  },
  data() {
    return {}
  },
  props: {
    user: Object,
    userIsMe: Boolean,
  },
}
</script>

<style>
.profile-card {
  position: fixed;
  right: 1%;
  width: 18%;
  background: rgba(0, 0, 0, 0.75);
  box-shadow: 0px 0px 15px #8270F2;
  border-radius: 50px;
  transform: translateY(-50%);
  padding-top: 1%;
  padding-bottom: 1%;
  top: 55%;
  transition: all 1s;
}

.profile-pic {
  width: 50%;
  margin: 0 25%;
  border-radius: 100%;
  box-shadow: 0px 0px 30px #8270f2;
  transition: all 1s;
}

.user-nickname {
  width: 70%;
  margin: 10px 15%;
  text-align: center;
  background: #fff;
  border-radius: 16px;
  padding: 15px 0;
  transition: all 1s;
}

.user-info {
  width: 70%;
  margin: 10px 15%;
  height: 154px;
  padding: 20px 0;
  text-align: center;
  background: #fff;
  border-radius: 12px;
  transition: all 1s;
}

.btn:hover~.profile-card-more {
  display: block;
}

.profile-card-more {
  width: 400px;
  height: 900px;
  background: #000;
  box-shadow: 0px 4px 4px #8270F2;
  border-radius: 50px;
  padding-top: 67px;
  margin-left: auto;
  margin-right: auto;
  position: relative;
  top: -965px;
  display: none;
  z-index: 1;

}

.form-add-post {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

.btn_profile {
  background-color: #000000;
  border-radius: 12px;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #8270F2;
  width: -webkit-fill-available;
  font-size: 20px;
  transition: all 0.5s;
  margin: 10px 25%;
  display: inline-block;
  text-align: center;
  transition: all 1s;
}

.btn_profile:hover {
  background-color: #000000;
  border-radius: 12px;
  border: #000000 solid 2px;
  box-shadow: 0px 0px 33px #8270F2;
}
</style>