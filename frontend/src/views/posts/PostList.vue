<template>
  <div class="container">
    <h2 class="text-center mt-2 mb-5">Recent Posts</h2>

    <!-- Blog Post List -->
    <div class="row">
      <!-- Blog Post Cards -->
      <div class="col-md-8">
        <div class="row">
          <div class="col-md-6 mb-4" v-for="post in filteredPosts" :key="post.id">
            <div class="card h-100">
              <div class="card-body">
                <h5 class="card-title">{{ post.title }}</h5>
                <p class="card-text">{{ post.excerpt }}</p>
                <p>{{ new Date(post.created_at).toLocaleDateString() }}</p>
                <router-link :to="{ name: 'PostDetail', params: { id: post.id } }" class="btn btn-primary">Read More</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Sidebar -->
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Categories</h5>
            <ul class="list-group">
              <li class="list-group-item" v-for="category in categories" :key="category.id">{{ category.name }}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  props: {
    searchQuery: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      showCategory: false,
      posts: [],
      categories: [
        { id: 1, name: 'Politics' },
        { id: 2, name: 'Trading' },
        // Add more categories as needed
      ],
    };
  },

  created() {
    this.fetchPost();
  }, 

  methods: {
    fetchPost() {
      axios.get('http://localhost:8000/api/posts/')  // Adjust the URL to match your API endpoint
        .then(response => {
          this.posts = response.data;
        })
        .catch(error => {
          console.error('Error fetching post:', error);
        });
    },
  },

   computed: {
    filteredPosts() {
      if (!this.searchQuery) {
        return this.posts;
      }
      return this.posts.filter(post =>
        post.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  }

};
</script>


<style scoped>
.card {
  width: 100%;
}
</style>

