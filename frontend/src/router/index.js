import { createRouter, createWebHistory } from 'vue-router'
import UserManager from '@/managers/UserManager'
import RegistrationPage from '@/views/RegistrationPage'
import LoginPage from '@/views/LoginPage'
import ProfilePage from '@/views/ProfilePage'
import NotFoundPage from '@/views/NotFoundPage'
import SettingsPage from '@/views/SettingsPage'
import MainPage from '@/views/MainPage'
import ChatPage from '@/views/ChatPage'
import ChatListPage from '@/views/ChatListPage'

const routes = [
  {
    path: '/registration',
    name: 'registration',
    component: RegistrationPage
  },
  {
    path: '/settings',
    name: 'settings-page',
    component: SettingsPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/',
    name: 'home',
    component: MainPage
  },
  {
    path: '/profile/:id',
    props: true,
    name: 'profile',
    component: ProfilePage
  },
  { 
    path: '/:pathMatch(.*)*', 
    name: 'NotFound', 
    component: NotFoundPage 
  },
  {
    path: '/chat',
    name: 'chat',
    component: ChatPage,
  },
  {
    path: '/chatlist',
    name: 'chatlist',
    component: ChatListPage,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login', '/registration'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = UserManager.getUser();

  if (authRequired && !loggedIn) {
    return next('/login');
  }

  next();
})

export default router;
