import FriendService from '@/services/FriendService';

export const friend = {
  namespaced: true,
  actions: {
    getFriendList(_, payload) {
      return FriendService.getFriendList(payload.id).then( 
        response => response.friends
      );
    },
    refuseFriendship({ rootGetters }, payload) {
      let data = {
        user1_id: rootGetters['auth/user'],
        user2_id: payload.friend_id,
      }
      return FriendService.refuseFriendship(data)
    }
  }
}; 