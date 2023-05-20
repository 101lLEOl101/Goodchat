import { createStore } from 'vuex'
import { auth } from '@/store/modules/AuthModule'
import { user } from '@/store/modules/UserModule'
import { post } from '@/store/modules/PostModule'

export default createStore({
  modules: {
    auth,
    user,
    post,
  }
})
