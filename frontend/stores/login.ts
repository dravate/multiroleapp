import { defineStore } from 'pinia'
import { useApi } from '@/services/api'
import type { Userdata } from '@/types/user'
import { useRouter } from 'vue-router'


export const useLoginStore = defineStore('login', {
  state: () => ({
    accessToken: localStorage.getItem('accessToken') || '',
    userId: localStorage.getItem('userId') ? Number(localStorage.getItem('userId')) : null,
    email: localStorage.getItem('email') || '',
    username: localStorage.getItem('username') || '',
    role: localStorage.getItem('role') || '',
    resetLink: '',
  }),

  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },

  actions: {
    async login(email: string, password: string) {
      const username = email // sending as username per backend expectations
      try {
        const api = useApi()
        const response = await api.post('/authentication/', { username, password })
       

        const { token, user_id, email, role } = response.data

        // Store in state
        this.accessToken = token
        this.userId = user_id
        this.email = email
        this.username = username
        this.role = role

        // Persist to localStorage
        localStorage.setItem('accessToken', token)
        localStorage.setItem('userId', String(user_id))
        localStorage.setItem('email', email)
        localStorage.setItem('username', username)
        localStorage.setItem('role', role)

        return true
      } catch (error) {
        console.error('Login failed:', error)
        return false
      }
    },

    logout() {
      this.accessToken = ''
      this.userId = null
      this.email = ''
      this.username = ''
      this.role = ''

      localStorage.removeItem('accessToken')
      localStorage.removeItem('userId')
      localStorage.removeItem('email')
      localStorage.removeItem('username')
      localStorage.removeItem('role')
    },

    async registerUser(payload: Userdata) {
      try {
        const api = useApi()
        const response = await api.post('/register/', payload)
       
        return { success: true }
      } catch (error: any) {
        console.error('Registration failed:', error.response?.data || error)
        return { success: false, errors: error.response?.data || error }
      }
    },

    async forgotPassword(email: string) {
      try {
      
        this.resetLink = `/reset-password/token-${btoa(email)}`
        return { success: true, link: this.resetLink }
      } catch (error) {
        console.error('Forgot password failed:', error)
        return { success: false }
      }
    },

    async resetPassword(token: string, newPassword: string) {
      try {
        const api = useApi()
        await api.post('/reset-password/', { token, new_password: newPassword })
        return { success: true }
      } catch (error) {
        console.error('Reset password failed:', error)
        return { success: false }
      }
    },

    async swapRole(newRole: string) {
  try {
    const api = useApi()
    const response = await api.post('/swap-role/', { role: newRole })

    // Assuming backend returns updated role and maybe a new token
    const { role, token } = response.data

    // Update stor
    this.role = role
    if (token) {
      this.accessToken = token
      localStorage.setItem('accessToken', token)
    }

    // Persist to localStorage
    localStorage.setItem('role', role)

    console.log(`Role switched to: ${role}`)
    return { success: true, role }
  } catch (error) {
    console.error('Role swap failed:', error.response?.data || error)
    return { success: false, errors: error.response?.data || error }
  }
    },
  }
})

