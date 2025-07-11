import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Base URL for API
const API_URL = 'http://localhost:8000/api/';

// Create axios instance
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor to add auth token to requests
api.interceptors.request.use(
  async (config) => {
    const token = await AsyncStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// API endpoints
export const authAPI = {
  login: (credentials) => api.post('users/login/', credentials),
  register: (userData) => api.post('users/register/', userData),
  logout: () => api.post('users/logout/'),
  getProfile: () => api.get('users/profile/'),
  updateProfile: (profileData) => api.put('users/profile/', profileData),
};

export const recipeAPI = {
  getRecipes: (params) => api.get('recipes/', { params }),
  getRecipe: (id) => api.get(`recipes/${id}/`),
  getCategories: () => api.get('categories/'),
  getCategory: (id) => api.get(`categories/${id}/`),
  getReviews: (recipeId) => api.get(`recipes/${recipeId}/reviews/`),
  addReview: (recipeId, reviewData) => api.post(`recipes/${recipeId}/reviews/`, reviewData),
};

export const orderAPI = {
  getCart: () => api.get('orders/cart/'),
  addToCart: (data) => api.post('orders/cart/', data),
  removeFromCart: (data) => api.delete('orders/cart/', { data }),
  checkout: (orderData) => api.post('orders/checkout/', orderData),
  getOrders: () => api.get('orders/'),
  getOrder: (id) => api.get(`orders/${id}/`),
};

export default api; 