<!-- <template>
    <h1>我是数据可视化</h1>

    <WorldMap />
    <SlideSelect />
    <StackedBarChartPolar />
    <BarChart />
    <RingChart />
    <LineChart />
</template>

<script setup>
import WorldMap from "@/components/graph/WorldMap.vue";
import BarChart from "@/components/graph/BarChart.vue";
import SlideSelect from "@/components/graph/SlideSelect.vue";
import StackedBarChartPolar from "@/components/graph/StackedBarChartPolar.vue";
import RingChart from "@/components/graph/RingChart.vue";
import LineChart from "@/components/graph/LineChart.vue";
</script> -->
<template>
    <!-- 导航栏 -->
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="Map" name="first"><WorldMap /></el-tab-pane>
        <el-tab-pane label="Gender" name="second"><SlideSelect /></el-tab-pane>
        <el-tab-pane label="Age" name="third"><BarChart /></el-tab-pane>
        <el-tab-pane label="Time" name="fourth"><RingChart /></el-tab-pane>
    </el-tabs>

    <div style="height: 60vh"></div>

    <el-row>
        <el-col :span="6">
            <el-statistic title="数据量" :value="268500" />
        </el-col>
        <el-col :span="6">
            <el-statistic title="数据表" :value="20" />
        </el-col>
        <el-col :span="6">
            <el-statistic title="工时" :value="outputValue" />
        </el-col>
        <el-col :span="6">
            <el-statistic title="员工数" :value="4" />
        </el-col>
    </el-row>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { useTransition } from "@vueuse/core";
import { ChatLineRound, Male } from "@element-plus/icons-vue";

import WorldMap from "@/components/graph/WorldMap.vue";
import BarChart from "@/components/graph/BarChart.vue";
import SlideSelect from "@/components/graph/SlideSelect.vue";
import StackedBarChartPolar from "@/components/graph/StackedBarChartPolar.vue";
import RingChart from "@/components/graph/RingChart.vue";
import LineChart from "@/components/graph/LineChart.vue";

const source = ref(0);
const outputValue = useTransition(source, {
    duration: 1500,
});
source.value = 200;

import type { TabsPaneContext } from "element-plus";

const activeName = ref("first");

const handleClick = (tab: TabsPaneContext, event: Event) => {
    console.log(tab, event);
};
</script>

<style scoped>
.demo-tabs > .el-tabs__content {
    padding: 32px;
    color: #6b778c;
    font-size: 32px;
    font-weight: 600;
}

.el-col {
    text-align: center;
}
</style>
