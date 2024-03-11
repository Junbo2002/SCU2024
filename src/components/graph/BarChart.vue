<template>
    <div
      ref="barChart"
      class="barChart"
      id="barChart1"
      :style="{ height: '50vh'}"
    ></div>
    <!-- <div
      ref="barChart"
      class="barChart"
      id="barChart2"
      :style="{ height: '50vh'}"
    ></div> -->
  </template>
   
  <script>
  import { getCurrentInstance, onMounted } from 'vue';
   
  export default {
    setup() {
      // 通过 internalInstance.appContext.config.globalProperties 获取全局属性或方法
      let internalInstance = getCurrentInstance();
      let echarts = internalInstance.appContext.config.globalProperties.$echarts;
   
      onMounted(() => {
        const dom1 = document.getElementById('barChart1');
        const barChart1 = echarts.init(dom1); // 初始化echarts实例
        const option1 = {
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
        barChart1.setOption(option1);


        // const dom2 = document.getElementById('barChart2');
        // const barChart2 = echarts.init(dom2); // 初始化echarts实例
        // const option2 = {
        //     xAxis: {
        //         type: 'category',
        //         data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        //     },
        //     yAxis: {
        //         type: 'value'
        //     },
        //     series: [
        //         {
        //         data: [120, 200, 150, 80, 70, 110, 130],
        //         type: 'bar',
        //         itemStyle: {
        //             color: new echarts.graphic.LinearGradient(
        //                 0, 0, 0, 1, 
        //                 [
        //                 { offset: 0,   color: '#83bff6' },
        //                 { offset: 0.5, color: '#188df0' },
        //                 { offset: 1,   color: '#188df0' },
        //                 ]
        //             ),
        //         },
        //         emphasis: {
        //         itemStyle: {
        //             color: new echarts.graphic.LinearGradient(
        //             0, 0, 0, 1, 
        //             [
        //                 { offset: 0, color: '#2378f7' },
        //                 { offset: 0.7, color: '#2378f7' },
        //                 { offset: 1, color: '#83bff6' },
        //             ]),
        //         }
        //         }
        //         }
        //     ]
        // };
        // // 设置实例参数
        // barChart2.setOption(option2);
      });
      return {};
    }
  };
  </script>


<style>
/* #barChart1 {
    background-color: pink;
} */
</style>
