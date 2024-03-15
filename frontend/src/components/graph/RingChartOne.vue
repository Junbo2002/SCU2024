<template>
    <div id="myRingChart" style="height: 70vh; width: 80vw"></div>
</template>

<script setup>
import * as echarts from "echarts";
import axios from "axios";
import { ref, onMounted } from "vue";
import { $base_url } from "@/assets/theme.js";

const tableData = ref();
const tableDataNew = ref([]);

onMounted(() => {
    axios
        .get($base_url + "/visualize/gender")
        .then((response) => {
            tableData.value = response.data;
            let obj1 = {
                name: "Male",
                value: tableData.value.m,
            };
            let obj2 = {
                name: "Female",
                value: tableData.value.f,
            };
            let obj3 = {
                name: "Unknown",
                value: tableData.value.unknown + tableData.value.n,
            };
            tableDataNew.value.push(obj1);
            tableDataNew.value.push(obj2);
            tableDataNew.value.push(obj3);
        })
        .catch((error) => {
            console.error(error);
        })
        .finally(() => {
            if (option && typeof option === "object") {
                option["series"][0]["data"] = tableDataNew.value;
                myRingChart.setOption(option);
            }
        });

    const dom1 = document.getElementById("myRingChart");
    const myRingChart = echarts.init(dom1);

    const option = {
        tooltip: {
            trigger: "item",
        },
        legend: {
            top: "5%",
            left: "center",
        },
        series: [
            {
                name: "Amount",
                type: "pie",
                center: ["50%", "56%"],
                radius: ["45%", "70%"],
                avoidLabelOverlap: false,
                padAngle: 5,
                itemStyle: {
                    borderRadius: 10,
                },
                color: ["#73b0ff", "#ea7c77", "#fac858"],
                label: {
                    show: false,
                    position: "center",
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: 40,
                        fontWeight: "bold",
                    },
                },
                labelLine: {
                    show: false,
                },
            },
        ],
    };
});
</script>
