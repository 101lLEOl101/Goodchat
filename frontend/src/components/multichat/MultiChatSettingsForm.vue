<template>
	<h1 v-if=!IsEdit class="chat-info-title">New Multychat</h1>
	<h1 v-if=IsEdit class="chat-info-title">Settings Chat</h1>
	<form id="members-form" @submit.prevent enctype="multipart/form-data">
		<div class="input-img">
			<div v-if=IsEdit class="input-file-row" id="box-img">
				<label @change="open($event)" class="input-file" id="add_btn" style="visibility: hidden; width: 0px; height: 0px; margin: 0px;">
					<input type="file" name="chat-photo-form" accept="image/*" id="id_photo" value="">
					<span>Select an Image</span>
				</label>
				<div id="input-list" class="input-file-list" style="margin: 0px auto;">
					<div class="input-file-list-item">
						<a href="#" onclick="removeFilesItem(this); return false;" class="input-file-list-remove">x</a>
						<img class="input-file-list-img" :src="defaultAvatar">
					</div>
				</div>
			</div>
			<div v-else class="input-file-row" id="box-img">
				<label @change="open($event)" class="input-file" id="add_btn">
					<input type="file" name="chat-photo-form" accept="image/*" id="id_photo">
					<span>Choose an Image</span>
				</label>
				<div id="input-list" class="input-file-list"></div>
			</div>
			<div class="settings_info_box">
				<p id="img-name" class="displayed_info">currentavatar.png</p>
			</div>
		</div>
		<div class="members" id="members">
			<div class="input-chat">
				<input @input="updateName" class = "input-from-multychat" type="text" id="chat-name-input" name="chat-name-form" :value="name" placeholder="Name">
			</div>
		</div>
		<div class="invitable" v-if=!IsEdit>
			<label for="invitable">Friends:</label>
			<div 
				class="friendlist_item" 
				v-for="member in invitable"
				:key="member.id"
			>
				<img class="friend-avatar" :src="member.avatar">
				<router-link class="friend_name" :to="`/profile/${member.id}`"></router-link>
				<span class="friend_name">{{ member.name }} {{ member.surname }}</span>
				<input type="checkbox" name="members-checkbox-form" v-model="member.checked">
			</div>
		</div>
		<div class="invitable" v-if=IsEdit>
			<label for="invitable">Members:</label>
			<div 
				class="friendlist_item" 
				v-for="member in members"
				:key="member.id"
			>
				<img class="friend-avatar" :src="member.avatar">
				<router-link class="friend_name" :to="`/profile/${member.id}`"></router-link>
				<span class="friend_name">{{ member.name }} {{ member.surname }}</span>
				<input type="checkbox" name="members-checkbox-form" v-model="member.checked">
			</div>
		</div>
		<div style="margin-bottom: 20px;" class="invitable" v-if=IsEdit>
			<label for="invitable">Invitable:</label>
			<div 
				class="friendlist_item" 
				v-for="member in invitable"
				:key="member.id"
			>
				<img class="friend-avatar" :src="member.avatar">
				<router-link class="friend_name" :to="`/profile/${member.id}`"></router-link>
				<span class="friend_name">{{ member.name }} {{ member.surname }}</span>
				<input type="checkbox" name="members-checkbox-form" v-model="member.checked">
			</div>
		</div>
		<button @click="createChat" v-if=!IsEdit class="btn-save" type="submit" form="members-form">Create</button>
		<router-link v-if=!IsEdit to="/chatlist" class="btn-discard">Cancel</router-link>
		<button @click="editChat" v-if=IsEdit class="btn-save" type="submit" form="members-form">Save</button>
		<router-link v-if=IsEdit to="/chat/1/info" class="btn-discard" href="/chatlist">Cancel</router-link>
	</form>
</template>

<script>
import ChatMemberChoice from "@/components/multichat/ChatMemberChoice"
import { addImageCodeFragment } from "@/utils/ImgAdd.js";
import jQuery from "jquery";
const $ = jQuery;
window.$ = $;
let dt = new DataTransfer();

