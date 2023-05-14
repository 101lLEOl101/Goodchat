import UserService from '@/services/UserService';
import UserManager from '@/managers/UserManager';

let initialState = {user: UserManager.getUser()}; 
export const user = {
  namespaced: true,
  state: initialState,
  mutations: {
    loadSelfUser(state) {
      state.user = UserManager.getUser();
    }
  },
  actions: {
    getUser({ state }, payload) {
      return UserService.getUser(payload.id)
        .then(
          response => {
            return response.user;
          },
          error => {
            return Promise.reject('User does not exist');
          }
        )
    },
    isUserSelf({ state }, payload) {
      return state.user.id == payload.id;
    },
  }
}