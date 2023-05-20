<template>
  <form class="form-reg">
    <input type="text" class="form-input" placeholder="Name" v-model="user.name">
    <input type="text" class="form-input" placeholder="Surname" v-model="user.surname">
    <input type="text" class="form-input" placeholder="Login" v-model="user.login">
    <input type="email" class="form-input" placeholder="Email" v-model="user.email">
    <input type="password" class="form-input" placeholder="Password" v-model="user.password">
    <input type="password" class="form-input" placeholder="Repeat password" v-model="user.rePassword">
    <p v-if="message" :class="`form-error ${message.type}`">{{ message.content }}</p>
    <button type="button" class="btn_add" @click="register">Register</button>
  </form>
</template>

<script>
import RegistrationFormValidator from '@/validators/RegistrationFormValidator';

export default {
  data() {
    return {
      user: {
        name: '',
        surname: '',
        login: '',
        email: '',
        password: '',
        rePassword: ''
      },
      message: {}
    }
  },
  methods: {
    validateForm() {
      return true;
    },
    register() {
      if (RegistrationFormValidator.valid(this.user)){
        this.message = {}
        this.$emit('register', this.clearedUser);
      }
      else{
        this.message = {
          content: 'Incorrect data entered in the form',
          type: 'error',
        }
      }
    }
  },
  computed: {
    clearedUser() {
      return {
        name: this.user.name,
        surname: this.user.surname,
        login: this.user.login,
        email: this.user.surname.toLowerCase(),
        password: this.user.password
      }
    }
  }
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