// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: false },
  modules: ['@nuxt/ui', '@nuxt/content', '@nuxt/image', '@pinia/nuxt'],
  css: ['~/assets/css/main.css'],
  pages: true,
  runtimeConfig: {
    public: {
       API_BASE_URL: process.env.NUXT_BASE_URL || 'http://localhost:8000',
    },
  },
  ssr: false,  // IMPORTANT: disables server-side rendering
  target: 'static',  // legacy but still helps clarify intent
  app: {
    baseURL: '/', // or use `/your-subfolder/` if hosting in subfolder
  },

})
