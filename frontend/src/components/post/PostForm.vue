<template>
<div class="new-post-text-img">
	<form method="POST" id="new-post-form" class="form-add-post" enctype="multipart/form-data">
        <textarea name="content" cols="40" rows="10" class="text-of-new-post" placeholder="Your text" required="" id="id_content"></textarea>
		<div class="input-file-row" id="box-img">
			<label class="input-file" id="add_btn">
				<input type="file" name="photo" accept="image/*" id="id_photo">
				<span>Add an Image</span>
			</label>
			<div id="input-list" class="input-file-list"></div>
		</div>
	</form>
</div>
</template>
<script>
import $ from "jquery";
export default {
    data() {
    },
    mounted() {
      let recaptchaScript = document.createElement('script');
      recaptchaScript.setAttribute('src', 'https://snipp.ru/cdn/jquery/2.1.1/jquery.min.js');
      document.head.appendChild(recaptchaScript);
      let dt = new DataTransfer();
      $('.input-file input[type=file]').on('change', function(){
        let $files_list = $(this).closest('.input-file').next();
            $files_list.empty();
            for(let i = 0; i < 1; i++){
                let file = this.files.item(i);
                dt.items.add(file);
                let reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onloadend = function(){
                    let new_file_input = '<div class="input-file-list-item">' +
                        '<img class="input-file-list-img" src="' + reader.result + '">' +
                        '<span class="input-file-list-name">' + file.name + '</span>' +
                        '<a href="#" @click="show(this)" class="input-file-list-remove">x</a>' +
                    '</div>';
                    $files_list.append(new_file_input);
                }
            };
            this.files = dt.files;
            let btn = document.getElementById("add_btn");
            btn.style.visibility = "hidden";
            btn.style.width = '0';
            btn.style.height = '0';
            btn.style.margin = '0';
            document.getElementById("box-img").style.height = "auto";
            document.getElementById("input-list").style.margin = "0 auto";
            console.log(dt.files)
      });
    },
    methods: {
      show: function (target){
            let recaptchaScript = document.createElement('script');
            recaptchaScript.setAttribute('src', 'https://snipp.ru/cdn/jquery/2.1.1/jquery.min.js');
            document.head.appendChild(recaptchaScript);
            let input = $(target).closest('.input-file-row').find('input[type=file]');
            input[0].files = dt.files;
            document.getElementById('add_btn').removeAttribute("style");
            document.getElementById("box-img").removeAttribute("style");
            document.getElementById("input-list").removeAttribute("style");
            let dt = new DataTransfer();
      }
    }
}
</script>
<style>
.text-of-new-post {
    width: 96%;
    font-size: 16px;
    margin: 1%;
    padding: 1%;
    background: #000;
    color: white;
    border-radius: 14px;
    transition:all 0.5s;
    resize: none;
    border: 2px solid #362982;
}

.text-of-new-post::-webkit-scrollbar {
  width: 12px;               /* ширина scrollbar */
}
.text-of-new-post::-webkit-scrollbar-track {
  background: black;        /* цвет дорожки */
}
.text-of-new-post::-webkit-scrollbar-thumb {
  background-color: #8270F2;    /* цвет плашки */
  border-radius: 17px;       /* закругления плашки */
  border: 0px 10px 33px #8270F2;  /* padding вокруг плашки */
}

.text-of-new-post:focus{
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
.input-file input[type=file]:focus + span {
	box-shadow: 0 0 0 0.2rem rgba(0,123,255,.25);
}

/* Hover/active */
.input-file:hover span {
	background-color: #5b4bbe;
}
.input-file:active span {
	background-color: #362982;
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