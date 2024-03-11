<template>
    <div id="container" style="height: 100vh"></div>
</template>

<script setup>
import * as echarts from "echarts";
import { onMounted } from "vue";
import World from "@/assets/world.json";

onMounted(() => {
    const dom = document.getElementById("container");

    var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
    });
    var option;

    echarts.registerMap("World", World, {
        Alaska: {
            left: -131,
            top: 25,
            width: 15,
        },
        Hawaii: {
            left: -110,
            top: 28,
            width: 5,
        },
        "Puerto Rico": {
            left: -76,
            top: 26,
            width: 2,
        },
    });
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
            orient: "horizontal",
            // left: "right",
            top: "10%",
            pieces: [
                { gt: 900, label: "rap", color: "#e0f3f8" }, // (900, Infinity]
                { gt: 310, lte: 1000, label: "blue", color: "#abd9e9" }, // (310, 1000]
                { gt: 200, lte: 300, label: "jazz", color: "#74add1" }, // (200, 300]
                { gt: 10, lte: 200, label: "pop", color: "#3189ff" }, // (10, 200]
                // {value: 123, label: '123（自定义特殊颜色）', color: "#313695"},  // [123, 123]
                // {lt: 5}                 // (-Infinity, 5)
            ],
            //             categories: ['重度污染', '中度污染', '轻度污染', '良', '优'],
            // dimension: 1,

            // splitList: [
            //     {start: 500, end:600},{start: 400, end: 500},
            //     {start: 300, end: 400},{start: 200, end: 300},
            //     {start: 100, end: 200}
            // ],

            // inRange: {

            // color: [
            //     "#313695",
            //     "#3189ff",
            //     "#74add1",
            //     "#abd9e9",
            //     "#e0f3f8",
            // ],

            // },
            // text: ["High", "Low"],
            // calculable: true,
        },
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: "right",
            top: "top",
            feature: {
                dataView: { show: false },
                restore: {
                    show: true,
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
                data: [
                    { name: "China", value: 1200 },
                    { name: "Russia", value: 20 },
                    { name: "United States", value: 250 },

                    // { name: "Alaska", value: 731449 },
                    // { name: "Arizona", value: 6553255 },
                    // { name: "Arkansas", value: 2949131 },
                    // { name: "California", value: 38041430 },
                    // { name: "Colorado", value: 5187582 },
                    // { name: "Connecticut", value: 3590347 },
                    // { name: "Delaware", value: 917092 },
                    // { name: "District of Columbia", value: 632323 },
                    // { name: "Florida", value: 19317568 },
                    // { name: "Georgia", value: 9919945 },
                    // { name: "Hawaii", value: 1392313 },
                    // { name: "Idaho", value: 1595728 },
                    // { name: "Illinois", value: 12875255 },
                    // { name: "Indiana", value: 6537334 },
                    // { name: "Iowa", value: 3074186 },
                    // { name: "Kansas", value: 2885905 },
                    // { name: "Kentucky", value: 4380415 },
                    // { name: "Louisiana", value: 4601893 },
                    // { name: "Maine", value: 1329192 },
                    // { name: "Maryland", value: 5884563 },
                    // { name: "Massachusetts", value: 6646144 },
                    // { name: "Michigan", value: 9883360 },
                    // { name: "Minnesota", value: 5379139 },
                    // { name: "Mississippi", value: 2984926 },
                    // { name: "Missouri", value: 6021988 },
                    // { name: "Montana", value: 1005141 },
                    // { name: "Nebraska", value: 1855525 },
                    // { name: "Nevada", value: 2758931 },
                    // { name: "New Hampshire", value: 1320718 },
                    // { name: "New Jersey", value: 8864590 },
                    // { name: "New Mexico", value: 2085538 },
                    // { name: "New York", value: 19570261 },
                    // { name: "North Carolina", value: 9752073 },
                    // { name: "North Dakota", value: 699628 },
                    // { name: "Ohio", value: 11544225 },
                    // { name: "Oklahoma", value: 3814820 },
                    // { name: "Oregon", value: 3899353 },
                    // { name: "Pennsylvania", value: 12763536 },
                    // { name: "Rhode Island", value: 1050292 },
                    // { name: "South Carolina", value: 4723723 },
                    // { name: "South Dakota", value: 833354 },
                    // { name: "Tennessee", value: 6456243 },
                    // { name: "Texas", value: 26059203 },
                    // { name: "Utah", value: 2855287 },
                    // { name: "Vermont", value: 626011 },
                    // { name: "Virginia", value: 8185867 },
                    // { name: "Washington", value: 6897012 },
                    // { name: "West Virginia", value: 1855413 },
                    // { name: "Wisconsin", value: 5726398 },
                    // { name: "Wyoming", value: 576412 },
                    // { name: "Puerto Rico", value: 3667084 },
                ],
            },
        ],
    };
    myChart.setOption(option);

    if (option && typeof option === "object") {
        myChart.setOption(option);
    }

    window.addEventListener("resize", myChart.resize);
});
</script>
