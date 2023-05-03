friend.classList.add("now-side_icon");
friend.classList.remove("side_icon");
i = friend.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");

btn_h1.addEventListener('click', function() {
        document.getElementById("req_h1").style.display = "none";
});