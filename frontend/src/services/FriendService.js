import $axios from "@/axios";

class FriendService {
  getFriendList(id){
    let url = `friendlist/${id}`;
    return $axios.get(url).then(
      response => response.data
    );
  }

  getFriendRequestList() {
    let url = 'friend/request/list';
    return $axios.get(url).then(
      response => response.data
    );
  }

  getFriendshipStatus(id) {
    let url = `friendship/status/${id}`;
    return $axios.get(url).then(
      response => response.data
    );
  }

  refuseFriendship(data) {
    let url = 'friendship/refuse';
    return $axios.post(url, data).then(
      response => console.log(response.status)
    )
  }

  sendFriendRequest(id) {
    let url = `friend/request/send/${id}`;
    return $axios.get(url).then(
      response => response.data
    );
  }

  withdrawFriendRequest(id) {
    let url = `friend/request/withdraw/${id}`;
    return $axios.get(url).then(
      response => response.data
    );
  }

  acceptFriendRequest(id) {
    let url = `friend/request/accept/${id}`;
    return $axios.get(url).then(
      response => response.data
    );
  }

  declineFriendRequest(id) {
    let url = `friend/request/decline/${id}`;
    return $axios.get(url).then(
      response => response.data
    );
  }
}

export default new FriendService();