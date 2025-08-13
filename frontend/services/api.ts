// services/api.ts
import axios from 'axios'

export const useApi = () => {
  const config = useRuntimeConfig()
  const baseURL = config.public.API_BASE_URL

  const instance = axios.create({
    baseURL,
    headers: {
      'Content-Type': 'application/json',
    },
  })

  // Attach token dynamically before every request
  instance.interceptors.request.use(
    (config) => {
      const token = localStorage.getItem('accessToken')
      if (token) {
        config.headers['Authorization'] = `Token ${token}`  // or `Token` if your backend expects that
      }
      return config
    },
    (error) => Promise.reject(error)
  )

  return instance
}

