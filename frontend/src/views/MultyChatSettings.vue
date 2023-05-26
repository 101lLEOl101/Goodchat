<template>
    <div class = "container">
        <multi-chat-settings-form :IsEdit=true />
    </div>
</template>
<script>
import MultiChatSettingsForm from "@/components/multichat/MultiChatSettingsForm"
export default {
    components: {
        MultiChatSettingsForm,
    },
}
</script>
<style>
.container {
    display: block;
    height: 80%;
    width: 80%;
    color: white;
    background-color: black;
    border: solid 2px #8270F2;
    border-radius: 20px;
    padding: 3rem;
    margin: auto;
    margin-top: 5%;
}
</style>