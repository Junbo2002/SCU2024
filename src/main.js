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
<<<<<<< HEAD
import * as echarts from "echarts";
=======
// import * as echarts from '/node_modules/.vite/deps/echarts.js?v=a78e7802';
import * as echarts from 'echarts'
// Vue.prototype.$echarts = echarts

>>>>>>> 9e4d4cc99b37059abdca811c53c100128a4caf4d

const app = createApp(App);

app.config.globalProperties.$echarts = echarts;

// 全局注册 Icon 图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component);
}

app.use(ElementPlus); // 全局挂载 ElementPlus
app.use(router).mount("#app");
