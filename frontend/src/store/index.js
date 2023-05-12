import { createStore } from 'vuex'
import { auth } from '@/store/modules/AuthModule'

export default createStore({
  modules: {
    auth,
  }
})
