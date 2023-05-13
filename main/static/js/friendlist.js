friend.classList.add("now-side_icon");
friend.classList.remove("side_icon");
i = friend.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
let requests = document.getElementsByClassName("friendrequest_item");
let friends = document.getElementsByClassName("friendlist_item");
btn.addEventListener('click', function() {
if (btn.innerHTML == 'Friend Request'){
    for(let i = 0; i < requests.length; i++){
        requests[i].style.display = "flex";
    }
    for(let i = 0; i < friends.length; i++){
        friends[i].style.display = "none";
    }
    btn.innerHTML = 'Friends List'
    title.innerHTML = 'Friend Request'
}
else if (btn.innerHTML == 'Friends List'){
    for(let i = 0; i < requests.length; i++){
        requests[i].style.display = "none";
    }
    for(let i = 0; i < friends.length; i++){
        friends[i].style.display = "flex";
    }
    btn.innerHTML = 'Friend Request'
    title.innerHTML = 'Friends List'
}
});