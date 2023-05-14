import { createStore } from 'vuex'
import { auth } from '@/store/modules/AuthModule'
import { user } from '@/store/modules/UserModule'

export default createStore({
  modules: {
    auth,
    user,
  }
})
