<template>
  <div id="profile_name" class="settings_settings_devider">
    <h3 class="settings_block_tittle">Profile Name</h3>
    <div class="settings_change_menu">
      <div class="settings_info_box">
        <input :value="name" @input="updateName" placeholder="" id="name_input" type="text" class="settings_input" required minlength="2" maxlength="14"
          size="100">
        <input :value="surname" @input="updateSurname" placeholder="" id="surname_input" type="text" class="settings_input" required minlength="7" maxlength="14"
          size="100">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    surname: String,
  },
  methods: {
    updateName(event) {
      this.$emit('update:name', event.target.value)
    },
    updateSurname(event) {
      this.$emit('update:surname', event.target.value)
    },
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