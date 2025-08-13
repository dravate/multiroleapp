<template>
  <footer class="bg-gray-100 dark:bg-gray-900 text-gray-700 dark:text-gray-300 mt-10 border-t border-gray-200 dark:border-gray-700">
    <div class="max-w-7xl mx-auto px-6 py-8 grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Brand / Logo -->
      <div>
        <h2 class="text-2xl font-bold text-blue-600 dark:text-blue-400">YourAppName</h2>
        <p class="mt-2 text-sm">
          Empowering users with seamless role switching and a better experience.
        </p>
      </div>

      <!-- Quick Links -->
      <div>
        <h3 class="text-lg font-semibold mb-3">Quick Links</h3>
        <ul class="space-y-2">
          <li><NuxtLink to="/" class="hover:text-blue-500">Home</NuxtLink></li>
          <li><NuxtLink to="/about" class="hover:text-blue-500">About</NuxtLink></li>
          <li><NuxtLink to="/contact" class="hover:text-blue-500">Contact</NuxtLink></li>
          <li><NuxtLink to="/login" class="hover:text-blue-500">Login</NuxtLink></li>
        </ul>
      </div>

      <!-- Social Links -->
      <div>
        <h3 class="text-lg font-semibold mb-3">Connect</h3>
        <div class="flex space-x-4">
          <a href="#" target="_blank" class="hover:text-blue-500">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M..." /> <!-- Facebook SVG Path -->
            </svg>
          </a>
          <a href="#" target="_blank" class="hover:text-blue-500">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M..." /> <!-- Twitter SVG Path -->
            </svg>
          </a>
          <a href="#" target="_blank" class="hover:text-blue-500">
            <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M..." /> <!-- LinkedIn SVG Path -->
            </svg>
          </a>
        </div>
      </div>

    </div>

    <!-- Bottom Bar -->
    <div class="border-t border-gray-200 dark:border-gray-700 py-4 text-center text-sm">
      © {{ new Date().getFullYear() }} Sarathi Dravate Technologies LLP. All rights reserved.
    </div>
  </footer>
</template>

<style scoped>
/* You can adjust colors here if you want more vibrancy */
</style>
