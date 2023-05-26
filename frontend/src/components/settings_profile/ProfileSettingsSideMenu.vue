<template>
  <div class="side_menu_settings">
    <h1 class="settings_tittle">Settings</h1>
    <a href="#profile_avatar" class="settings_link">Profile Picture</a>
    <a href="#profile_name" class="settings_link">Name</a>
    <a href="#profile_information" class="settings_link">About</a>
    <a href="#profile_data" class="settings_link">Personal Data</a>

    <div class="settings_buttons">
      <router-link to="/settings" class="settings_btn settings_btn1">Cancel</router-link>
      <button @click="$emit('edit')" class="settings_btn settings_btn2 settings_save" form="edit_form">Apply</button>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
.side_menu_settings {
  background: #0C0C0C;
  border-radius: 16px;
  width: 30%;
  height: 100%;
  box-shadow: 0px 4px 4px #8270f2;
  display: inline-block;
  position: relative;
}

.settings_tittle {
  color: #ffffff;
  width: 100%;
  height: fit-content;
  text-align: center;
  border-bottom: 1px solid #ffffff;
  padding-bottom: 5%;
  margin-bottom: 0;
}

.settings_btn {
  color: #ffffff;
  width: 44%;
  padding: 4%;
  margin: 2%;
  background-color: #1F1F1F;
  border: 0px;
  border-radius: 16px;
  font-size: 100%;
  font-weight: bolder;
  cursor: pointer;
  text-align: center;
}

.settings_save {
  background-color: #8270F2;
}

.settings_link {
  width: 100%;
  height: fit-content;
  place-content: center;
  border-bottom: 1px solid #ffffff;
  padding-bottom: 5%;
  padding-top: 5%;
  display: flex;
  color: #ffffff;
}

.settings_buttons {
  color: #000000;
  display: flex;
  position: absolute;
  bottom: 0;
  height: fit-content;
  width: 100%;
  justify-content: space-between;
}
</style>