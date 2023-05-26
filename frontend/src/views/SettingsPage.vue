<template>
  <div class="setting_page">
    <router-link to="/settings/profile" class="setting-btn">Settings Profile</router-link>
    <button @click="logout" class="setting-btn">Exit</button>
  </div>
</template>
  
<script>
export default {
  methods: {
    logout() {
      this.$store.dispatch('auth/logout');
      location.reload(true);
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
    document.getElementById("set").classList.add("now-side_icon");
    document.getElementById("set").classList.remove("side_icon");
    document.getElementById("set").childNodes[0].childNodes[0].classList.add("now-icona");
    document.getElementById("set").childNodes[0].childNodes[0].classList.remove("icona");
    document.title = "settings";
  },
}
</script>
  
<style>
.setting_page {
  width: 50%;
  height: 75vh;
  margin: 0 auto;
  background-color: #000000;
  border-radius: 73px;
  box-shadow: 0px 10px 30px #8270f2;
  padding-top: 100px;
}

.ou-setting-btn {
  margin: 80px;
  width: 40%;
}

.setting-btn {
  padding: 1%;
  color: white;
  font-size: calc(24px + 16 * (100vw / 2560));
  padding-right: auto;
  padding-left: auto;
  border: 2px solid white;
  background-color: black;
  border-radius: 20px;
  text-decoration: none;
  width: 50%;
  display: grid;
  text-align: center;
  margin: auto;
  margin-top: 10%;
}
</style>