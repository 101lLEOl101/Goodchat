<template>

  <div id = "profile_data" class = "settings_settings_devider">
    <h3 class = "settings_block_tittle">Private Data</h3>
    <div class = "settings_change_menu">
      <div class = "settings_info_box">
        <label for = "id_hobby">I like: </label>
        <!-- <input id = "settings_hobby" type="text" class = "settings_input" required minlength="2" maxlength="100" size="100" placeholder="{{ profile.hobby }}"></input> -->
        {{ user.hobby }}
        <label for = "id_hobby">City/Town: </label>
        <!-- <input id = "settings_city" type="text" class = "settings_input" required minlength="2" maxlength="20" size="100" placeholder="{{ profile.city }}"></input> -->
        {{ user.city }}
        <label for = "id_hobby">Education: </label>
        <!-- <input id = "settings_edu" type="text" class = "settings_input" required minlength="2" maxlength="40" size="100" placeholder="{{ profile.education }}"></input> -->
        {{ user.education }}
        <label for = "id_hobby">Company: </label>
        <!-- <input id = "settings_company" type="text" class = "settings_input" required minlength="2" maxlength="40" size="100"placeholder="{{ profile.company }}"></input> -->
        {{ user.company }}
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