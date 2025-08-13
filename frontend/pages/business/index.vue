<template>
  <section class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-500 via-teal-500 to-cyan-500 text-white">
    <div class="text-center px-6 md:px-12">
      <!-- Role Badge -->
      <span class="inline-block px-4 py-1 bg-white/20 rounded-full text-sm font-medium mb-4">
        Current Role: Business
      </span>

      <!-- Hero Title -->
      <h1 class="text-4xl md:text-6xl font-extrabold mb-4">
        Welcome, Business Partner!
      </h1>

      <!-- Description -->
      <p class="max-w-2xl mx-auto text-lg md:text-xl mb-8 text-white/90">
        Manage your clients, track performance, and grow your business with the right tools — all in one place.
      </p>

      <!-- Action Button -->
      <button 
        class="px-6 py-3 bg-white text-green-600 rounded-full font-semibold shadow-lg hover:bg-green-100 transition">
        View Dashboard
      </button>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { useLoginStore } from '../../stores/login'


const router = useRouter()
const userStore = useLoginStore(); 

onMounted(() => {
  if (userStore.role === 'client') {
    router.replace('/clients')
  }
})
</script>
