import FriendService from '@/services/FriendService';

export const friend = {
  namespaced: true,
  actions: {
    getFriendList(_, payload) {
      return FriendService.getFriendList(payload.id).then( 
        response => response.friends
      );
    },
    getFriendRequestList() {
      return FriendService.getFriendRequestList().then(
        response => response.inviters
      )
    },
    refuseFriendship({ rootGetters }, payload) {
      let data = {
        user1_id: rootGetters['auth/user'].id,
        user2_id: payload.friend_id,
      }
      return FriendService.refuseFriendship(data)
    },
    getFriendshipStatus(_, payload) {
      return FriendService.getFriendshipStatus(payload.id).then(
        response => response.status
      )
    },
    sendFriendRequest(_, payload) {
      return FriendService.sendFriendRequest(payload.id)
    },
    withdrawFriendRequest(_, payload) {
      return FriendService.withdrawFriendRequest(payload.id)
    },
    acceptFriendRequest(_, payload) {
      return FriendService.acceptFriendRequest(payload.id)
    },
    declineFriendRequest(_, payload) {
      return FriendService.declineFriendRequest(payload.id)
    },
  }
}; 