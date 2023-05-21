<template>
  <form class="input-area-mess">
    <textarea name="content" cols="40" rows="10" class="message_area" placeholder="New comment" required=""
      id="id_content" v-model="content"></textarea>
    <button class="btn_message" type="button" @click="send">Send</button>
  </form>
</template>
<script>
export default {
  data() {
    return {
      content: '',
    }
  },
  methods: {
    send() {
      if (this.content == '') return;
      this.$emit('send', this.content);
      this.content = '';
    }
  }
}
</script>
<style>
.input-area-mess {
  position: sticky;
  bottom: 0;
}

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
  font-size: 20px;
  transition: all 0.5s;
}

.btn_message:hover {
  background-color: rgba(0, 0, 0, 60%);
}
</style>