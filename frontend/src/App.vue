<template>
  <header>
    <div class="header_menu">
      <router-link to="/feed" class="logo_h">
        <img src="@/assets/logo.png" class="logo_h" alt="Feed">
      </router-link>
    </div>

    <div v-if="$store.state.auth.status.loggedIn" class="auth_box">
      <img class="image_avatar header_avatar" :src="$store.state.auth.user.avatar">
      <a disabled class="auth_btn" @click="logout">Exit</a>
    </div>
    <div v-else class="auth_box">
      <router-link to="/registration" class="auth_reg_btn">Registration</router-link>
      <router-link to="/login" class="auth_btn">Login</router-link>
    </div>
  </header>

  <side-menu />
  <div class="main">
    <router-view />
  </div>
  <!-- <script src="https://kit.fontawesome.com/a5b3356b6d.js" crossorigin="anonymous"></script> -->
  
</template>

<script>
import SideMenu from '@/components/navigation/SideMenu';
export default{
  components: {
    SideMenu,
  },
  methods: {
    logout() {
      this.$store.dispatch('auth/logout');
      location.reload(true);
    }
  }
}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600&display=swap');
/* BASE */
/* base.html: header*/
body{
    background-image: url("@/assets/background.jpg");
    background-size: cover;
    background-attachment: fixed;
    margin: 0;
    font-family: 'Inter', sans-serif;
}

body::-webkit-scrollbar {
  width: 12px;               /* ширина scrollbar */
}
body::-webkit-scrollbar-track {
  background: black;        /* цвет дорожки */
}
body::-webkit-scrollbar-thumb {
  background-color: #8270F2;    /* цвет плашки */
  border-radius: 100px;       /* закругления плашки */
  border: 0px 10px 33px #8270F2;  /* padding вокруг плашки */
}

header{
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
.header_menu{
    width: 100%;
    height: 100%;
    background-color: black;
}

.logo_h{
    height: 100%;
    display: flex;
}

.logo{
    position: absolute;
    right: 95%;
}
/*header: end*/
/*main*/

.main{
    display: flex;

}

.auth_reg_btn{
    background: transparent;
    color:white;
    border: 2px solid black;
    text-align:center;
    font-family: 'Inter', sans-serif;
    margin-right: 20px;
    transition: all 0.3s;
}
.auth_btn:hover{
    border-bottom: 2px solid #8270F2;
}

.auth_reg_btn:hover{
    border-bottom: 2px solid #8270F2;
}

.auth_btn{
    background: transparent;
    color: #8270F2;
    font-family: 'Inter', sans-serif;
    border: 2px solid black;
    margin-right:50px;
    transition: all 0.3s;
}

.auth_box{
    width:250px;
    height: 100%;
    display:flex;
    justify-content:center;
    align-items:center;
}

.img_header{
    height: 80%;
    border-radius: 100%;
    margin-right: 20px;
    box-shadow: 0px 0px 20px #8270F2;
    border: 1px solid #8270F2;
}

a{
text-decoration: none;
}

textarea:focus, input:focus
{
  outline: none;
}


li{
    margin-bottom: 5px;
    margin-top: 5px;
}

.box {
   position: relative;
   overflow:hidden;
   width: 5.6vh;
   height: 80%;
   border-radius: 100%;
   margin-right: 20px;
   box-shadow: 0px 0px 20px #8270F2;
   border: 1px solid #8270F2;
}

.box img {
   position: absolute;
   top:50%;
   left:50%;
   width:100%;
   height: 100%;
   -webkit-transform:translate(-50%,-50%);
       -ms-transform:translate(-50%,-50%);
           transform:translate(-50%,-50%);
   -o-object-fit:cover;
      object-fit:cover;
}

.block_inner_avatar {
  width: 100%;
  padding-top: 100%;
  border-radius: 100%;
  position: relative;
}

.image_avatar {
	aspect-ratio: 1/1;
	object-fit: cover;
}

.header_avatar{
    height: 5.6vh;
    border-radius: 100%;
    margin-right: 20px;
    box-shadow: 0px 0px 20px #8270F2;
    border: 1px solid #8270F2;
}
</style>
