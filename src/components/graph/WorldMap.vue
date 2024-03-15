<template>
    <div id="container" style="height: 100vh; width: 80vw"></div>
</template>

<script setup>
import * as echarts from "echarts";
import axios from "axios";
import { ref, onMounted } from "vue";
import { $base_url } from "@/assets/theme.js";
import World from "@/assets/world.json";

const tableData = ref();

onMounted(() => {
    axios
        .get($base_url + "/visualize/avgnationplaycount")
        .then((response) => {
            tableData.value = response.data;
        })
        .catch((error) => {
            console.error(error);
        })
        .finally(() => {
            if (option && typeof option === "object") {
                option["series"][0]["data"] = tableData.value;
                option["visualMap"]["max"] = tableData.value[0]["value"];
                option["visualMap"]["min"] = tableData.value[tableData.value.length - 1]["value"];
                myChart.setOption(option);
            }
        });

    const dom = document.getElementById("container");

    var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
    });
    var option;

    echarts.registerMap("World", World);
    option = {
        title: {
            text: "World Music Type",
            // subtext: "Data from www.census.gov",
            // sublink: "http://www.census.gov/popest/data/datasets.html",
            left: "left",
        },
        tooltip: {
            trigger: "item",
            showDelay: 0,
            transitionDuration: 0.2,
        },
        visualMap: {
            left: "right",
            min: 8.0,
            max: 12.806174828821609,
            // 浅色在上面
            inRange: {
                color: [
                    // '#ecf5ff',
                    // '#d9ecff',
                    // '#c6e2ff',
                    // '#a0cfff',
                    // '#79bbff',
                    // '#337ecc'
                    "#313695cc",
                    "#4575b4cc",
                    "#74add1cc",
                    "#abd9e9cc",
                    "#e0f3f8cc",
                    "#ffffbfcc",
                    "#fee090cc",
                    "#fdae61cc",
                    "#f46d43cc",
                    "#d73027cc",
                    "#a50026cc",
                ],
            },
        },
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: "right",
            top: "top",
            feature: {
                dataView: { show: false },
                restore: {
                    show: false,
                },
                saveAsImage: {
                    show: false,
                },
            },
        },
        legend: {
            //     data: ["China"],
            //     show: true
        },
        series: [
            {
                // name: "USA PopEstimates",
                type: "map",
                roam: false,
                map: "World",
                emphasis: {
                    label: {
                        show: true,
                    },
                },
                // data: tableData.value
                // [
                //     { name: "China", value: 1200 },
                //     { name: "Russia", value: 20 },
                //     { name: "United States", value: 250 },
                //     { name: "Japan", value: 400 },
                //     { name: "Brazil", value: 1500 },
                // ],
                // data: [
                //     {
                //         "name": "Timor-Leste",
                //         "value": 364461
                //     },
                //     {
                //         "name": "Liechtenstein",
                //         "value": 281817
                //     }
                // ]
            },
        ],
    };
    // myChart.setOption(option);

    // if (option && typeof option === "object") {
    //     myChart.setOption(option);
    // }

    window.addEventListener("resize", myChart.resize);
});
</script>
