// src/api/axios.js
import axios from 'axios'
const API_URL = import.meta.env.VITE_API_URL
const api = axios.create({
  baseURL: `${API_URL}/api`,
})
const auth = axios.create({
  baseURL:  `${API_URL}/api/auth`,
})
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export {api, auth}
