import axios from "axios";
import TokenManager from "@/managers/TokenManager";
import UserManager from "@/managers/UserManager";
import { API_ORIGIN } from "@/config";

const BASE_URL = `${API_ORIGIN}/`;

class AuthService {
  login(user) {
    const route = "api/token";
    const url = BASE_URL + route;
    const data = {
      username: user.username,
      password: user.password,
    };

    return axios.post(url, data).then((response) => {
      if (response.data) {
        TokenManager.setToken(response.data);
        return UserManager.loadUser();
      }

      return response.data;
    });
  }

  logout() {
    TokenManager.removeToken();
    UserManager.removeUser();
  }

  register(user) {
    const route = "api/register";
    const url = BASE_URL + route;
    const data = {
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
