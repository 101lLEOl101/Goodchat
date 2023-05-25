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
    getDialogId() {
        return this.$store.dispatch('chat/getDialogId', {id: this.id})
          .then(response => this.dialog_id = response);
    },
    writeMessage() {
      this.getDialogId().then(
        _ => this.$router.push(`/chat/${this.dialog_id}`)
      )
    },
  }
}
</script>