import $axios from "@/axios";

class PostService {
  getPost(id) {
    let url = `post/${id}`;
    return $axios.get(url).then((response) => response.data);
  }

  getUserPosts(id) {
    let url = `post/getUserPosts/${id}`;
    return $axios.get(url).then((response) => response.data);
  }

  getFeed() {
    let url = "post/getFeed";
    return $axios.get(url).then((response) => response.data);
  }

  getBookmarks() {
    let url = "bookmarks";
    return $axios.get(url).then((response) => response.data);
  }

  addPost(data) {
    if (!data.photo && !data.content) return;

    let photo = data.photo ? data.photo : "";
    let content = data.content ? data.content : "";
    let url = "post/new";

    let form = new FormData();
    form.append("content", content);
    form.append("photo", photo);

    return $axios.post(url, form).then((response) => response.data);
  }

  editPost(data) {
    if (!data.withPhoto && !data.content) return;

    let url = `post/${data.id}/edit`;

    let form = new FormData();
    form.append("content", data.content);
    form.append("with_photo", data.withPhoto);
    form.append("photo_old", data.isPhotoOld);
    form.append("photo", data.photo);

    return $axios.post(url, form).then((response) => response.data);
  }

  deletePost(id) {
    let url = `post/${id}/delete`;
    return $axios.get(url).then((response) => response.data)
  }

  addDeleteBookmark(id) {
    let url = `post/${id}/bookmark`;
    return $axios.get(url).then(
      (response) => response.data
    )
  }
}

export default new PostService();