export default {
	components: {
		ChatMemberChoice,
	},
	data() {
		return {
			members: [],
			invitable: [],
		}
	},
	props: {
		IsEdit: Boolean,
		oldMembers: Array,
		oldInvitable: Array,
		name: String,
		id: Number,
		defaultAvatar: String,
	},
	methods: {
		updateName(event) {
			this.$emit('update:name', event.target.value);
		},
		editChat() {
			let withPhoto = !(document.getElementsByClassName("input-file-list-img").length == 0)
      let isPhotoOld = true;
			let photo = null;
			if (withPhoto){
				isPhotoOld = document.getElementById("id_photo").files.length == 0;
				if (!isPhotoOld){
					photo = document.getElementById("id_photo").files[0];
				}
			}

			let members = [
				...this.members.filter(member => member.checked),
				...this.invitable.filter(member => member.checked),
			]
			let members_id = [];

			members.forEach(member => {
				members_id.push(member.id);
			});

			let chatname = this.name;

			let data = {
				id: this.id,
				with_photo: withPhoto,
				photo_old: isPhotoOld,
				name: chatname,
				photo: photo,
				members: members_id,
			}

			console.log(data);
			this.$store.dispatch('chat/editChat', data).then(
				response => {
					this.$router.push(`/chat/${response}`);
				}
			);
		},
		createChat() {
			if (!this.name) {
				alert('Chat name is required')
				return false;
			};

			let withPhoto = !(document.getElementsByClassName("input-file-list-img").length == 0)
      let photo = document.getElementById("id_photo").files[0]

			let members = [
				...this.invitable.filter(member => member.checked),
			]
			let members_id = [];

			members.forEach(member => {
				members_id.push(member.id);
			});

			let chatname = this.name;

			let data = {
				with_photo: withPhoto,
				name: chatname,
				photo: photo,
				members: members_id,
			}

			console.log(data);
			this.$store.dispatch('chat/createChat', data).then(
				response => {
					this.$router.push(`/chat/${response}`);
				}
			);
		},
		open: function (event) {
			dt = new DataTransfer();
			let $files_list = $(document.getElementById("id_photo")).closest('.input-file').next();
			$files_list.empty();
			for (let i = 0; i < 1; i++) {
				let file = document.getElementById("id_photo").files.item(i);
				dt.items.add(file);
				let reader = new FileReader();
				reader.readAsDataURL(file);
				document.getElementById("img-name").innerHTML = file.name
				reader.onloadend = function () {
					let new_file_input = '<div style="display: inline-block; vertical-align: top; position: relative;" class="input-file-list-item">' +
						'<a href="#" onclick="removeFilesItem(this); return false;" style="color: #fff;text-decoration: none; display: inline-block; position: absolute; padding: 0; margin: 0; top: 5px; right: 5px; background: #ff0202; width: 16px; height: 16px; text-align: center; line-height: 16px; border-radius: 50%;" class="input-file-list-remove">x</a>' +
						'<img id="post-img" class="input-file-list-img" style="height: 10vw; border-radius: 100%; aspect-ratio: 1/1; object-fit: cover;" src="' + reader.result + '">' +
						'</div>';
					$files_list.append(new_file_input);
				}
			};
			document.getElementById("id_photo").files = dt.files;
			let btn = document.getElementById("add_btn");
			btn.style.visibility = "hidden";
			btn.style.width = '0';
			btn.style.height = '0';
			btn.style.margin = '0';
			document.getElementById("input-list").style.margin = "0 auto";
		},
	},
	watch: {
		oldMembers() {
			this.members = this.oldMembers;
		},
		oldInvitable() {
			this.invitable = this.oldInvitable;
		},
	},
	mounted() {
		if (document.body.getElementsByTagName("script").length == 0) {
			let tag = document.createElement("script");
			tag.setAttribute("src", "https://snipp.ru/cdn/jquery/2.1.1/jquery.min.js");
			document.body.appendChild(tag);
			const s = document.createElement("script");
			s.innerHTML = addImageCodeFragment;
			document.body.appendChild(s);
		}
	},
}
</script>

<style scoped>
.friendlist_item {
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

.friend-avatar {
	margin-left: 2%;
	object-fit: cover;
	aspect-ratio: 1/1;
	width: 10%;
	border-radius: 100%;
}

.btn-save {
    color: white;
    background-color: black;
    border: solid 2px #8270F2;
    border-radius: 20px;
    padding: 1rem;
	width: 10em;
	font-size: large;
	cursor: pointer;
}

.btn-discard{
	color: black;
    background-color: #8270F2;
    border: solid 2px #5a4daf;
    border-radius: 20px;
    padding: 1rem;
	width: 10em;
	font-size: large;
	cursor: pointer;
}

.friend_name {
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
	width: 10vw;
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
.input-file input[type=file]:focus+span {
	box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, .25);
}

/* Hover/active */
.input-file:hover span {
	background-color: #1F1F1F;
}

.input-file:active span {
	background-color: #0F0F0F;
}

/* Disabled */
.input-file input[type=file]:disabled+span {
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

.input-from-multychat {
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


.input-chat {
	display: flex;
	justify-content: center;
}

.input-img {
	display: grid;
	justify-content: center;
	margin-top: 2em;
}

.settings_info_box {
	margin-left: 2%;
	display: block;
	margin-top: 0%;
	vertical-align: top;
}

.displayed_info {
	text-align: center;
	margin: 10px auto;
}
</style>