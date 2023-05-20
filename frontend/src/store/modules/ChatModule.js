import ChatService from "@/services/ChatService"

export const chat = {
  namespaced: true,
  actions: {
    async getChat(_, payload) {
      return ChatService.getChat(payload.id).then(response => response.chat);
    },
    async getChatlist() {
      return ChatService.getChatlist().then(
        response => response.chats
      );
    }
  }
}