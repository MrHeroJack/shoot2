import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // 如果您的后端在不同的端口上运行，请调整此处的 baseURL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  getItems() {
    return apiClient.get('/items/');
  },
  getItem(id) {
    return apiClient.get(`/items/${id}`);
  },
  createItem(item) {
    return apiClient.post('/items/', item);
  },
  updateItem(id, item) {
    return apiClient.put(`/items/${id}`, item);
  },
  deleteItem(id) {
    return apiClient.delete(`/items/${id}`);
  },
};
