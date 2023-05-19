<template>
    <div>
        <img class = "author_avatar" src = "{{post.author_photo.url}}">
        <router-link to="/profile/{{ post.author.id }}" class = "post-author">{{post.author.name}} {{ post.author.surname}}</router-link>
    </div>
</template>
<script>
export default {
    data() {
        return {}
    }
    
}
</script>
<style>

.post-author {
    color: white;
    margin-right: 4%;
    cursor: pointer;
    text-decoration: none;
}
.author_avatar{
    margin: 5.125px 30px;
	aspect-ratio: 1/1;
	object-fit: cover;
	height: 40px;
	width: 40px;
	border-radius: 100%;
	margin-left: auto;
}
</style>