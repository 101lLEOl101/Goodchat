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
import CreatePostPage from '@/views/CreatePostPage'
import FindFriendPage from '@/views/FindFriendPage'
import FriendListPage from '@/views/FriendListPage'
import SecretPage from '@/views/SecretPage'
import RequestListPage from '@/views/RequestListPage'
import SettingsProfilePage from '@/views/SettingsProfilePage'
import PostEditPage from '@/views/PostEditPage'
import MultichatInfoPage from '@/views/MultichatInfoPage'
import MultychatCreate from '@/views/MultychatCreate'
import MultyChatSettings from '@/views/MultyChatSettings'


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
    path: '/chat/:id',
    props: true,
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
  },
  {
    path: '/addpost',
    name: 'addpost',
    component: CreatePostPage,
  },
  {
    path: '/findfriend',
    name: 'findfriend',
    component: FindFriendPage,
  },
  {
    path: '/requestlist',
    name: 'requestlist',
    component: RequestListPage,
  },
  {
    path: '/friendlist/:id',
    props: true,
    name: 'friendlist',
    component: FriendListPage,
  },
  {
    path: '/editpost/:id',
    props: true,
    name: 'editpost',
    component: PostEditPage,
  },
  {
    path: '/settings/profile',
    name: 'settingsprofile',
    component: SettingsProfilePage,
  },
  {
    path: '/dev',
    name: 'dev',
    component: SecretPage,
  },
  {
    path: '/chat/:id/info',
    props: true,
    component: MultichatInfoPage,
  },

  {
    path: '/multychatcreate',
    component: MultychatCreate,
  },
  {
    path: '/chat/:id/edit',
    props: true,
    component: MultyChatSettings,
  },
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
