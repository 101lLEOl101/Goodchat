<template>
    <div class="chat_box">
       <a href="{% url 'new-multychat' %}" class = "create_chat"><i class="fa-solid fa-comment-medical create"></i></a>
       <h2 style="text-align:center;"> Список чатов </h2>
       <chats-list :chats="chats"/>
   </div>
 </template>
 
 <script>
 import ChatsList from '@/components/chat/ChatsList.vue'

 export default {
    data() {
    return {
        chats: [
            {
                name: 'Stepan Pupkin',
                avatar: '@/images/ANONYMOUS_AVATAR.png',
                last_message: 'охх зря я туда полез...',
            },
            {
                name: 'Oleg Mongol',
                avatar: '@/images/ANONYMOUS_AVATAR.png',
                last_message: 'эээ а где йупи йо',
            },
            {
                name: 'Stepan Jupa',
                avatar: '@/images/ANONYMOUS_AVATAR.png',
                last_message: 'Хочу колы',
            },
            {
                name: 'Uder Nidar',
                avatar: '@/images/ANONYMOUS_AVATAR.png',
                last_message: 'Хочу банан',
            },
            {
                name: 'Stepan Pupkin',
                avatar: '@/images/ANONYMOUS_AVATAR.png',
                last_message: 'охх зря я туда полез...',
            },
            {
                name: 'Oleg Mongol',
                avatar: '@/images/ANONYMOUS_AVATAR.png',
                last_message: 'эээ а где йупи йо',
            },
            {
                name: 'Stepan Jupa',
                avatar: '@/images/ANONYMOUS_AVATAR.png',
                last_message: 'Хочу колы',
            },
            {
                name: 'Uder Nidar',
                avatar: '@/images/ANONYMOUS_AVATAR.png',
                last_message: 'Хочу банан',
            },
            
        ],
    }
  },
  components: {
    ChatsList
    
  }
}
 </script>
 
 <style>
 .chat_box{
   background-color: rgba(0,0,0,60%);
   width: 800px;
   min-height: 100vh;
   margin: 0 auto;
   color: white;
   padding-top: calc(7vh + 5px);
   border-radius: 50px;
   box-shadow: 0px 0px 33px #8270F2;
}
.create{
    color:white;
    font-size:200%;
    border: #8270F2 solid 2px;
    padding:10px;
    margin:10px;
    margin-bottom:0px;
    border-radius:200px;
    transition:0.5s;
}
.create_chat{
   position: relative;
   left: 90%;
}
.create:hover{
   color:black;
   background-color:white;
   transition:0.5s;
}
 </style>
 