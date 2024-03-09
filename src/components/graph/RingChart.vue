<template>
    <div
      ref="ringChart"
      id="ringChart"
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
        const dom = document.getElementById('ringChart');
        const ringChart = echarts.init(dom); // 初始化echarts实例
        const option = {
            tooltip: {
                trigger: 'item'
            },
            legend: {
                top: '5%',
                left: 'center'
            },
            series: [
                {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                    show: true,
                    fontSize: 40,
                    fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    { value: 1048, name: 'Search Engine' },
                    { value: 735, name: 'Direct' },
                    { value: 580, name: 'Email' },
                    { value: 484, name: 'Union Ads' },
                    { value: 300, name: 'Video Ads' }
                ]
                }
            ]
            };
        // 设置实例参数
        ringChart.setOption(option);
      });
      return {};
    }
  };
  </script>


<style>
/* #ringChart {
    background-color: pink;
} */
</style>
