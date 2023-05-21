import CommentService from "@/services/CommentService";

export const comment = {
  namespaced: true,
  actions: {
    getComments(_, payload){
      return CommentService.getComments(payload.post_id).then(
        response => response.comments
      );
    },
    sendComment(_, payload){
      let data = {
        post_id: payload.post_id,
        content: payload.content,
      };
      return CommentService.sendComment(data).then(
        response => response.comment
      );
    }
  },
}