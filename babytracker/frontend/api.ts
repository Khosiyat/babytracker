import axios from 'axios';

const API_BASE = 'http://localhost:8000/api'; // adjust as needed

export const fetchFoodItems = () => axios.get(`${API_BASE}/food-items/`);
export const addCustomFoodItem = (data: any) => axios.post(`${API_BASE}/food-items/`, data);
export const logFeeding = (data: any) => axios.post(`${API_BASE}/feedings/`, data);
export const getBabySummary = (babyId: number, date: string) =>
  axios.get(`${API_BASE}/baby/${babyId}/summary/?date=${date}`);
