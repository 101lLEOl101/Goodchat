<template>
  <div class="reg_box">
    <club-rules />

    <div class="input_form">
      <h1 class="reg-header">Authorization</h1><br>
      <login-form @login="login" />
      <p v-if="message" :class="`form-error ${message.type}`">{{ message.content }}</p>
      <a class="auth-link" href="registration">No Account?</a>
    </div>
  </div>
</template>

<script>
import ClubRules from '@/components/login_register/ClubRules.vue';
import LoginForm from '@/components/login_register/LoginForm.vue';

export default {
  components: {
    ClubRules,
    LoginForm
  },
  data() {
    return {
      message: {},
    }
  },
  metaInfo: {
    title: "Login"
  },
  methods: {
    login(user) {
      this.$store.dispatch('auth/login', user)
        .then(
          response => {
            this.$router.push(`/profile/${this.$store.state.auth.user.id}`);
          },
          error => {
            this.message = {
              type: 'error',
              content: 'Failed to authorize user with such data',
            };
          }
        )
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
    document.title = "login";
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
  transform: translate(-50%, -50%) scale(0.9);
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