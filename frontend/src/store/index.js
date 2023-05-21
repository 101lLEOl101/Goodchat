import { createStore } from 'vuex'
import { auth } from '@/store/modules/AuthModule'
import { user } from '@/store/modules/UserModule'
import { post } from '@/store/modules/PostModule'
import { chat } from '@/store/modules/ChatModule'
import { comment } from '@/store/modules/CommentModule'

export default createStore({
  modules: {
    auth,
    user,
    post,
    chat,
    comment,
  }
})
