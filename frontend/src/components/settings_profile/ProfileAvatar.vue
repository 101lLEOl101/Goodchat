<template>
	<div id="profile_avatar" class="settings_settings_devider">
		<h3 class="settings_block_tittle">Profile Picture</h3>
		<div class="settings_change_menu">
			<div class="input-file-row" id="box-img">
				<label class="input-file" id="add_btn" style="visibility: hidden; width: 0px; height: 0px; margin: 0px;" @change="open($event)">
					<input @change="updateAvatar" type="file" name="avatar-profile-form" accept="image/*" id="id_photo" value="">
					<span>Select an Image</span>
				</label>
				<div @change="change" id="input-list" class="input-file-list" style="margin: 0px auto;">
					<div class="input-file-list-item">
						<a href="#" onclick="removeFilesItem(this); return false;" class="input-file-list-remove">x</a>
						<img class="input-file-list-img" src="@/assets/logo.png">
					</div>
				</div>
			</div>
			<div class="settings_info_box">
				<p id="img-name" class="displayed_info">{{ namephoto }}</p>
			</div>
		</div>
	</div>
</template>

<script>
import { addImageCodeFragment } from "@/utils/ImgAdd.js"
import jQuery from "jquery";
const $ = jQuery;
window.$ = $;
let dt = new DataTransfer();
export default {
	data() {
		return {}
	},
	methods: {
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
.settings_settings_devider {
	color: #ffffff;
	width: 100%;
	height: fit-content;
	border-bottom: 1px solid #ffffff;
	padding-bottom: 1%;
	margin-bottom: 0;
}

.settings_block_tittle {
	color: #ffffff;
	text-align: left;
	padding-left: 5%;

}

.settings_change_menu {
	margin-top: 2%;

}


.input-file-row {
	display: flex;
	margin: 10px;
	border: 2px dashed #ffffff;
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
	color: #ffffff;
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

.input-file-list-img {
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

.settings_info_box {
	margin-left: 2%;
	display: block;
	margin-top: 0%;
	vertical-align: top;
}

.displayed_info {
	color: #ffffff;
	padding: 0.5%;
	background-color: #000000;
	width: fit-content;
	border: 1px solid #ffffff;
	border-radius: 16px;

}
</style>