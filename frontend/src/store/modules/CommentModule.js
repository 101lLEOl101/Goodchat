import CommentService from "@/services/CommentService";

export const comment = {
  namespaced: true,
  actions: {
    getComments(_, payload){
      return CommentService.getComments(payload.post_id).then(
        response => response.comments
      );
    }
  },
}