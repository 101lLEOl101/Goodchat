<template>
  <div class="ur_friend">
    <router-link class="chat-avatar-div" :to="headerLink"><img :src="info.avatar" class="friend-user-pic image_avatar"></router-link>
    <p>{{ info.name }}</p>
  </div>
</template>
  
<script>
export default {
  props: {
    info: Object,
  },
  computed: {
    headerLink() {
      let link = '';
      if (this.info.isMulty)
        link = `/chat/${this.info.id}/info`;
      else 
        link = `/profile/${this.info.interlocutorID}`;
      return link; 
    }
  },
}
</script>
  
<style>
.image_avatar {
	aspect-ratio: 1/1;
	object-fit: cover;
}


.ur_friend {
  height: 7%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0.7%;
  left: 50%;
  transform: translateX(-50%);
  z-index: 51;
  width: 200px;
  font-size: 15px;
}

.chat-avatar-div {
  height: 100%
}

.friend-user-pic {
  height: 80%;
  aspect-ratio: 1/1;
  margin-right: 20px;
  box-shadow: 0px 0px 20px #8270F2;
  border: 1px solid #8270F2;
  border-radius: 100%;
}
</style>
  