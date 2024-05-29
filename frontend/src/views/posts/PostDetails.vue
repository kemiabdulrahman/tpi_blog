<template>
  <div class="container my-5">
    <div class="card">
      <!--  
      <img :src="post.image" class="card-img-top" alt="Post image">
      -->
      <div class="card-body">
        <h5 class="card-title">{{ post.title }}</h5>
        <p class="card-text">{{ post.content }}</p>
        <p class="card-text"><small class="text-muted"></small></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PostDetail',
  data() {
    return {
      post: {},
    };
  },
  created() {
    this.fetchPost();
  },
  methods: {
    fetchPost() {
      const postId = this.$route.params.id;
      axios.get(`http://localhost:8000/api/posts/${postId}/`)
        .then(response => {
          this.post = response.data;
        })
        .catch(error => {
          console.error('Error fetching post:', error);
        });
    },
  },
};
</script>

