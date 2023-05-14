import $axios from "@/axios";

class UserService {
  getUser(id) {
    let url = `profile/${id}`;
    return $axios.get(url)
      .then(
        response => {
          return response.data;
        }
      );
  }
}

export default new UserService();