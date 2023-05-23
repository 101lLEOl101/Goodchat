import $axios from "@/axios";

class FriendService {
  getFriendList(id){
    let url = `friendlist/${id}`;
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
}

export default new FriendService();