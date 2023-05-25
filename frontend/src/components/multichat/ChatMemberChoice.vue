<template>
  <div>
  <label for="members">Members:</label>
                <div  class="friendlist_item">
                    <img :src="member.avatar" class="friend-avatar">
                    <a class="friend_name" href="{% url 'profile' member.id %}">{{ member.name }} {{ member.surname }}</a>
                    <span class="friend_name">{{ member.access_description }}</span>
                    <input type="checkbox" name="members-checkbox-form" checked value="{{ member.id }}">
                </div>
   </div>
</template>

<script>
export default {

}
</script>

<style>
.friend-avatar{
    margin-left: 2%;
    object-fit: cover;
    aspect-ratio: 1/1;
    width: 10%;
    border-radius: 100%;
}

.friend_name{
    color: #8270F2;
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
</style>