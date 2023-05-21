<template>
    <friend-item 
    v-for="friend in friends"
    :key="friend.id"
    :friend = "friend"
    />
</template>

<script>
import FriendItem from '@/components/friendlist/FriendItem.vue'

export default {
    components: {
        FriendItem,
    },
    props: {
        friends: Array,
    }
}
</script>

<style>

</style>