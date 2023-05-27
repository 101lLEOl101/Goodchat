<template>
  <div class="reg_box">
    <club-rules />
    <div class="input_form">
      <h1 class="reg-header">Registration</h1><br>
      <registration-form @register="register" />
      <p v-if="message" :class="`${message.type}`">{{ message.content }}</p>
      <a class="auth-link" href="login">Already a gogorik?</a>
    </div>
  </div>
</template>

<script>
import RegistrationForm from '@/components/login_register/RegistrationForm.vue';
import ClubRules from '@/components/login_register/ClubRules.vue';

export default {
  components: {
    RegistrationForm,
    ClubRules
  },
  data() {
    return {
      user: {
        name: '',
        surname: '',
        email: '',
        password: '',
        rePassword: ''
      },
      message: {}
    }
  },
  methods: {
    register(user) {
      this.$store.dispatch('auth/register', user)
        .catch(error => {
          if (error.code === 900) {
            this.message = {
              type: 'error',
              content: 'User with such data is already registered',
            }
          }
        })
        .then(response => {
          this.$router.push('/login');
        })
    }
  },
  created() {
    this.$store.dispatch('auth/logout');
  },
  mounted() {
    if (document.getElementsByClassName("now-side_icon").length != 0) {
      let icon = document.getElementsByClassName("now-side_icon")[0];
      let icona = document.getElementsByClassName("now-icona")[0];
      icona.classList.remove("now-icona");
      icon.classList.remove("now-side_icon");
      icona.classList.add("icona");
      icon.classList.add("side_icon");
    }
    document.title = "registation";
  },
}
</script>

<style>
.reg-header {
  color: white;
  text-align: center;

}

.reg_box {
  display: flex;
  margin-top: 50px;
  align-items: center;
  justify-content: center;
  position: fixed;
  transform: translate(-50%, -50%);
  left: 50%;
  top: 50%;
}

.auth-link {
  text-decoration: none;
  color: #8270F2;
  margin-top: 10px;
  font-size: 13px;
  text-shadow:
    -0 -1px 6px #000000,
    0 -1px 6px #000000,
    -0 1px 6px #000000,
    0 1px 6px #000000,
    -1px -0 6px #000000,
    1px -0 6px #000000,
    -1px 0 6px #000000,
    1px 0 6px #000000,
    -1px -1px 6px #000000,
    1px -1px 6px #000000,
    -1px 1px 6px #000000,
    1px 1px 6px #000000,
    -1px -1px 6px #000000,
    1px -1px 6px #000000,
    -1px 1px 6px #000000,
    1px 1px 6px #000000;
}
</style>