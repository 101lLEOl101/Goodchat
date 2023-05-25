<template>
  <router-link :to="`/profile/${profile.id}`" class="user-card-search">
    <img class="profile-pic-search" :src="profile.avatar"><br>
    <p class="nickname-search">{{ profile.name }} {{ profile.surname }}</p>
    <p class="info-search">{{ profile.about }}</p>
  </router-link>
</template>
<script>
export default {
  props: {
    profile: Object,
  },
}
</script>
<style>
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

.profile-pic-search {
  margin-top: 2%;
  height: 28%;
  aspect-ratio: 1/1;
  object-fit: cover;
  border-radius: 360px;
  border-color: white;
  border-style: solid;
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
</style>
