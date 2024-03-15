<template>
    <div ref="StackedBarChartPolar" id="stackBarChartPolar" style="height: 70vh; width: 80vw"></div>
    <div class="slider-demo-container">
        <div class="slider-demo-block" ref="slider">
            <div class="slider-track"></div>
            <div
                class="slider-handle"
                v-for="(point, index) in points"
                :key="index"
                :style="{ left: point - 2 + '%' }"
                @mousedown="onMouseDown(index)">
                {{ Math.round(point) }}
            </div>
        </div>
    </div>
</template>

<script>
import { getCurrentInstance } from "vue";
import axios from "axios";
import { $base_url } from "@/assets/theme.js";
import { List } from "echarts";

export default {
    data() {
        return {
            stackBarChartPolar: Object,
            tableData: {},
            points: [25, 40, 55], // 初始的三个点位置
            isDragging: false,
            activePointIndex: -1,
            option: {
                title: {
                    text: "Listener vs. Age vs. Subscription Type",
                    left: "left",
                },
                angleAxis: {},
                radiusAxis: {
                    type: "category",
                    // 年龄区间
                    // data: ['Mon', 'Tue', 'Wed', 'Thu'],
                    z: 10,
                },
                polar: {},
                series: [
                    {
                        type: "bar",
                        color: "#53abd8",
                        // color: "#4a7298",
                        // data: [1, 2, 3, 4],
                        coordinateSystem: "polar",
                        name: "Base",
                        stack: "a",
                        emphasis: {
                            focus: "series",
                        },
                    },
                    {
                        type: "bar",
                        // color: "#a4cae5",
                        color: "#f3c846",
                        // data: [2, 4, 6, 8],
                        coordinateSystem: "polar",
                        name: "Premium",
                        stack: "a",
                        emphasis: {
                            focus: "series",
                        },
                    },
                ],
                legend: {
                    show: true,
                    data: ["Base", "Premium"],
                },
            },
        };
        // this.stackBarChartPolar = echarts.init(dom);
    },
    methods: {
        onMouseDown(index) {
            this.isDragging = true;
            this.activePointIndex = index;
        },
        onMouseMove(event) {
            if (!this.isDragging) return;
            const sliderRect = this.$refs.slider.getBoundingClientRect();
            const x = event.pageX - sliderRect.left;
            const percentage = (x / sliderRect.width) * 100;
            this.points[this.activePointIndex] = Math.max(0, Math.min(100, percentage));
        },
        onMouseUp() {
            this.isDragging = false;
            this.activePointIndex = -1;
            var p = [
                Math.round(this.points[0]),
                Math.round(this.points[1]),
                Math.round(this.points[2]),
            ];
            var value = p.sort((a, b) => a - b);
            // 使用前缀和算法
            var getPreSum = function(nums){
                // 从开始到第i个元素之和 
                const preSum = [];
                for(let i = 0; i < nums.length; i++){
                    if(i === 0){
                        preSum[i] = nums[i];
                    } else{
                        preSum[i] = preSum[i-1] + nums[i]
                    }
                }
                preSum[-1] = 0; 
                return preSum;
            }
            var sum1 = getPreSum(this.tableData.base);
            var sum2 = getPreSum(this.tableData.premium);

            var amount1 = sum1[114] - sum1[value[2]];
            var amount2 = sum1[value[2]] - sum1[value[1]];
            var amount3 = sum1[value[1]] - sum1[value[0]];
            var amount4 = sum1[value[0]];
            var amount5 = sum2[114] - sum2[value[2]];
            var amount6 = sum2[value[2]] - sum2[value[1]];
            var amount7 = sum2[value[1]] - sum2[value[0]];
            var amount8 = sum2[value[0]];
            this.option["radiusAxis"]["data"] = [
                value[2] + "+",
                value[1] + "-" + value[2],
                value[0] + "-" + value[1],
                value[0] + "-",
            ];
            this.option["series"][0]["data"] = [amount1, amount2, amount3, amount4];
            this.option["series"][1]["data"] = [amount5, amount6, amount7, amount8];
            this.stackBarChartPolar.setOption(this.option);
        },
    },
    mounted() {
        // 通过 internalInstance.appContext.config.globalProperties 获取全局属性或方法
        let internalInstance = getCurrentInstance();
        let echarts = internalInstance.appContext.config.globalProperties.$echarts;

        axios
            // .get($base_url + "/visualize/age?age1=" + points[0] + "&age2=" + points[1] + "&age3=" + points[2])
            .get($base_url + "/visualize/ageall")
            .then((response) => {
                this.tableData = response.data;
            })
            .catch((error) => {
                console.error(error);
            });
        const dom = document.getElementById("stackBarChartPolar");
        this.stackBarChartPolar = echarts.init(dom); // 初始化echarts实例

        // 设置实例参数
        this.stackBarChartPolar.setOption(this.option);
        // return {};
        document.addEventListener("mousemove", this.onMouseMove);
        document.addEventListener("mouseup", this.onMouseUp);
    },
    beforeUnmount() {
        document.removeEventListener("mousemove", this.onMouseMove);
        document.removeEventListener("mouseup", this.onMouseUp);
    },
};
</script>

<style scoped>
.slider-demo-container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 6vh;
    /* background-color: pink; */
}

.slider-demo-block {
    width: 40vw;
    height: 10px;
    /* background-color: #eaeaea; */
    position: relative;
    user-select: none;
    touch-action: none;
    /* margin-left: auto;
  margin-right: auto; */
}

.slider-track {
    /* width: 100%; */
    height: 100%;
    background-color: #f0f0f0;
    border-radius: 5px;
}

.slider-handle {
    position: absolute;
    top: -6px;
    width: 25px;
    height: 25px;
    background-color: #409eff;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: background-color 0.3s;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 15px;
}

.slider-handle:hover {
    background-color: #66b1ff;
}

.slider-handle:active {
    background-color: #1d6dc2;
}
</style>
