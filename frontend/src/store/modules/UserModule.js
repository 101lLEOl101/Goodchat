import UserService from '@/services/UserService';
import UserManager from '@/managers/UserManager';

let initialState = {user: UserManager.getUser()}; 
export const user = {
  namespaced: true,
  state: initialState,
  mutations: {
    setUser(state, user) {
      state.user = user;
    }
  },
  actions: {
    loadSelfUser({ commit }) {
      commit('setUser', UserManager.getUser());
    },
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
    findUser(_, payload) {
      return UserService.findUser(payload.querry).then(
        response => response.users
      );
    },
    editProfile({ dispatch }, payload) {
      let data = {
        name: payload.name,
        surname: payload.surname,
        about: payload.about,
        hobby: payload.hobby,
        city: payload.city,
        education: payload.education,
        company: payload.company,
        with_photo: payload.with_photo,
        photo_old: payload.photo_old,
        photo: payload.photo,
      }
  
      return UserService.editProfile(data).then(
        response => {
          UserManager.loadUser().then(
            user => {
              console.log(user);
              dispatch('loadSelfUser');
              dispatch('auth/reloadUser', {}, {root: true});
            }
          );
        }
      )
    }
  }
}