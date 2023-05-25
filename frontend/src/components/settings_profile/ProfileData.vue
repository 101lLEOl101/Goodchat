<template>
  <div id="profile_data" class="settings_settings_devider">
    <h3 class="settings_block_tittle">Private Data</h3>
    <div class="settings_change_menu">
      <div class="settings_info_box">
        <label for="id_hobby">I like: </label>
        <input id="settings_hobby" type="text" class="settings_input" required minlength="2" maxlength="100" size="100"
          placeholder="">
        <label for="id_hobby">City/Town: </label>
        <input id="settings_city" type="text" class="settings_input" required minlength="2" maxlength="20" size="100"
          placeholder="">
        <label for="id_hobby">Education: </label>
        <input id="settings_edu" type="text" class="settings_input" required minlength="2" maxlength="40" size="100"
          placeholder="">
        <label for="id_hobby">Company: </label>
        <input id="settings_company" type="text" class="settings_input" required minlength="2" maxlength="40" size="100"
          placeholder="">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
}
</script>

<style>
.settings_input {
  background-color: #000000;
  border: 1px solid #ffffff;
  border-radius: 16px;
  width: 40%;
  height: fit-content;
  padding: 1%;
  color: #ffffff;
  display: block;
  margin-bottom: 3%;
  margin-top: 1%;
}

.settings_block_tittle {
  color: #ffffff;
  text-align: left;
  padding-left: 5%;

}

.settings_settings_devider {
  color: #ffffff;
  width: 100%;
  height: fit-content;
  border-bottom: 1px solid #ffffff;
  padding-bottom: 1%;
  margin-bottom: 0;
}

.settings_change_menu {
  margin-top: 2%;
}

.settings_info_box {
  margin-left: 2%;
  display: block;
  margin-top: 0%;
  vertical-align: top;
}</style>