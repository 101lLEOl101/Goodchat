<template>
    <div  class="friendrequest_item" id="request_item">
                <img :src="inviter.avatar" class="friend-avatar image_avatar">
                <a class="friend_name" href="{% url 'profile' inviter.id %}">{{ inviter.full_name }}</a>
                <a class="button_write accept" href="{% url 'add-friend' inviter.id%}">Accept</a>
                <a class="button_write reject" href="{% url 'reject_request_friend' inviter.id%}">Deny</a>
    </div>
</template>

<script>
export default {
    props:{
        inviter: Object,
    }
}
</script>
<style>
.friendrequest_item{
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