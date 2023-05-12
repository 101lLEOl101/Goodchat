import axios from 'axios';
import TokenManager from '@/managers/TokenManager';
import UserManager from '@/managers/UserManager';

const BASE_URL = "http://localhost:8000/";

class AuthService {
  login(user) {
    let route = "api/token";
    let url = BASE_URL + route;
    let data = {
      username: user.username,
      password: user.password,
    };
    return axios
      .post(url, data)
      .then(
        (response) => {
          if (response.data) {
            TokenManager.setToken(response.data);
            return UserManager.loadUser();
          }

          return response.data;
        },
      );
  }

  logout() {
    TokenManager.removeToken();
    UserManager.removeUser();
  }

  register(user) {
    let route = "api/register";
    let url = BASE_URL + route;
    let data = {
      name: user.name,
      surname: user.surname,
      login: user.login,
      email: user.email,
      password: user.password,
    };
    return axios.post(url, data);
  }
}

export default new AuthService();
