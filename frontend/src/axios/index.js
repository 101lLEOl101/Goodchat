import axios from "axios";
import TokenManager from "@/managers/TokenManager";
import UserManager from "@/managers/UserManager";
import authHeader from "@/utils/AuthHeader";
import { API_URL } from "@/config";

const $axios = axios.create({
  baseURL: API_URL,
  timeout: 1000,
});

$axios.interceptors.request.use(
  async (config) => {
    config.headers = {
      ...config.headers,
      ...authHeader(),
    };

    return config;
  },
  (error) => Promise.reject(error)
);

$axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const config = error.config;

    if (error.response.status === 401 && !config.sent) {
      config.sent = true;
      const result = await TokenManager.refreshToken().then((response) => response);

      if (result.access) {
        config.headers = {
          ...config.headers,
          Authorization: `Bearer ${result.access}`,
        };
      } else {
        TokenManager.removeToken();
        UserManager.removeUser();
        location.reload(true);
      }

      return $axios(config);
    }

    return Promise.reject(error);
  }
);

export default $axios;
