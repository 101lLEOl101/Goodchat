<template>
  <div  class="friendlist_item" id="friend_item">
                <img :src="friend.avatar" class="friend-avatar image_avatar">
                <a class="friend_name" href="{% url 'profile' friend.id %}">{{ friend.full_name }}</a>
                <a class="button_write accept" href="{% url 'add-friend' friend.id %}">Delete</a>
                <a class="button_write reject" href="{% url 'open-dialog' friend.id %}">Message</a>
            </div>
</template>

<script>
export default {
    props: {
        friend: Object,
    },
}
</script>

<style>
.button_write{
    display:block;
    padding: 10px;
    border-radius: 5px;
    background-color: black;
    border: solid 1px #8270F2;
    color: #8270F2;
    text-align: center;
    box-shadow: 0px 0px 10px #8270F2;
    transition: all 0.3s;
    position: relative;
    left: 40%;
}
.button_write:hover{
    box-shadow: 0px 0px 40px #8270F2;
}
.friend_name{
    color: white;
    width: 20%;
    text-align: center;
}
.friend-avatar{
    margin-left: 2%;
    width: 10%;
    border-radius: 100%;
    object-fit: cover;
    aspect-ratio: 1/1;
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
.accept{
    left:44%;
}

.reject{
    left:45%;
}
</style>