<template>
  <div class="post-workspace">
    <post-form :isEdit="false" :HaveImg="false" />
  </div>
</template>
<script>
import PostForm from '@/components/post/PostForm.vue';
export default {
  components: {
    PostForm,
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
    document.getElementById("add").classList.add("now-side_icon");
    document.getElementById("add").classList.remove("side_icon");
    document.getElementById("add").childNodes[0].childNodes[0].classList.add("now-icona");
    document.getElementById("add").childNodes[0].childNodes[0].classList.remove("icona");
    document.title = "create-post";
  },
}

</script>
<style>
.post-workspace {
  width: 50%;
  margin: 0px auto;
  background: #000000;
  box-shadow: 0px 4px 4px #8270F2;
  border-radius: 37px;
  margin-top: 15vh;
  margin-bottom: 50px;
}

.new-post-header {
  display: flex;
  justify-content: space-between;
  background: #000;
  border-bottom: 1px solid #8270F2;
  border-radius: 37px 37px 0px 0px;
}

.btn_post {
  background-color: #000000;
  border-radius: 12px;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #8270F2;
  width: 50%;
  font-size: 20px;
  transition: all 0.5s;
  margin: 10px 25%;
  cursor: pointer;
}

.btn_post:hover {
  background-color: #000000;
  border-radius: 12px;
  border: #362982 solid 2px;
  color: #4131a1;
}
</style>