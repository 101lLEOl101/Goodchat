import { createRouter, createWebHistory } from 'vue-router'
import UserManager from '@/managers/UserManager'
import RegistrationPage from '@/views/RegistrationPage'
import LoginPage from '@/views/LoginPage'
import ProfilePage from '@/views/ProfilePage'
import NotFoundPage from '@/views/NotFoundPage'
import SettingsPage from '@/views/SettingsPage'
import FeedPage from '@/views/FeedPage'
import ChatPage from '@/views/ChatPage'
import ChatListPage from '@/views/ChatListPage'
import PostPage from '@/views/PostPage'
import BookmarksPage from '@/views/BookmarksPage'


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
    path: '/feed',
    name: 'feed',
    component: FeedPage
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
  },
  {
    path: '/post/:id',
    props: true,
    name: 'post',
    component: PostPage,
  },
  {
    path: '/bookmarks',
    name: 'bookmarks',
    component: BookmarksPage,
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
