import ChatService from "@/services/ChatService"

export const chat = {
  namespaced: true,
  actions: {
    async getChat(_, payload) {
      return ChatService.getChat(payload.id).then(
        response => response.chat
      );
    },
    async getChatInfo(_, payload) {
      return ChatService.getChatInfo(payload.id).then(
        response => response
      )
    },
    async getChatlist() {
      return ChatService.getChatlist().then(
        response => response.chats
      )
    },
    async sendMessage(_, payload) {
      let data = {
        chat_id: payload.chat_id,
        content: payload.content,
      };
      return ChatService.sendMessage(data).then(
        response => response.message
      );
    },
    async getDialogId(_, payload){
      return ChatService.getDialogId(payload.id).then(
        response => response.dialog_id,
      )
    },
    async editChat(_, payload){
      return ChatService.editChat(payload).then(
        response => response.id,
      )
    },
    async createChat(_, payload){
      return ChatService.createChat(payload).then(
        response => response.id,
      )
    },
    async getChatAccessMode(_, payload) {
      return ChatService.getChatAccessMode(payload.id).then(
        response => response.mode
      )
    },
    async leaveChat(_, payload) {
      return ChatService.leaveChat(payload.id)
    }
  }
}