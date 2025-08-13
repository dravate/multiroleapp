<template>
  <section class="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 text-white">
    <div class="text-center px-6 md:px-12">
      <!-- Role Badge -->
      <span class="inline-block px-4 py-1 bg-white/20 rounded-full text-sm font-medium mb-4">
        Current Role: Client
      </span>

      <!-- Hero Title -->
      <h1 class="text-4xl md:text-6xl font-extrabold mb-4">
        Welcome, Valued Client!
      </h1>

      <!-- Description -->
      <p class="max-w-2xl mx-auto text-lg md:text-xl mb-8 text-white/90">
        Explore our services, track your projects, and stay connected with your business partners.  
        Your journey to success starts here.
      </p>

      <!-- Action Button -->
      <button 
        class="px-6 py-3 bg-white text-indigo-600 rounded-full font-semibold shadow-lg hover:bg-indigo-100 transition">
        Get Started
      </button>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { useLoginStore } from '../../stores/login'


const router = useRouter()
const userStore =useLoginStore();

onMounted(() => {
  if (userStore.role === 'business') {
    router.replace('/business')
  }
})
</script>
