<template>
  <div class="friend_box">
    <div class="title_h">
        <h2 class="requests_h1" id = "title">Developer Page</h2>
    </div>
    <div style = "border: 2px solid #FFD700;"  class="friendlist_item" id="friend_item">
                <img style = "border: 2px solid #FFD700;" src="@/assets/killua.jpg" class="friend-avatar image_avatar">
                <a class="friend_name">Егор Назайкин</a>
                <p>- Гл. Бекендер </p>
                <img style="margin-left: auto; width: 5%; cover; aspect-ratio: 1/1; margin-right: 30px;" src="@/assets/pngwing.com.png">
    </div>
    <div style = "border: 2px solid #FFD700;"  class="friendlist_item" id="friend_item">
                <img style = "border: 2px solid #FFD700;" src="@/assets/TSEAdGqJQA0.jpg" class="friend-avatar image_avatar">
                <a class="friend_name">Леонид Кучук</a>
                <p>- Тимлид</p>
                <img style="margin-left: auto; width: 5%; cover; aspect-ratio: 1/1; margin-right: 30px;" src="@/assets/pngwing.com.png">
    </div>
    <div style = "border: 2px solid #FFD700;"  class="friendlist_item" id="friend_item">
                <img style = "border: 2px solid #FFD700;" src="@/assets/264x264-000000-80-0-0.jpg" class="friend-avatar image_avatar">
                <a class="friend_name">Давид Какубава</a>
                <p>- Фронтендер и бекендер</p>
                <img style="margin-left: auto; width: 5%; cover; aspect-ratio: 1/1; margin-right: 30px;" src="@/assets/pngwing.com.png">
    </div>
    <div style = "border: 2px solid #FFD700;"  class="friendlist_item" id="friend_item">
                <img style = "border: 2px solid #FFD700;" src="@/assets/f4a9f86d273f84cc8e2f632d0e168220.jpg" class="friend-avatar image_avatar">
                <a class="friend_name">Михаил Шатохин</a>
                <p>- Гл. Фронтендер</p>
                <img style="margin-left: auto; width: 5%; cover; aspect-ratio: 1/1; margin-right: 30px;" src="@/assets/pngwing.com.png">
    </div>
    <div style = "border: 2px solid #FFD700;" class="friendlist_item" id="friend_item">
                <img style = "border: 2px solid #FFD700;" src="@/assets/Papich-seksualno-stonet-sadyas-na-shpagat.webp" class="friend-avatar image_avatar">
                <a class="friend_name">Марк Камалитдинов</a>
                <p>- Фронтендер и дизайнер</p>
                <img style="margin-left: auto; width: 5%; cover; aspect-ratio: 1/1; margin-right: 30px;" src="@/assets/pngwing.com.png">
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/images.jpeg" class="friend-avatar image_avatar">
                <a class="friend_name">Данила Дерябин</a>
                <p>- Фронтендер</p>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/tumblr_3b537417ba9240a06cbb4cbe5e1aab6b_d0beb585_540.jpg" class="friend-avatar image_avatar">
                <a class="friend_name">Николай Прошурин</a>
                <p>- Фронтендер</p>
    </div>
    <div  class="friendlist_item" id="friend_item">
                <img src="@/assets/3eab185eeb793ec135ba112b0975ad89--k-on-sleep.jpg" class="friend-avatar image_avatar">
                <a class="friend_name">Анна Гордиенко</a>
                <p>- Бекендерша</p>
    </div>
</div>
</template>

<script>
export default {

}
</script>

<style>
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