<template>
    <div
      ref="StackedBarChartPolar"
      id="stackBarChartPolar"
      :style="{ height: '70vh'}"
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
        const dom = document.getElementById('stackBarChartPolar');
        const stackBarChartPolar = echarts.init(dom); // 初始化echarts实例
        const option = {
            angleAxis: {},
            radiusAxis: {
                type: 'category',
                // 年龄区间
                data: ['Mon', 'Tue', 'Wed', 'Thu'],
                z: 10
            },
            polar: {},
            series: [
                {
                type: 'bar',
                color: '#53abd8',
                data: [1, 2, 3, 4],
                coordinateSystem: 'polar',
                name: 'Base',
                stack: 'a',
                emphasis: {
                    focus: 'series'
                }
                },
                {
                type: 'bar',
                color: '#a4cae5',
                data: [2, 4, 6, 8],
                coordinateSystem: 'polar',
                name: 'Premium',
                stack: 'a',
                emphasis: {
                    focus: 'series'
                }
                },
                {
                type: 'bar',
                color: '#b7dbe3',
                data: [1, 2, 3, 4],
                coordinateSystem: 'polar',
                name: 'C',
                stack: 'a',
                emphasis: {
                    focus: 'series'
                }
                }
            ],
            legend: {
                show: true,
                data: ['Base', 'Premium', 'C']
            }
            };
        // 设置实例参数
        stackBarChartPolar.setOption(option);
      });
      return {};
    }
  };
  </script>


<style>
/* #stackBarChartPolar {
    background-color: pink;
} */
</style>