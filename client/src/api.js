import axios from 'axios'
import Cookies from 'js-cookie'

const api = axios.create({
  baseURL: '/api',
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
})

api.interceptors.request.use((config) => {
  const token = Cookies.get('csrftoken')
  if (token) {
    config.headers['X-CSRFToken'] = token
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const config = error.config
    const status = error.response?.status
    const csrfFailed =
      status === 403 &&
      !config?._csrfRetry &&
      (config?.method === 'post' || config?.method === 'put' || config?.method === 'patch' || config?.method === 'delete')

    if (csrfFailed) {
      try {
        await api.get('/profile/csrf/')
        config._csrfRetry = true
        const token = Cookies.get('csrftoken')
        if (token) {
          config.headers['X-CSRFToken'] = token
        }
        return api(config)
      } catch (e) {
        return Promise.reject(error)
      }
    }
    return Promise.reject(error)
  },
)

export default api
