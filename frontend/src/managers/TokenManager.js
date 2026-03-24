import axios from "axios";
import { API_URL } from "@/config";

class TokenManager {
  getToken() {
    const token = localStorage.getItem("token");
    if (token) return JSON.parse(token);
    return false;
  }

  setToken(token) {
    if (!token) return;
    if (!token.access || !token.refresh) return;

    localStorage.setItem("token", JSON.stringify(token));
  }

  refreshToken() {
    const url = `${API_URL}token/refresh`;
    const token = this.getToken();
    const data = {
      refresh: token.refresh,
    };

    return axios.post(url, data).then((response) => {
      if (response.data) {
        token.access = response.data.access;
        this.setToken(token);
      }

      return response.data;
    });
  }

  removeToken() {
    localStorage.removeItem("token");
  }
}

export default new TokenManager();
