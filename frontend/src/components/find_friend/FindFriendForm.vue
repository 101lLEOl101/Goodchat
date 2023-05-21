<template>
<div class="input_friend">
	<form method="POST" class="form_friend">
		<input type="text" name="querry" class="search-id-input" placeholder="Search(ID/Name)" required="" id="id_querry">
		<button type="submit" class="btn_message">Search</button>
	</form>
</div>
</template>
<script>

</script>
<style>
.input_friend{
    margin: 0 auto;
}

.form_friend{
    width: 650px;
}

.search-id-input {
        margin-top: 2%;
        box-sizing: border-box;
        background-color: black;
        color: white;
        font-size: 40px;
        padding: 3%;
        width: 100%;
        height: 73px;
        border: 2px solid #FFFFFF;
        border-top-right-radius: 10px;
        border-top-left-radius: 10px;
}

.search-id-input::placeholder {
        color: white;
}

.btn_message{
    background-color: #000000;
    border: #8270F2 solid 2px;
    padding: 15px;
    color: #8270F2;
    width: 100%;
    font-size: 20px;
    transition: all 0.5s;
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
}

.btn_message:hover{
    background-color: rgba(255,255,255,60%);
}
</style>