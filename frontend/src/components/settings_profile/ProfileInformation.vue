<template>
  <div id = "profile_information" class = "settings_settings_devider">
    <h3 class = "settings_block_tittle">About</h3>
    <div class = "settings_change_menu">
      <div class = "settings_info_box">
        <!-- <textarea class = "settings_input" rows="5" cols="33">{{ profile.about }}</textarea> -->
        {{ user.about }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  props: {
    user: Object
  }
}
</script>

<style>
.settings_block_tittle{
    color: #ffffff;
    text-align: left;
    padding-left: 5%;

}
.settings_settings_devider{
    color: #ffffff;
    width: 100%;
    height: fit-content;
    border-bottom: 1px solid #ffffff;
    padding-bottom: 1%;
    margin-bottom: 0;
}
.settings_change_menu{
    margin-top:2%;
}
.settings_info_box{
    margin-left: 2%;
    display: block;
    margin-top: 0%;
    vertical-align: top;
}
</style>