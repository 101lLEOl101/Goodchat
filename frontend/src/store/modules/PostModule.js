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
    },
    async editPost(_, payload) {
      let data = {
        id: payload.id,
        content: payload.content,
        withPhoto: payload.withPhoto,
        isPhotoOld: payload.isPhotoOld,
        photo: payload.photo
      };

      return PostService.editPost(data).then(
        response => response.id
      )
    },
    async deletePost(_, payload) {
      return PostService.deletePost(payload.id)
    },
    async addDeleteBookmark(_, payload) {
      return PostService.addDeleteBookmark(payload.id).then(
        response => response.status
      )
    }
  }
}