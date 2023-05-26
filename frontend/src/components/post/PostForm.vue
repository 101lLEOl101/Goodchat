<template>
	<div class="new-post-header">
		<button v-if=!isEdit class="btn_post" @click="createPost">Create Post</button>
		<button v-else class="btn_post" @click="editPost">Edit Post</button>
	</div>
	<div class="new-post-text-img">
		<form id="new-post-form" class="form-add-post" enctype="multipart/form-data">
			<textarea name="content" cols="40" rows="10" class="text-of-new-post" placeholder="Your text" required=""
				id="id_content" v-model="content"></textarea>
			<div v-if=!HaveImg class="input-file-row" id="box-img">
				<label class="input-file" id="add_btn" @change="open($event)">
					<input type="file" name="photo" accept="image/*" id="id_photo">
					<span>Add an Image</span>
				</label>
				<div id="input-list" class="input-file-list"></div>
			</div>
			<div v-else class="input-file-row" style="height: auto;" id="box-img">
				<label @change="open($event)" class="input-file" id="add_btn" style="visibility: hidden; width: 0px; height: 0px; margin: 0px;">
					<input type="file" name="avatar-profile-form" accept="image/*" id="id_photo" value="">
					<span>Select an Image</span>
				</label>
				<div id="input-list" class="input-file-list" style="margin: 0px auto;">
					<div class="input-file-list-item">
						<a href="#" onclick="removeFilesItem(this); return false;" class="input-file-list-remove">x</a>
						<img class="input-file-list-img" :src="oldPost.photo">
						<span id ="img-name" class="input-file-list-name"></span>
					</div>
				</div>
			</div>
		</form>
	</div>
</template>
<script>
import { addImageCodeFragment } from "@/utils/ImgAdd.js"
import jQuery from "jquery";
const $ = jQuery;
window.$ = $;
let dt = new DataTransfer();
export default {
	props: {
		isEdit: Boolean,
		HaveImg: Boolean,
		oldPost: Object,
	},
	data() {
		return {
			content: this.oldPost ? this.oldPost.content : '',
		}
	},
	methods: {
		createPost() {
			let photo = document.getElementById("id_photo").files[0]
			if (photo || this.content) {
				let data = {
					photo: photo,
					content: this.content,
				};
				this.$store.dispatch('post/addPost', data).then(
					response => this.$router.push(`/post/${response}`)
				);
			}
		},
		editPost() {
			let withPhoto = !(document.getElementsByClassName("input-file-list-img").length == 0)
			let isPhotoOld = true;
			let photo = null;
			if (withPhoto){
				isPhotoOld = document.getElementById("id_photo").files.length == 0;
				if (!isPhotoOld){
					photo = document.getElementById("id_photo").files[0];
				}
			}

			if (this.content || withPhoto){
				let post_data = {
					id: this.oldPost.id,
					content: this.content,
					withPhoto: withPhoto,
					isPhotoOld: null,
					photo: null,
				};
				if (withPhoto){
					post_data.isPhotoOld = isPhotoOld;
					if (!isPhotoOld){
						post_data.photo = photo;
					}
				}

				this.$store.dispatch('post/editPost', post_data).then(
					response => {
						this.$router.push(`/post/${response}`);
					}
				)
			}
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
				reader.onloadend = function () {
					let new_file_input = '<div class="input-file-list-item" style=" display: inline-block; vertical-align: top; position: relative;">' +
						'<img style="width: 50%; margin: 100px 25%; border-radius: 14px;" id="post-img" class="input-file-list-img" src="' + reader.result + '">' +
						'<span style="text-align: center; display: block; font-size: 12px; color: white; text-overflow: ellipsis; overflow: hidden;" id="img-name" class="input-file-list-name">' + file.name + '</span>' +
						'<a style ="color: #fff; text-decoration: none; display: inline-block; position: absolute; padding: 0; margin: 0; top: 5px; right: 5px; background: #ff0202; width: 16px; height: 16px; text-align: center; line-height: 16px; border-radius: 50%;" href="#" onclick="removeFilesItem(this); return false;" class="input-file-list-remove">x</a>' +
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
			document.getElementById("box-img").style.height = "auto";
			document.getElementById("input-list").style.margin = "0 auto";
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
.text-of-new-post {
	width: 96%;
	font-size: 16px;
	margin: 1%;
	padding: 1%;
	background: #000;
	color: white;
	border-radius: 14px;
	transition: all 0.5s;
	resize: none;
	border: 2px solid #362982;
}

.text-of-new-post::-webkit-scrollbar {
	width: 12px;
	/* ширина scrollbar */
}

.text-of-new-post::-webkit-scrollbar-track {
	background: black;
	/* цвет дорожки */
}

.text-of-new-post::-webkit-scrollbar-thumb {
	background-color: #8270F2;
	/* цвет плашки */
	border-radius: 17px;
	/* закругления плашки */
	border: 0px 10px 33px #8270F2;
	/* padding вокруг плашки */
}

.text-of-new-post:focus {
	box-shadow: 0px 15px 20px #362982;
}

.input-file-row {
	display: flex;
	border: 4px dashed #362982;
	border-radius: 14px;
	width: 96%;
	padding: 1%;
	margin: 1%;
	height: 30vh;
}

.input-file {
	position: relative;
	display: inline-block;
	margin: auto;
}

.input-file span {
	position: relative;
	display: inline-block;
	cursor: pointer;
	outline: none;
	text-decoration: none;
	font-size: 14px;
	vertical-align: middle;
	color: black;
	text-align: center;
	border-radius: 4px;
	background-color: #8270f2;
	line-height: 22px;
	height: 40px;
	padding: 10px 20px;
	box-sizing: border-box;
	border: none;
	margin: 0;
	transition: background-color 0.2s;
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
	background-color: #5b4bbe;
}

.input-file:active span {
	background-color: #362982;
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
	width: 50%;
	margin: 100px 25%;
	border-radius: 14px;
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
</style>