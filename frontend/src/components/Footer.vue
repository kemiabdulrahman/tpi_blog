<template>
  <footer class="footer mt-auto py-3 bg-light">
    <div class="container text-center">
      <span class="text-muted">Follow us on:</span>
      <div class="mt-2">
        <a href="https://www.facebook.com" class="text-muted me-3" target="_blank">
          <i class="fab fa-facebook fa-lg"></i>
        </a>
        <a href="https://www.twitter.com" class="text-muted me-3" target="_blank">
          <i class="fab fa-twitter fa-lg"></i>
        </a>
        <a href="https://www.instagram.com" class="text-muted me-3" target="_blank">
          <i class="fab fa-instagram fa-lg"></i>
        </a>
        <a href="https://www.linkedin.com" class="text-muted me-3" target="_blank">
          <i class="fab fa-linkedin fa-lg"></i>
        </a>
      </div>
      <div class="mt-2">
        <span class="text-muted">© 2024 Blog. All rights reserved.</span>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
};
</script>

<style scoped>
.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #f8f9fa;
  text-align: center;
}
</style>

