<template>
  <router-link :to="`chat/${chat.id}`">
    <div class="chat_item">
      <img class="chat-user-pic image_avatar" :src="chat.avatar">
      <div class="chat_texts">
        <h2>{{ chat.name }}</h2>
        <h3 id="last_message">
          <span class="author">{{ chat.lastMessage.author }}:</span> {{ chat.lastMessage.content }}
        </h3>
      </div>
    </div>
  </router-link>
</template>
  
<script>
export default {
  props: {
    chat: Object
  }
}
</script>
  
<style>
.chat_item{
    display:flex;
    align-items:center;
    justify-content: start;
    width: 99%;
    height: 120px;
    transform: scale(0.8,0.8);
    transition: all 0.5s;
    border-radius: 20px;
    border: 2px solid #8270F2;
    margin-top: 10px;
    margin-bottom: 10px;
    color: white;
}
.chat_item:hover{
    border-radius: 12px;
    border: #000000 solid 2px;
    box-shadow: 0px 0px 33px #8270F2;
}

.chat_texts{
    text-decoration: none;
    word-wrap: break-word;
    word-break: break-all;
}

.chat-user-pic {
    width: 100px;
    margin-left:5%;
    margin-right:30px;
    border: 2px solid #000;
    border-radius: 100%;
}

.author {
  color: #8270F2;
}
</style>
  