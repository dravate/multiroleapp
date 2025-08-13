import { defineNuxtRouteMiddleware, useRouter } from '#app'
import { useLoginStore } from '~/stores/login'

export default defineNuxtRouteMiddleware((to, from) => {
  const loginStore = useLoginStore()
  const router = useRouter()

  const user = loginStore.user
  const role = loginStore.role

  if (!loginStore.isAuthenticated) {
    if (to.path !== '/') {
      return navigateTo('/', { replace: true })
    } else {
      console.info('You are a GUEST user.')
    }
    return
  }

  // If authenticated, check roles
  if (role === 'client' && to.path.startsWith('/business')) {
    return navigateTo('/client', { replace: true })
  }

  if (role === 'business' && to.path.startsWith('/client')) {
    return navigateTo('/business', { replace: true })
  }
})

