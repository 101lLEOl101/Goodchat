<template>
  <form class="form-reg">
    <input type="text" class="form-input" placeholder="Login" v-model="username"/>
    <input type="password" class="form-input" placeholder="Password" v-model="password"/>
    <p v-if="message" :class="`form-error ${message.type}`">{{ message.content }}</p>
    <button type="button" class="btn_add" @click="login">Log In</button>
  </form>
</template>

<script>
import LoginFormValidator from '@/validators/LoginFormValidator';

export default {
  data() {
    return {
      username: '',
      password: '',
      message: {}
    }
  },
  methods: {
    login() {
      if (LoginFormValidator.valid(this.clearedUser)){
        this.message = {}
        this.$emit('login', this.clearedUser);
      }
      else {
        this.message = {
          type: 'error',
          content: 'Failed to authorize user with such data',
        }
      }
    }
  },
  computed: {
    clearedUser() {
      let user = {
        username: this.username,
        password: this.password,
      }
      return user;
    }
  },
}
</script>

<style>
.form-input {
  display: block;
  background-color: #000000;
  border-radius: 12px;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #797979;
  width: 250px;
  margin-bottom: 15px;
  font-size: 20px;
}

.btn_add {
  background-color: #000000;
  border-radius: 12px;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #8270F2;
  width: 100%;
  font-size: 20px;
  transition: all 0.7s;
  cursor: pointer;
  font-weight: bold;
}

.btn_add:hover {
  background: linear-gradient(to top left, #9f49ff, #19087d);
  border-radius: 12px;
  color: white;
  font-weight: bold;
}

.form-error {
  color: white;
  width: 284px;
}

.error {
  color: #fc4949;
}
</style>