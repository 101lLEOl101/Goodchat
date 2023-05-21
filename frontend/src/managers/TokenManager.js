import axios from 'axios';

class TokenManager {
  getToken() {
    let token = localStorage.getItem('token')
    if (token) return JSON.parse(token);
    return false
  }

  setToken(token) {
    if (!token) return
    if (!token.access || !token.refresh) return 

    localStorage.setItem('token', JSON.stringify(token));    
  }

  refreshToken() {
    let url = 'http://127.0.0.1:8000/api/token/refresh';
    let token = this.getToken();
    let data = {
      refresh: token.refresh, 
    };

    return axios
      .post(url, data)
      .then(response => {
        if (response.data){
          token.access = response.data.access;
          this.setToken(token);
        }

        return response.data;
      })
  }

  removeToken() {
    localStorage.removeItem('token');
  }
};

export default new TokenManager();