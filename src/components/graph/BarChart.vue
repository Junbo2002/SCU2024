


<template>
  <div id="barChart" style="height: 70vh"></div>
</template>

<script setup>
import * as echarts from "echarts";
import axios from "axios";
import { ref, onMounted } from "vue";
import { $base_url } from "@/assets/theme.js";


const tableData = ref();
const tableDataNew1 =ref([]);
const tableDataNew2 =ref([]);

onMounted(() => {
  axios
      .get($base_url + "/visualize/playcountrange")
      .then((response) => {
          tableData.value = response.data;
          for (let key in tableData.value) {
            tableDataNew1.value.push(key);
            tableDataNew2.value.push(tableData.value[key]);
          }
          console.log(tableDataNew1.value)
          console.log(tableDataNew2.value)
      })
      .catch((error) => {
          console.error(error);
      })
      .finally(() => {
          if (option && typeof option === "object") {
              option["xAxis"]["data"] = tableDataNew1.value
              option["series"][0]["data"] = tableDataNew2.value
              barChart.setOption(option);
          }
      });

  const dom2 = document.getElementById("barChart");
  const barChart = echarts.init(dom2);

  // var myChart = echarts.init(dom, null, {
  //     renderer: "canvas",
  //     useDirtyRect: false,
  // });
  // var option;

 
  const option = {
            xAxis: {
                type: 'category',
                // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                axisLabel: {
                  rotate: 90
                },
            },
            yAxis: {
                type: 'value'
            },
            grid: {
              top:'15%',
              bottom:'25%'
            },
            series: [
                {
                // data: [120, 200, 150, 80, 70, 110, 130],
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


});
</script>

<style>
/* #barChart {
    background-color: pink;

} */
</style>