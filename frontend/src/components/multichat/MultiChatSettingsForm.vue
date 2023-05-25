<template>
  <form id="members-form" method="POST" enctype="multipart/form-data">
        <div class="input-img">
        {% if chat_avatar_name %}
            <div class="input-file-row" id="box-img">
						    <label class="input-file" id="add_btn" style="visibility: hidden; width: 0px; height: 0px; margin: 0px;">
						    <input type="file" name="chat-photo-form" accept="image/*" id="id_photo" value="{{chat_avatar_value}}">
						    <span>Select an Image</span>
						    </label>
					        <div id="input-list" class="input-file-list" style="margin: 0px auto;">
                                <div class="input-file-list-item">
                                    <a href="#" onclick="removeFilesItem(this); return false;" class="input-file-list-remove">x</a>
                                    <img class="input-file-list-img" src="{{chat_avatar_url}}">
                                </div>
                            </div>
				        </div>
        <input id = 'is_del' name="is_del" type="text" style="display: none;" value="0">
        {% else %}
        <div class="input-file-row" id="box-img">
						<label class="input-file" id="add_btn">
						<input type="file" name="chat-photo-form" accept="image/*" id="id_photo" >
						<span>Choose an Image</span>
						</label>
					<div id="input-list" class="input-file-list"></div>
        </div>
        <div class = "settings_info_box">
            <p class ="displayed_info">{{chat.avatar.name}}</p>
        </div>
         </div>
        <div class="members" id="members">
            <div class="input-chat">
                <input type="text" id="chat-name-input" name="chat-name-form" value="{{ chat_name }}" placeholder="Name">
            </div>
            
        </div>
            <div class="invitable">
                <label for="invitable">Invitable:</label>
                    <div  class="friendlist_item">
                        <img :src="member.avatar" class="friend-avatar">
                        <a class="friend_name" href="{% url 'profile' member.id %}">{{ member.name }} {{ member.surname }}</a>
                        <!-- <span class="friend_name">{{ member.access_description }}</span> -->
                        <input type="checkbox" name="members-checkbox-form" value="{{ member.id }}">
                    </div>
            </div>
            <div class="banned">
                <label for="banned">Banned:</label>
                    <div  class="friendlist_item">
                        <img :src="member.avatar" class="friend-avatar">
                        <a class="friend_name" href="{% url 'profile' member.id %}">{{ member.name }} {{ member.surname }}</a>
                        <span class="friend_name">{{ member.access_description }}</span>
                        <input type="checkbox" name="members-checkbox-form" value="{{ member.id }}">
                    </div>
            </div>
    </form>
</template>

<script>
export default {

}
</script>

<style>

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


.input-file-row {
	display: flex;
	margin: 10px auto;
	border: 2px dashed #8270F2;
	border-radius: 100%;
	width: fit-content;
	height: 10vw;
}
.input-file {
	position: relative;
	display: inline-block;
	margin: auto;
}
.input-file span {
	position: relative;
	cursor: pointer;
	outline: none;
	text-decoration: none;
	font-size: 14px;
    display: table-cell;
    vertical-align: middle;
	color: #8270F2;
	text-align: center;
	border-radius: 100%;
	background-color: black;
	line-height: 22px;
	height: 10vw;
	box-sizing: border-box;
	border: none;
	margin: 0;
	transition: background-color 0.2s;
	width:10vw;
}
.input-file input[type=file] {
	position: absolute;
	z-index: -1;
	opacity: 0;
	display: block;
	width: 0;
	height: 0;
}

/* Focus */
.input-file input[type=file]:focus + span {
	box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25);
}

/* Hover/active */
.input-file:hover span {
	background-color: #1F1F1F;
}
.input-file:active span {
	background-color: #0F0F0F;
}

/* Disabled */
.input-file input[type=file]:disabled + span {
	background-color: #eee;
}

/* Список c превью */

.input-file-list-item {
	display: inline-block;
	vertical-align: top;
	position: relative;
}
.input-file-list-item img {
	height: 10vw;
	border-radius: 100%;
	aspect-ratio: 1/1;
	object-fit: cover;
}
.input-file-list-name {
	text-align: center;
	display: block;
	font-size: 12px;
	color: white;
	text-overflow: ellipsis;
	overflow: hidden;
}
.input-file-list-remove {
	color: #fff;
	text-decoration: none;
	display: inline-block;
	position: absolute;
	padding: 0;
	margin: 0;
	top: 5px;
	right: 5px;
	background: #ff0202;
	width: 16px;
	height: 16px;
	text-align: center;
	line-height: 16px;
	border-radius: 50%;
}

input[type="text"]{
	background-color: #000000;
    border-radius: 12px;
    border: #8270F2 solid 2px;
    padding: 15px;
    color: #797979;
    width: 250px;
    margin-bottom: 15px;
    font-size: 20px;
}

/* .custom-checkbox {
	position: absolute;
	opacity: 0;
  } */

  
  .input-chat{
	display: flex;
	justify-content: center;
  }
  .input-img{
	display: grid;
	justify-content: center;
	margin-top: 2em;
  }

.settings_info_box{
    margin-left: 2%;
    display: block;
    margin-top: 0%;
    vertical-align: top;
}
.displayed_info{
    text-align: center;
}
</style>