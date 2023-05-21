import $axios from "@/axios";

class CommentService {
  getComments(post_id){
    let url = `post/${post_id}/comments`;
    return $axios.get(url).then(
      response => response.data
    );
  }
}

export default new CommentService();