<template>
    <div
      ref="barChart"
      id="barChart"
      :style="{ height: '50vh'}"
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
        const dom = document.getElementById('barChart');
        const barChart = echarts.init(dom); // 初始化echarts实例
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
                data: [120, 200, 150, 80, 70, 110, 130],
                type: 'bar',
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(
                        0, 0, 0, 1, 
                        [
                        { offset: 0,   color: '#83bff6' },
                        { offset: 0.5, color: '#188df0' },
                        { offset: 1,   color: '#188df0' },
                        ]
                    ),
                },
                emphasis: {
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(
                    0, 0, 0, 1, 
                    [
                        { offset: 0, color: '#2378f7' },
                        { offset: 0.7, color: '#2378f7' },
                        { offset: 1, color: '#83bff6' },
                    ]),
                }
                }
                }
            ]
        };
        // 设置实例参数
        barChart.setOption(option);
      });
      return {};
    }
  };
  </script>


<style>
/* #barChart {
    background-color: pink;
} */
</style>
