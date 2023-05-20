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
      response => response.data
    );
  }
}

export default new ChatService();