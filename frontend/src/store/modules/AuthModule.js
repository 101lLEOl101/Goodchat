import AuthService from '@/services/AuthService';
import UserManager from '@/managers/UserManager';

const user = UserManager.getUser();
const initialState = user
  ? { status: { loggedIn: true }, user: user }
  : { status: { loggedIn: false }, user: null };

export const auth = {
  namespaced: true,
  state: initialState,
  mutations: {
    loginSuccess(state, user) {
      state.status.loggedIn = true;
      state.user = user;
    },
    updateUser(state, user){
      state.user = user;
    },
    loginFailure(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
    logout(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
    registerSuccess(state) {
      state.status.loggedIn = false;
    },
    registerFailure(state) {
      state.status.loggedIn = false;
    },
  },
  actions: {
    login({ commit }, user) {
      return AuthService.login(user)
        .then(
          user => {
            commit('loginSuccess', UserManager.getUser());
            commit('user/setUser', user, {root: true});
            return Promise.resolve('login success');
          },
          error => {
            commit('loginFailure');
            return Promise.reject(error);
          }
        );
    },
    logout({ commit }) {
      AuthService.logout();
      commit('logout');
    },
    register({ commit }, user) {
      return AuthService.register(user).then(
        response => {
          console.log(response)
          if (response.data.status === 'ok') {
            commit('registerSuccess');
            return Promise.resolve(response.data);
          }
          else{
            commit('registerFailure');
            let error = {
              message: response.data.message,
              code: 900
            }
            return Promise.reject(error);
          }
        },
        error => {
          commit('registerFailure');
          return Promise.reject(error);
        }
      );
    },
    reloadUser({ commit }) {
      console.log('userreloaded');
      commit('updateUser', UserManager.getUser());
    }
  },
  getters: {
    user(store) {
      return store.user;
    }
  }
};
