<template>
  <div id="app">
    <img alt="Vue 标志" src="./assets/logo.png" style="width: 100px; height: auto;">
    <h1>我的全栈应用</h1>
    <ItemComponent />
  </div>
</template>

<script>
import ItemComponent from './components/ItemComponent.vue';

export default {
  name: 'App',
  components: {
    ItemComponent,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
