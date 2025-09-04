// frontend/src/api.ts
import axios from "axios";

const API_BASE = process.env.REACT_APP_API_URL || "http://localhost:8000/api";

// Create Axios instance
const api = axios.create({
  baseURL: API_BASE,
});

// Attach token automatically before each request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`; // Use Bearer for JWT
  }
  return config;
});

// ---------- Auth ----------
export const signup = (data: any) => api.post("/auth/signup/", data);
export const login = (data: any) => api.post("/auth/token/", data);

// ---------- Food Items ----------
export const fetchFoodItems = () => api.get("/food-items/");
export const addCustomFoodItem = (data: any) => api.post("/food-items/custom/", data);

// ---------- Feeding ----------
export const logFeeding = (data: any) => api.post("/feedings/", data);
export const getBabySummary = (babyId: number, date: string) =>
  api.get(`/baby/${babyId}/summary/?date=${date}`);

export default api;
