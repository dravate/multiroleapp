import { useApi } from './api'

export async function getCSRFToken() {
  const api = useApi()
  try {
    const response = await api.get('/csrf/')
    const csrfToken = response.data.csrfToken
    api.defaults.headers['X-CSRFToken'] = csrfToken
    return api
  } catch (error) {
    console.error('Failed to fetch CSRF token', error)
    throw error
  }
}
