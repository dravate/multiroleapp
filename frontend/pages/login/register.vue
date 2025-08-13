<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
    <div class="bg-white dark:bg-gray-800 p-8 rounded shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-center text-gray-800 dark:text-gray-100">Register</h2>

      <form @submit.prevent="handleRegister">
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Email</label>
          <input
            v-model="email"
            type="email"
            required
            class="mt-1 w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:ring-blue-400 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
          />
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Password</label>
          <input
            v-model="password"
            type="password"
            required
            minlength="6"
            class="mt-1 w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:ring-blue-400 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
          />
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">Confirm Password</label>
          <input
            v-model="confirmPassword"
            type="password"
            required
            class="mt-1 w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:ring-blue-400 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
          />
          <p v-if="passwordMismatch" class="text-sm text-red-500 mt-1">Passwords do not match.</p>
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded disabled:opacity-50"
          :disabled="!canSubmit"
        >
          Register
        </button>
      </form>

      <div class="mt-6 text-center text-sm text-gray-600 dark:text-gray-300">
        Already have an account?
        <NuxtLink to="/login" class="text-blue-600 hover:underline">Login</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useLoginStore } from '@/stores/login'

const email = ref('')
const password = ref('')
const confirmPassword = ref('')

const loginStore = useLoginStore()

const passwordMismatch = computed(() => password.value !== confirmPassword.value)

const canSubmit = computed(() => {
  return (
    email.value &&
    password.value &&
    confirmPassword.value &&
    !passwordMismatch.value
  )
})

const handleRegister = async () => {
  console.log('handleRegister');
  if (!canSubmit.value) return

  try {
    await loginStore.registerUser({
      username: email.value,
      password: password.value,
      email: email.value,
    })
    // Optional: Redirect to login or dashboard
    navigateTo('/login')
  } catch (err) {
    console.error('Registration failed', err)
    // Show toast or error message here
  }
}
</script>

