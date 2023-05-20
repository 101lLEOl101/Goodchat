<template>
  <div :class="{message_own: message.isMyown, message: !message.isMyown}">
    <div class="chat_texts">
      <div class="timestamp">
        <h2>{{ message.author }}</h2>
        <p class="time">{{ message.date_create }}</p>
      </div>
      <h3 class="message-text">{{ message.content }}</h3>
    </div>
  </div>
</template>
  
<script>
export default {
  props: {
    message: Object,
  }
}
</script>
  
<style>
/* чужое сообщение  */
.message {
  position: relative;
  margin-right: auto;
  margin-left: 15px;
  display: flex;
  align-items: center;
  justify-content: start;
  width: 99%;
  max-width: 500px;
  transition: all 0.5s;
  border-radius: 20px;
  box-shadow: 0px 10px 33px #8270F2;
  margin-top: 50px;
  margin-bottom: 50px;
  padding-left: 20px;
  word-wrap: break-word;
  word-break: break-all;
}

/* Свое сообщение */
.message_own {
  position: relative;
  margin-left: auto;
  margin-right: 15px;
  display: flex;
  align-items: center;
  justify-content: end;
  width: 99%;
  max-width: 500px;
  padding-right: 20px;
  padding-left: 20px;
  transition: all 0.5s;
  border-radius: 20px;
  box-shadow: 0px 10px 33px #8270F2;
  margin-top: 50px;
  margin-bottom: 50px;
  text-align: start;
  word-wrap: break-word;
  word-break: break-all;
}

.timestamp {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 500px;
}

.time {
  margin-left: 10px;
  margin-right: 10px;
  background-color: rgba(130, 112, 242, 20%);
  border-radius: 50px;
  padding: 5px;
}
</style>
  