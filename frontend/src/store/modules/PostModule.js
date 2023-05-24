import PostService from '@/services/PostService'

export const post = {
  namespaced: true,
  actions: {
    async getPost(_, payload) {
      return PostService.getPost(payload.id).then(
        response => response.post,
      );
    },
    async getUserPosts(_, payload) {
      return PostService.getUserPosts(payload.id).then(
        response => response.posts
      );
    },
    async getFeed() {
      return PostService.getFeed().then(
        reponse => reponse.posts
      );
    },
    async getBookmarks() {
      return PostService.getBookmarks().then(
        response => response.posts
      );
    },
    async addPost(_, payload) {
      let data = {
        photo: payload.photo,
        content: payload.content,
      };
      return PostService.addPost(data).then(
        response => response.id
      );
    }
  }
}