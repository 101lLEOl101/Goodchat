console.log()
if (window.location.pathname == "/profile") {
prof.classList.add("now-side_icon");
prof.classList.remove("side_icon");
i = prof.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
}
else if (window.location.pathname.indexOf("chatlist") >= 0 || window.location.pathname.indexOf("chat") >= 0) {
mes.classList.add("now-side_icon");
mes.classList.remove("side_icon");
i = mes.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
}
else if (window.location.pathname.indexOf("/settings") >= 0 || window.location.pathname.indexOf("settingsprofile") >= 0) {
set.classList.add("now-side_icon");
set.classList.remove("side_icon");
i = set.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
}
else if (window.location.pathname == "/") {
glob.classList.add("now-side_icon");
glob.classList.remove("side_icon");
i = glob.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
}
else if (window.location.pathname == "/bookmarks") {
book.classList.add("now-side_icon");
book.classList.remove("side_icon");
i = book.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
}
else if (window.location.pathname == "/addpost") {
add.classList.add("now-side_icon");
add.classList.remove("side_icon");
i = add.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
}
else if (window.location.pathname == "/findfriend") {
f.classList.add("now-side_icon");
f.classList.remove("side_icon");
i = f.querySelector('.hr').querySelector('.icona');
i.classList.add("now-icona");
i.classList.remove("icona");
}



