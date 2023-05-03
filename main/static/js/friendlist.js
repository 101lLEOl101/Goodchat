friend.classList.add("now-side_icon");
friend.classList.remove("side_icon");
i = friend.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");

var button = document.getElementById("btn_h2");
var button_2 = document.getElementById("btn_h1");
var title = document.getElementById("req_h1");
var title_2 = document.getElementById("req_h2");
var request = document.getElementById("request_item");
var friends = document.getElementById("friend_item");

button.addEventListener('click', function() {
        title.style.display = "none";
        button.style.display = "none";
        title_2.style.display = "block";
        button_2.style.display = "block";
        request.style.display = "flex";
        friends.style.display = "none";
        console.log("Кнопка нажата.");
});

button_2.addEventListener('click', function() {
        title.style.display = "block";
        button.style.display = "block";
        friends.style.display = "flex";
        title_2.style.display = "none";
        button_2.style.display = "none";
        request.style.display = "none";
        console.log("Кнопка_2 нажата.");
});