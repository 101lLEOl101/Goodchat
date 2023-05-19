<template>
  <header>
    <div class="header_menu">
      <router-link to="/home" class="logo_h">
        <img src="@/assets/logo.png" class="logo_h" alt="Home Page">
      </router-link>
    </div>

    <div v-if="$store.state.auth.status.loggedIn" class="auth_box">
      <img class="img_header" src="@/assets/logo.png">
      <a disabled class="auth_btn" @click="logout">Exit</a>
    </div>
    <div v-else class="auth_box">
      <router-link to="/registration" class="auth_reg_btn">Registration</router-link>
      <router-link to="/login" class="auth_btn">Login</router-link>
    </div>
  </header>

  <div class = "navigation">
    <div  class = "side_menu">
        <div id = "prof" class = "side_icon">
            <router-link to="/settings" class = "hr" >
                <i class="fa-regular fa-user icona"></i>
            </router-link>
        </div>
        <div  id = "mes" class = "side_icon">
            <router-link to="/settings" class = "hr" >
                <i class="fa-regular fa-comment-dots icona"></i>
            </router-link>
        </div>
        <div  id = "friend" class = "side_icon">
            <router-link to="/settings" class = "hr" >
                <i class="fa-solid fa-user-group icona"></i>
            </router-link>
        </div>
        <div  id = "set" class = "side_icon">
            <router-link to="/settings" class = "hr" >
                <i class="fa-solid fa-gear icona"></i>
            </router-link>
        </div>
        <div id = "glob" class = "side_icon">
            <router-link to="/global" class = "hr" >
                <i class="fa-solid fa-globe icona"></i>
            </router-link>
        </div>
        <div  id = "book" class = "side_icon">
            <router-link to="/settings" class = "hr" >
                <i class="fa-regular fa-bookmark icona"></i>
            </router-link>
        </div>
        <div  id = "add" class = "side_icon">
            <router-link to="/settings" class = "hr" >
                <i class="fa-solid fa-plus icona"></i>
            </router-link>
        </div>
        <div  id = "f" class = "side_icon">
            <router-link to="/settings" class = "hr" >
                <i class="fa-solid fa-magnifying-glass icona"></i>
            </router-link>
        </div>
    </div>
</div>
  <div class="main">
    <router-view />
  </div>
  <!-- <script src="https://kit.fontawesome.com/a5b3356b6d.js" crossorigin="anonymous"></script> -->
  
</template>

<script >
export default{
  methods: {
    logout() {
      this.$store.dispatch('auth/logout');
    }
  }
}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap');

/* BASE */
/* base.html: header*/
body {
  background-image: url("@/assets/background.jpg");
  background-size: cover;
  background-attachment: fixed;
  margin: 0;
  font-family: 'Inter', sans-serif;
}

body::-webkit-scrollbar {
  width: 12px;
  /* ширина scrollbar */
}

body::-webkit-scrollbar-track {
  background: black;
  /* цвет дорожки */
}

body::-webkit-scrollbar-thumb {
  background-color: #8270F2;
  /* цвет плашки */
  border-radius: 100px;
  /* закругления плашки */
  border: 0px 10px 33px #8270F2;
  /* padding вокруг плашки */
}

header {
  display: flex;
  align-items: center;
  color: white;
  background-color: #000000;
  border-bottom: #8270F2 solid 5px;
  width: 100%;
  height: 7%;
  position: fixed;
  z-index: 1;
  box-shadow: 0px 10px 33px #8270f2;

}

.header_menu {
  width: 100%;
  height: 100%;
  background-color: black;
}

.logo_h {
  height: 100%;
  display: flex;
}

.logo {
  position: absolute;
  right: 95%;
}

/*header: end*/
/*main*/

.main {
  display: flex;

}

/* Navigation*/
.navigation {
  display: inline-flex;
  width: 10%;
  position: fixed;
  margin-top: 10%;
}

.side_icon {
  width: calc(24px + 11 * (200vw / 1280));
  height: calc(24px + 11 * (200vw / 1280));
  background-color: black;
  border-radius: 1000px;
  margin: 6px;
  color: white;
  border: 2px solid #8270F2;
  transition: 0.3s;
  display: flex;
  justify-content: center;
  align-items: center;
}

.now-side_icon {
  width: calc(24px + 11 * (200vw / 1280));
  height: calc(24px + 11 * (200vw / 1280));
  background-color: white;
  color: black;
  border-radius: 1000px;
  margin: 6px;
  border: 2px solid #8270F2;
  transition: 0.3s;
  display: flex;
  justify-content: center;
  align-items: center;
}

.icona {
  color: white;
  font-size: calc(17px + 11 * (130vw / 1280));
  transition: 0.3s;
}

.now-icona {
  color: black;
  font-size: calc(17px + 11 * (130vw / 1280));
  transition: 0.3s;
}

.side_menu {
  background-color: black;
  border-top-right-radius: calc((24px + 11 * (200vw / 1280)) / 2);
  border-bottom-right-radius: calc((24px + 11 * (200vw / 1280)) / 2);
  position: fixed;
  border: solid 1px #8270F2;
  box-shadow: 0px 10px 10px #8270F2;
  transform: translateY(-50%);
  top: 50%;
  max-height: 80%;
  left: -1px;
}

.auth_reg_btn {
  background: transparent;
  color: white;
  border: 2px solid black;
  text-align: center;
  font-family: 'Inter', sans-serif;
  margin-right: 20px;
  transition: all 0.3s;
}

.auth_btn:hover {
  border-bottom: 2px solid #8270F2;
}

.auth_reg_btn:hover {
  border-bottom: 2px solid #8270F2;
}

.auth_btn {
  background: transparent;
  color: #8270F2;
  font-family: 'Inter', sans-serif;
  border: 2px solid black;
  margin-right: 50px;
  transition: all 0.3s;
}

.auth_box {
  width: 250px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.fa-user-group {
  font-size: calc(16px + 8 * (130vw / 1280));
}

.img_header {
  height: 80%;
  border-radius: 100%;
  margin-right: 20px;
  box-shadow: 0px 0px 20px #8270F2;
  border: 1px solid #8270F2;
}

a {
  text-decoration: none;
}

textarea:focus,
input:focus {
  outline: none;
}

li {
  margin-bottom: 5px;
  margin-top: 5px;
}
</style>
