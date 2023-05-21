<template>
  <div class="comment-box">
    <div class="timestamp">
      <p class="comment-author">{{ comment.author.name }} {{ comment.author.surname }}</p>
      <p class="time">{{ comment.timestamp }}</p>
    </div>
    <p class="comment-text">{{ comment.content }}</p>
  </div>
</template>
<script>
export default {
  props: {
    comment: Object,
  }
}
</script>
<style>
.comment-box {
  color: white;
  width: 90%;
  margin-left: 20px;
}

timestamp {
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

.comment-text {
  white-space: pre-wrap;
}
</style>