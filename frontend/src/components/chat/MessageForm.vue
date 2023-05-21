<template>
  <form class="input-area-mess">
    <!-- Тут я не уверен что сделал все правильно имеено форму перенес -->
    <textarea class="message_area" placeholder="Enter message" v-model="content" />
    <button type="button" class="btn_message" @click="send">Send</button>
  </form>
</template>
  
<script>
export default {
  data() {
    return {
      content: ''
    }
  },
  methods: {
    send() {
      if (!this.content) return;
      this.$emit('send', this.content);
      this.content = ''
    }
  }
}
</script>
  
<style>
.message_area {
  width: 100%;
  resize: none;
  height: 150px;
  background-color: rgba(0, 0, 0, 97%);
  box-shadow: 0px 10px 40px #8270F2;
  color: white;
  border: 1px solid #8270F2;
  padding: 10px;
}

.btn_message {
  background-color: #000000;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #8270F2;
  width: 100%;
  border-bottom-left-radius: 12px;
  font-size: 20px;
  transition: all 0.5s;

}

.btn_message:hover {
  background-color: rgba(0, 0, 0, 60%);
}

.input-area-mess {
  position: sticky;
  bottom: 0;
  border-bottom-left-radius: 12px;
  border-bottom-right-radius: 12px;
  margin-top: auto;
}
</style>
  