import axios from 'axios';

const API_BASE = 'http://localhost:8000/api'; // Change in production

// Auto-include token if available
const token = localStorage.getItem('token');
if (token) {
  axios.defaults.headers.common['Authorization'] = `Token ${token}`;
}

// API calls
export const signup = (data: any) => axios.post(`${API_BASE}/signup/`, data);
export const login = (data: any) => axios.post(`${API_BASE}/token/`, data);

export const fetchFoodItems = () => axios.get(`${API_BASE}/food-items/`);
export const addCustomFoodItem = (data: any) => axios.post(`${API_BASE}/food-items/`, data);
export const logFeeding = (data: any) => axios.post(`${API_BASE}/feedings/`, data);
export const getBabySummary = (babyId: number, date: string) =>

  axios.get(`${API_BASE}/baby/${babyId}/summary/?date=${date}`);
