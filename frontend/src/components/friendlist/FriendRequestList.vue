<template>
    <friend-request 
    v-for="inviter in inviters"
    :key="inviter.id"
    :inviter = "inviter"
    />
</template>

<script>
import FriendRequest from '@/components/friendlist/FriendRequest.vue'

export default {
    components: {
        FriendRequest,
    },
    props: {
        inviters: Array,
    }
}
</script>

<style>

</style>