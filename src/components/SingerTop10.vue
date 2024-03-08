<template>
    <div
      ref="myChart"
      id="myChart"
      :style="{ width: '800px', height: '400px' }"
    ></div>
  </template>
   
  <script>
  import { getCurrentInstance, onMounted } from 'vue';
   
  export default {
    setup() {
      // 通过 internalInstance.appContext.config.globalProperties 获取全局属性或方法
      let internalInstance = getCurrentInstance();
      let echarts = internalInstance.appContext.config.globalProperties.$echarts;
   
      onMounted(() => {
        const dom = document.getElementById('myChart');
        const myChart = echarts.init(dom); // 初始化echarts实例
        const option = {
          xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              data: [820, 932, 901, 934, 1290, 1330, 1320],
              type: 'line',
              smooth: true
            }
          ]
        };
        // 设置实例参数
        myChart.setOption(option);
      });
      return {};
    }
  };
  </script>
