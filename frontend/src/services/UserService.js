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

  findUser(querry) {
    let url =  'users/find';
    let data = {
      querry: querry,
    }
    return $axios.post(url, data).then(
      response => response.data
    );
  }

  editProfile(data){
    let url = 'profile/edit';

    console.log(data);
    return $axios.postForm(url, data).then(
      response => response.data
    )
  }
}

export default new UserService();