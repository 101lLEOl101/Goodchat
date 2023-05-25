<template>
  <div class="profile_box">
    <ProfileSettingsSideMenu/>

    <div class = "content_settings">
      <form method="POST" id="edit_form" enctype="multipart/form-data">
        {% csrf_token %}
        <ProfileAvatar/>
        <ProfileName/>
        <ProfileInformation/>
        <ProfileData/>
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
  name: "ProfileSettingsPage",
  components: {ProfileData, ProfileInformation, ProfileName, ProfileAvatar, ProfileSettingsSideMenu}
}
</script>

<style>
.profile_box{
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
.content_settings{
    width: 70%;
    height: 100%;
    display: inline-block;
    overflow-y: auto;

}
.content_settings::-webkit-scrollbar {
  width: 12px;               /* ширина scrollbar */
}
.content_settings::-webkit-scrollbar-track {
  background: black;        /* цвет дорожки */
}
.content_settings::-webkit-scrollbar-thumb {
  background-color: #8270F2;    /* цвет плашки */
  border-radius: 100px;       /* закругления плашки */
  border: 0px 10px 33px #8270F2;  /* padding вокруг плашки */
}
</style>