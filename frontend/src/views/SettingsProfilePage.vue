<template>
  <div class="profile_box">
    <profile-settings-side-menu />

    <div class="content_settings">
      <form method="POST" id="edit_form" enctype="multipart/form-data">
        <profile-avatar />
        <profile-name />
        <profile-information />
        <profile-data />
      </form>
    </div>
  </div>
</template>

<script>
import ProfileSettingsSideMenu from "@/components/settings_profile/ProfileSettingsSideMenu";
import ProfileAvatar from "@/components/settings_profile/ProfileAvatar";
import ProfileName from "@/components/settings_profile/ProfileName";
import ProfileInformation from "@/components/settings_profile/ProfileInformation";
import ProfileData from "@/components/settings_profile/ProfileData";
export default {
  components: { ProfileData, ProfileInformation, ProfileName, ProfileAvatar, ProfileSettingsSideMenu },
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
  },
}

</script>

<style>
.profile_box {
  position: fixed;
  transform: translate(-50%, -50%);
  left: 53%;
  top: 53%;
  height: 85%;
  width: 90%;
  background: rgba(0, 0, 0, 0.75);
  box-shadow: 0px 4px 4px #8270f2;
  border-radius: 16px;
  display: flex;
}

.content_settings {
  width: 70%;
  height: 100%;
  display: inline-block;
  overflow-y: auto;

}

.content_settings::-webkit-scrollbar {
  width: 12px;
  /* ширина scrollbar */
}

.content_settings::-webkit-scrollbar-track {
  background: black;
  /* цвет дорожки */
}

.content_settings::-webkit-scrollbar-thumb {
  background-color: #8270F2;
  /* цвет плашки */
  border-radius: 100px;
  /* закругления плашки */
  border: 0px 10px 33px #8270F2;
  /* padding вокруг плашки */
}</style>