import $axios from '@/axios';

class UserManager {
  getUser() {
    let user = localStorage.getItem('user');
    if (user) return JSON.parse(user);
    return false;
  }
  setUser(user) {
    if (user.id && user.name && user.surname && user.login) {
      localStorage.setItem('user', JSON.stringify(user));
      return true;
    }
    return false;
  }
  removeUser() {
    localStorage.removeItem('user');
  }
  loadUser() {
    return $axios.get('profile/self')
      .then(response => {
        if (response.data)
          this.setUser(response.data.user);
        return response.data.user
      });
  }
}

export default new UserManager();