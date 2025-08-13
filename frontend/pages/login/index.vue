<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100 dark:bg-gray-900">
    <div class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-md w-full max-w-md">
      <h2 class="text-2xl font-semibold text-gray-800 dark:text-white mb-6 text-center">
        Login
      </h2>

      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-1" for="username">Username</label>
          <input
            v-model="username"
            type="text"
            id="username"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-700 rounded focus:outline-none focus:ring focus:border-blue-500 dark:bg-gray-700 dark:text-white"
          />
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-1" for="password">Password</label>
          <input
            v-model="password"
            type="password"
            id="password"
            required
            class="w-full px-4 py-2 border border-gray-300 dark:border-gray-700 rounded focus:outline-none focus:ring focus:border-blue-500 dark:bg-gray-700 dark:text-white"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded transition"
        >
          Login
        </button>
      </form>

      <div class="mt-4 flex justify-between text-sm text-gray-600 dark:text-gray-300">
        <NuxtLink to="/login/forgot-password" class="hover:underline">Forgot Password?</NuxtLink>
        <NuxtLink to="/login/register" class="hover:underline">New User? Register Yourself</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useLoginStore } from '@/stores/login'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const loginStore = useLoginStore()
const router = useRouter()

const handleLogin = async () => {
  const success = await loginStore.login(username.value, password.value)
  if (success) {

    console.log("The role is")
    const role = loginStore?.role || 'Client';
    console.log(role); 

    if (role === 'business') {
      router.push('/business')
    } else {
      router.push('/clients')
    }
  } else {
    // Optionally show a toast or error message
    alert('Invalid credentials, please try again.')
  }
}
</script>

