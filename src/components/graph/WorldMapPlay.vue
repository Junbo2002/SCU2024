<template>
    <div id="container1" style="height: 76vh; width: 80vw"></div>
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

    const dom = document.getElementById("container1");

    var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
    });
    var option;

    echarts.registerMap("World", World);
    option = {
        title: {
            text: "World Music Plays",
            left: "left",
        },
        tooltip: {
            trigger: "item",
            showDelay: 0,
            transitionDuration: 0.2,
        },
        visualMap: {
            left: "right",
            top: "60%",
            min: 8.0,
            max: 12.806174828821609,
            // 浅色在上面
            inRange: {
                color: [
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
            text: ['High', 'Low'],
            // calculable: true
        },
        toolbox: {
            show: true,
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
        series: [
            {
                name: "Amount",
                type: "map",
                roam: false,
                map: "World",
                emphasis: {
                    label: {
                        show: false,
                    },
                },
            },
        ],
    };
    window.addEventListener("resize", myChart.resize);
});
</script>
