<template>
    <div class="navigation">
        <div class="side_menu">
            <div id="prof" class="side_icon">
                <router-link v-if="$store.state.auth.status.loggedIn" :to="`/profile/${$store.state.auth.user.id}`"
                    class="hr">
                    <i class="fa-regular fa-user icona"></i>
                </router-link>
                <router-link v-else :to="`/login`" class="hr">
                    <i class="fa-regular fa-user icona"></i>
                </router-link>
            </div>
            <div id="mes" class="side_icon">
                <router-link to="/chatlist" class="hr">
                    <i class="fa-regular fa-comment-dots icona"></i>
                </router-link>
            </div>
            <div id="friend" class="side_icon">
                <router-link v-if="$store.state.auth.status.loggedIn" :to="`/friendlist/${$store.state.auth.user.id}`"
                    class="hr">
                    <i class="fa-solid fa-user-group icona"></i>
                </router-link>
                <router-link v-else :to="`/login`" class="hr">
                    <i class="fa-solid fa-user-group icona"></i>
                </router-link>
            </div>
            <div id="set" class="side_icon">
                <router-link to="/settings" class="hr">
                    <i class="fa-solid fa-gear icona"></i>
                </router-link>
            </div>
            <div id="glob" class="side_icon">
                <router-link to="/feed" class="hr">
                    <i class="fa-solid fa-globe icona"></i>
                </router-link>
            </div>
            <div id="book" class="side_icon">
                <router-link to="/bookmarks" class="hr">
                    <i class="fa-regular fa-bookmark icona"></i>
                </router-link>
            </div>
            <div id="add" class="side_icon">
                <router-link to="/addpost" class="hr">
                    <i class="fa-solid fa-plus icona"></i>
                </router-link>
            </div>
            <div id="f" class="side_icon">
                <router-link to="/findfriend" class="hr">
                    <i class="fa-solid fa-magnifying-glass icona"></i>
                </router-link>
            </div>
        </div>
    </div>
</template>
<script>
</script>
<style>
.navigation {
    display: inline-flex;
    width: 10%;
    position: fixed;
    margin-top: 10%;
}

.side_icon {
    width: calc(24px + 11 * (200vw / 1280));
    height: calc(24px + 11 * (200vw / 1280));
    background-color: black;
    border-radius: 1000px;
    margin: 6px;
    color: white;
    border: 2px solid #8270F2;
    transition: 0.3s;
}

.now-side_icon {
    width: calc(24px + 11 * (200vw / 1280));
    height: calc(24px + 11 * (200vw / 1280));
    background-color: white;
    color: black;
    border-radius: 1000px;
    margin: 6px;
    border: 2px solid #8270F2;
    transition: 0.3s;
}

.icona {
    color: white;
    margin-left: 20%;
    margin-top: 18%;
    font-size: calc(17px + 11 * (130vw / 1280));
    transition: 0.3s;
}

.now-icona {
    color: black;
    margin-left: 20%;
    margin-top: 18%;
    font-size: calc(17px + 11 * (130vw / 1280));
    transition: 0.3s;
}

.side_menu {
    background-color: black;
    border-top-right-radius: calc((24px + 11 * (200vw / 1280)) / 2);
    border-bottom-right-radius: calc((24px + 11 * (200vw / 1280)) / 2);
    position: fixed;
    border: solid 1px #8270F2;
    box-shadow: 0px 10px 10px #8270F2;
    transform: translateY(-50%);
    top: 50%;
    max-height: 80%;
    left: -1px;
}

.fa-user-group {
    font-size: calc(17px + 8 * (130vw / 1280));
    margin-left: 15%;
    margin-top: 18%;
}
</style>
