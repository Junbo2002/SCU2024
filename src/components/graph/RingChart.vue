<template>
    <div class="ringChart">
        <div
            ref="ringChart"
            id="ringChart1"
        ></div>
        <div
            ref="ringChart"
            id="ringChart2"
        ></div>
        <div
            ref="ringChart"
            id="ringChart3"
        ></div>
        <div
            ref="ringChart"
            id="ringChart4"
        ></div>
        <div
            ref="ringChart"
            id="ringChart5"
        ></div>
        <div
            ref="ringChart"
            id="ringChart6"
        ></div>
    </div>
  </template>
   
  <script>
  import { getCurrentInstance, onMounted } from 'vue';
   
  export default {
    setup() {
      // 通过 internalInstance.appContext.config.globalProperties 获取全局属性或方法
      let internalInstance = getCurrentInstance();
      let echarts = internalInstance.appContext.config.globalProperties.$echarts;
   
      onMounted(() => {
        // 15岁以下
        const dom1 = document.getElementById('ringChart1');
        const ringChart1 = echarts.init(dom1); // 初始化echarts实例
        const option1 = {
            title: {
                text: '15岁以下',
                textStyle: {
                    fontSize: 15,
                },
                top: '90%',
                left: 'center'
            },
            tooltip: {
                trigger: 'item'
            },
            // legend: {
            //     top: '5%',
            //     left: 'center'
            // },
            series: [
                {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '60%'],
                center: ['50%', '55%'],
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
        ringChart1.setOption(option1);

        // 15-25岁
        const dom2 = document.getElementById('ringChart2');
        const ringChart2 = echarts.init(dom2); // 初始化echarts实例
        const option2 = {
            title: {
                text: '15-25岁',
                textStyle: {
                    fontSize: 15,
                },
                top: '90%',
                left: 'center'
            },
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
                radius: ['20%', '40%'],
                center: ['50%', '55%'],
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
                    { value: 1735, name: 'Direct' },
                    // { value: 580, name: 'Email' },
                    // { value: 484, name: 'Union Ads' },
                    // { value: 300, name: 'Video Ads' }
                ]
                }
            ]
            };
        // 设置实例参数
        ringChart2.setOption(option2);

        // 25-35岁
        const dom3 = document.getElementById('ringChart3');
        const ringChart3 = echarts.init(dom3); // 初始化echarts实例
        const option3 = {
            title: {
                text: '25-35岁',
                textStyle: {
                    fontSize: 15,
                },
                top: '90%',
                left: 'center'
            },
            tooltip: {
                trigger: 'item'
            },
            // legend: {
            //     top: '5%',
            //     left: 'center'
            // },
            series: [
                {
                name: 'Access From',
                type: 'pie',
                radius: ['50%', '70%'],
                center: ['50%', '55%'],
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
                    { value: 148, name: 'Search Engine' },
                    { value: 735, name: 'Direct' },
                    // { value: 580, name: 'Email' },
                    // { value: 484, name: 'Union Ads' },
                    // { value: 300, name: 'Video Ads' }
                ]
                }
            ]
            };
        // 设置实例参数
        ringChart3.setOption(option3);

         // 35-45岁
        const dom4 = document.getElementById('ringChart4');
        const ringChart4 = echarts.init(dom4); // 初始化echarts实例
        const option4 = {
            title: {
                text: '35-45岁',
                textStyle: {
                    fontSize: 15,
                },
                top: '80%',
                left: 'center'
            },
            tooltip: {
                trigger: 'item'
            },
            // legend: {
            //     top: '5%',
            //     left: 'center'
            // },
            series: [
                {
                name: 'Access From',
                type: 'pie',
                radius: ['30%', '50%'],
                center: ['50%', '45%'],
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
                    // { value: 580, name: 'Email' },
                    // { value: 484, name: 'Union Ads' },
                    // { value: 300, name: 'Video Ads' }
                ]
                }
            ]
            };
        // 设置实例参数
        ringChart4.setOption(option4);

        // 45-55岁
        const dom5 = document.getElementById('ringChart5');
        const ringChart5 = echarts.init(dom5); // 初始化echarts实例
        const option5 = {
            title: {
                text: '45-55岁',
                textStyle: {
                    fontSize: 15,
                },
                top: '80%',
                left: 'center'
            },
            tooltip: {
                trigger: 'item'
            },
            // legend: {
            //     top: '5%',
            //     left: 'center'
            // },
            series: [
                {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '60%'],
                center: ['50%', '45%'],
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
        ringChart5.setOption(option5);

        // 55岁以上
        const dom6 = document.getElementById('ringChart6');
        const ringChart6 = echarts.init(dom6); // 初始化echarts实例
        const option6 = {
            title: {
                text: '55岁以上',
                textStyle: {
                    fontSize: 15,
                },
                top: '80%',
                left: 'center'
            },
            tooltip: {
                trigger: 'item'
            },
            // legend: {
            //     top: '5%',
            //     left: 'center'
            // },
            series: [
                {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '60%'],
                center: ['50%', '45%'],
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
        ringChart6.setOption(option6);
      });
      return {};
    }
  };
  </script>


<style>
.ringChart {
    /* background-color: pink; */
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}

#ringChart1 {
    /* background-color: blue; */
    height: 40vh;
    width: 26vw;
}

#ringChart2 {
    /* background-color: green; */
    height: 40vh;
    width: 26vw;
}

#ringChart3 {
    /* background-color: purple; */
    height: 40vh;
    width: 26vw;
}

#ringChart4 {
    /* background-color: purple; */
    height: 40vh;
    width: 26vw;
}

#ringChart5 {
    /* background-color: purple; */
    height: 40vh;
    width: 26vw;
}

#ringChart6 {
    /* background-color: purple; */
    height: 40vh;
    width: 26vw;
}
</style>
