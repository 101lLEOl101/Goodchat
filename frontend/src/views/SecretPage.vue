<template>
  <div class="friend_box">
    <div class="title_h">
        <h2 class="requests_h1" id = "title">Developer Page</h2>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/killua.jpg" class="friend-avatar image_avatar">
                <a class="friend_name">Егор Назайкин</a>
                <p>- Гл. Бекендер </p>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/TSEAdGqJQA0.jpg" class="friend-avatar image_avatar">
                <a class="friend_name">Леонид Кучук</a>
                <p>- Тимлид</p>ы
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/blank-profile-picture-973460_1280.webp" class="friend-avatar image_avatar">
                <a class="friend_name">Давид Какубава</a>
                <p>- Фронтендер и бекендер</p>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/blank-profile-picture-973460_1280.webp" class="friend-avatar image_avatar">
                <a class="friend_name">Марк Камалитдинов</a>
                <p>- Фронтендер и дизайнер</p>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/blank-profile-picture-973460_1280.webp" class="friend-avatar image_avatar">
                <a class="friend_name">Михаил Шатохин</a>
                <p>- Гл. Фронтендер</p>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/blank-profile-picture-973460_1280.webp" class="friend-avatar image_avatar">
                <a class="friend_name">Анна Гордиенко</a>
                <p>- Бекендерша</p>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/blank-profile-picture-973460_1280.webp" class="friend-avatar image_avatar">
                <a class="friend_name">Николай Прошурин</a>
                <p>- Фронтендер</p>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/blank-profile-picture-973460_1280.webp" class="friend-avatar image_avatar">
                <a class="friend_name">Данила Дерябин</a>
                <p>- Фронтендер</p>
    </div>
</div>
</template>

<script>
export default {

}
</script>

<style>
p{
  color: white;
}
.friend_name{
    color: white;
    width: 20%;
    text-align: center;
}
.friendlist_item{
    display: flex;
    justify-content: start;
    align-items: center;
    width: 98%;
    background-color: black;
    border: 1px solid #8270F2;
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
    box-shadow: 0px 0px 5px #8270F2;
}


.friend-avatar{
    margin-left: 2%;
    width: 10%;
    border-radius: 100%;
    object-fit: cover;
    aspect-ratio: 1/1;
}
.title_h{
    display:flex;
    align-items: center;
}
.friend_box{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    width:110vh;
    
    background-color: rgba(0,0,0,50%);
    box-shadow: 0px 0px 10px #8270F2;
    border: black solid 5px;
    border-radius: 14px;
    margin: 0 auto;
    position: relative;
    top: 15vh;
    padding: 20px;
}
</style>