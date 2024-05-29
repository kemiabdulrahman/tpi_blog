<template>
  <div class="container my-5">
    <PostList :searchQuery="searchQuery" />
  </div>
</template>

<script>
import PostList from '@/views/posts/PostList.vue';

export default {
  name: 'Home',
  components: {
    PostList,
  },

  props: {
    searchQuery: {
      type: String,
      default: ''
    }
  }
};
</script>

