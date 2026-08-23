import axios from 'axios'

export const api = axios.create({ baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1', timeout: 8000 })
export async function getCollection(path, fallback) { try { const { data } = await api.get(path); const payload = data.results || data; return Array.isArray(payload) && payload.length === 0 ? fallback : payload } catch { return fallback } }
