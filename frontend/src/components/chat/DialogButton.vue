<template>
  <button type="button"  @click="writeMessage">Message</button>
</template>

<script>
export default {
  data() {
    return {
      dialog_id: '',
    }
  },
  props: {
    id: Number,
  },
  methods: {
    writeMessage() {
      this.$router.push(`/chat/${this.dialog_id}`);
    },
    getDialogId() {
      if (this.id)
        this.$store.dispatch('chat/getDialogId', {id: this.id})
          .then(response => this.dialog_id = response);
    }
  },
  created() {
    this.getDialogId();
  },
  watch: {
    id() {
      this.getDialogId();
    }
  }
}
</script>