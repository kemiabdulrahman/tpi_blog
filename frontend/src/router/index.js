import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Contact from '../views/Contact.vue'
import About from '../views/About.vue'
import PostList from '../views/posts/PostList.vue'
import PostDetail from '../views/posts/PostDetails.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    props: route => ({ searchQuery: route.query.searchQuery })
  },

  {
    path: '/about',
    name: 'About',
    component: About
  },

  {
      path: '/contact',
      name: 'Contact',
      component: Contact,
   },

  {
    path: '/posts',
    name: 'PostList',
    component: PostList,
  },

  {
    path: '/posts/:id',
    name: 'PostDetail',
    component: PostDetail,
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
