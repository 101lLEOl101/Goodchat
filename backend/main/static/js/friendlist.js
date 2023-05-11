friend.classList.add("now-side_icon");
friend.classList.remove("side_icon");
i = friend.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
let requests = document.getElementsByClassName("friendrequest_item");
let friends = document.getElementsByClassName("friendlist_item");
btn.addEventListener('click', function() {
if (btn.innerHTML == 'Запросы в друзья'){
    for(let i = 0; i < requests.length; i++){
        requests[i].style.display = "flex";
    }
    for(let i = 0; i < friends.length; i++){
        friends[i].style.display = "none";
    }
    btn.innerHTML = 'Список Друзей'
    title.innerHTML = 'Запросы в друзья'
}
else if (btn.innerHTML == 'Список Друзей'){
    for(let i = 0; i < requests.length; i++){
        requests[i].style.display = "none";
    }
    for(let i = 0; i < friends.length; i++){
        friends[i].style.display = "flex";
    }
    btn.innerHTML = 'Запросы в друзья'
    title.innerHTML = 'Список Друзей'
}
});