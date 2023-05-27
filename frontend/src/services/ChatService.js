import $axios from '@/axios'

class ChatService {
  getChat(id) {
    let url = `chat/${id}`;
    return $axios.get(url).then(
      response => response.data
    );
  }

  getChatlist() {
    let url = 'chatlist';
    return $axios.get(url).then(
      response => {
        console.log(response.data)
        return response.data
      }
    );
  }

  getChatInfo(id) {
    let url = `chat/${id}/info`;
    return $axios.get(url).then(
      response => response.data
    );
  }

  sendMessage(data) {
    let url = 'chat/sendMessage';
    return $axios.post(url, data).then(
      response => response.data
    );
  }

  getDialogId(id) {
    let url = `dialog/get/${id}`;
    return $axios.get(url).then(
      response => response.data
    );
  }

  editChat(data) {
    let url = `chat/${data.id}/edit`;
    console.log(data)
    return $axios.postForm(url, data).then(
      response => response.data
    )
  }

  createChat(data) {
    let url = `chat/create`;
    console.log(data)
    return $axios.postForm(url, data).then(
      response => response.data
    )
  }

  getChatAccessMode(id) {
    let url = `chat/${id}/access`;
    return $axios.get(url).then(
      response => response.data
    )
  }

  leaveChat(id) {
    let url = `chat/${id}/leave`;
    return $axios.get(url).then(
      response => response.data
    )
  }
}

export default new ChatService();