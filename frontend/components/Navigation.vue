<template>
  <nav
    class="bg-white dark:bg-gray-900 shadow px-6 py-4 flex justify-between items-center transition-colors duration-300"
  >
    <!-- Left Section: Links -->
    <div class="flex items-center space-x-8">
      <NuxtLink
        to="/"
        class="text-xl font-bold text-gray-800 dark:text-gray-100 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
      >
        Home
      </NuxtLink>
      <NuxtLink
        to="/about"
        class="text-lg text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
      >
        About Us
      </NuxtLink>
      <NuxtLink
        to="/contact"
        class="text-lg text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
      >
        Contact
      </NuxtLink>
    </div>
<!-- Right Section: Auth -->
<div class="relative flex items-center space-x-4">
  <!-- Dark Mode Toggle -->
  <button
    @click="toggleDarkMode"
    class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
  >
    <span v-if="isDark">🌙</span>
    <span v-else>☀️</span>
  </button>

  <template v-if="isLoggedIn">
    <!-- Dropdown Trigger -->
    <div class="relative">
      <button
        @click="toggleDropdown"
        class="flex items-center space-x-2 hover:text-blue-600 dark:hover:text-blue-400 transition-colors"
      >
        <span class="text-lg font-medium">{{ username }}</span>
        <svg
          class="w-5 h-5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      <!-- Dropdown Menu -->
      <div
        v-if="dropdownOpen"
        class="absolute top-full right-0 mt-2 w-56 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg shadow-lg overflow-hidden z-50 transition-all duration-200"
      >
        <button
          @click="handleSwapRole"
          class="block w-full text-left px-4 py-2 text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700"
        >
          🔄 Switch to {{ otherRole }}
        </button>
        <div class="border-t border-gray-200 dark:border-gray-700"></div>
        <NuxtLink
          to="/"
          @click="loginStore.logout()"
          class="block w-full text-left px-4 py-2 text-red-600 dark:text-red-400 hover:bg-gray-100 dark:hover:bg-gray-700"
        >
          🚪 Logout
        </NuxtLink>
      </div>
    </div>
  </template>

  <template v-else>
    <NuxtLink
      to="/login"
      class="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700 transition-colors"
    >
      Login
    </NuxtLink>
  </template>
</div>

  </nav>
</template>


<script lang="ts" setup>
import { ref, computed, onMounted } from "vue";
import { useLoginStore } from "@/stores/login";
import { useRouter } from "vue-router";

const loginStore = useLoginStore();
const router = useRouter();

const isLoggedIn = computed(() => loginStore.isAuthenticated);
const username = computed(() => loginStore?.username || "User");
const currentRole = computed(() => loginStore.role);
const otherRole = computed(() =>
  currentRole.value === "client" ? "business" : "client"
);

const dropdownOpen = ref(false);
const isDark = ref(false);

function toggleDropdown() {
  dropdownOpen.value = !dropdownOpen.value;
}

async function handleSwapRole() {
  const res = await loginStore.swapRole(otherRole.value);
  if (res.success) {
    dropdownOpen.value = false;
    const role = loginStore.user?.role || "client";
    if (res.role === "business") {
      router.push("/business");
    } else {
      router.push("/clients");
    }
  }
}

function toggleDarkMode() {
  isDark.value = !isDark.value;
  document.documentElement.classList.toggle("dark", isDark.value);
  localStorage.setItem("theme", isDark.value ? "dark" : "light");
}

onMounted(() => {
  isDark.value = localStorage.getItem("theme") === "dark";
  document.documentElement.classList.toggle("dark", isDark.value);
});

</script>


<style scoped>
/* Optional: Close dropdown when clicking outside */
</style>

