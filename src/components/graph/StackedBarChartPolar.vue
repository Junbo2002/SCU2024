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

export default {
    data() {
        return {
            stackBarChartPolar: Object,
            tableData: {},
            points: [25, 40, 55], // 初始的三个点位置
            isDragging: false,
            activePointIndex: -1,
            option: {
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
                        color: "#a4cae5",
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
            var value1 = value[0] + 1;
            var value2 = value[1] + 1;
            var value3 = value[2] + 1;
            var amount1 = 0;
            var amount2 = 0;
            var amount3 = 0;
            var amount4 = 0;
            var amount5 = 0;
            var amount6 = 0;
            var amount7 = 0;
            var amount8 = 0;
            for (let i = value3; i < 115; i++) {
                amount1 = amount1 + this.tableData.base[i];
            }
            for (let i = value2; i < value3; i++) {
                amount2 = amount2 + this.tableData.base[i];
            }
            for (let i = value1; i < value2; i++) {
                amount3 = amount3 + this.tableData.base[i];
            }
            for (let i = 0; i < value1; i++) {
                amount4 = amount4 + this.tableData.base[i];
            }
            for (let i = value3; i < 115; i++) {
                amount5 = amount5 + this.tableData.premium[i];
            }
            for (let i = value2; i < value3; i++) {
                amount6 = amount6 + this.tableData.premium[i];
            }
            for (let i = value1; i < value2; i++) {
                amount7 = amount7 + this.tableData.premium[i];
            }
            for (let i = 0; i < value1; i++) {
                amount8 = amount8 + this.tableData.premium[i];
            }
            console.log(value);
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
                console.log(this.tableData);
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
    height: 10vh;
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
