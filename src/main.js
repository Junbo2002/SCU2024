// main.js
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Element Plus
import "element-plus/theme-chalk/index.css"; // 引入 ElementPlus 组件样式
// 图标和组件需要分开引入
import ElementPlus from "element-plus"; // 引入 ElementPlus 组件
import * as ElementPlusIconsVue from "@element-plus/icons-vue";

// 引入ECharts
import * as echarts from "echarts";

// 引入Vuex
import { createStore } from 'vuex';

// 创建一个新的 store 实例
const store = createStore({
  state () {
    return {
      id: 0
    }
  },
  mutations: {
    increment (state, payload) {
      state.id = payload
    }
  }
})

const app = createApp(App);

// 将 store 实例作为插件安装
app.use(store)

app.config.globalProperties.$echarts = echarts;

// 全局注册 Icon 图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component);
}

app.use(ElementPlus); // 全局挂载 ElementPlus
app.use(router).mount("#app");
