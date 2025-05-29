<template>
  <div class="item-manager">
    <h2>项目列表</h2>
    <form @submit.prevent="addItem" class="item-form">
      <input type="text" v-model="newItem.name" placeholder="项目名称" required />
      <input type="text" v-model="newItem.description" placeholder="项目描述" />
      <button type="submit">添加项目</button>
    </form>
    <ul class="item-list">
      <li v-for="item in items" :key="item.id" class="item-entry">
        <div>
          <strong>{{ item.name }}</strong>
          <p v-if="item.description">{{ item.description }}</p>
        </div>
        <button @click="deleteItem(item.id)" class="delete-btn">删除</button>
      </li>
    </ul>
    <p v-if="error" class="error-message">{{ error }}</p>
  </div>
</template>

<script>
import api from '../services/api';

export default {
  name: 'ItemComponent',
  data() {
    return {
      items: [],
      newItem: {
        name: '',
        description: '',
      },
      error: null,
    };
  },
  methods: {
    async fetchItems() {
      try {
        this.error = null;
        const response = await api.getItems();
        this.items = response.data;
      } catch (err) {
        console.error('Error fetching items:', err);
        this.error = '加载项目失败。后端服务是否正在运行？';
      }
    },
    async addItem() {
      try {
        this.error = null;
        if (!this.newItem.name.trim()) {
          this.error = "项目名称不能为空。";
          return;
        }
        await api.createItem(this.newItem);
        this.newItem.name = '';
        this.newItem.description = '';
        await this.fetchItems(); // 刷新列表
      } catch (err) {
        console.error('Error adding item:', err);
        this.error = '添加项目失败。';
      }
    },
    async deleteItem(id) {
      try {
        this.error = null;
        await api.deleteItem(id);
        await this.fetchItems(); // 刷新列表
      } catch (err) {
        console.error('Error deleting item:', err);
        this.error = '删除项目失败。';
      }
    },
  },
  created() {
    this.fetchItems();
  },
};
</script>

<style scoped>
.item-manager {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  border: 1px solid #eee;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.item-form {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
}
.item-form input[type="text"] {
  flex-grow: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.item-form button {
  padding: 8px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.item-form button:hover {
  background-color: #45a049;
}
.item-list {
  list-style-type: none;
  padding: 0;
}
.item-entry {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #eee;
}
.item-entry:last-child {
  border-bottom: none;
}
.item-entry strong {
  font-size: 1.1em;
}
.item-entry p {
  font-size: 0.9em;
  color: #555;
  margin: 5px 0 0 0;
}
.delete-btn {
  padding: 5px 10px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.delete-btn:hover {
  background-color: #da190b;
}
.error-message {
  color: red;
  margin-top: 10px;
}
</style>
