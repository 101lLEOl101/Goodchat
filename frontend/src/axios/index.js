import axios from "axios";
import authHeader from "@/utils/AuthHeader";
import TokenManager from "@/managers/TokenManager";
import UserManager from "@/managers/UserManager";

const $axios = axios.create({
  baseURL: "https://goodchat.pythonanywhere.com/api/",
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
      const result = await TokenManager.refreshToken().then((result) => result);

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
