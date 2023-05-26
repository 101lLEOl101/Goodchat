<template>
<div class="messager_container">
  <message-card 
    v-for="message in messages" 
    :key="message.id" 
    :message="message"
    />
</div>
</template>

<script>
import MessageCard from '@/components/chat/MessageCard';

export default {
  components: {
    MessageCard,
  },
  props: {
    messages: Array,
  }
}

</script>

<style>
.messager_container{
    min-height:58.4vh;
}
</style>