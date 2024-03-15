<template>
    <div class="container" v-if="showCtrl">
        <el-row>
            <el-col :span="8">
                <el-statistic :value="volume">
                    <template #title> <div class="title">Volume</div> </template>
                    <template #suffix>
                        <div style="font-size: medium">Bytes</div>
                    </template>
                </el-statistic>
            </el-col>
            <el-col :span="4">
                <el-statistic :value="tables">
                    <template #title> <div class="title">Tables</div> </template>
                </el-statistic>
            </el-col>
            <el-col :span="6">
                <el-statistic :value="sloc">
                    <template #title> <div class="title">SLOC</div> </template>
                </el-statistic>
            </el-col>
            <el-col :span="6">
                <el-statistic :value="man_hour">
                    <template #title> <div class="title">Man-hour</div> </template>
                </el-statistic>
            </el-col>
        </el-row>
        <el-button type="primary" @click="onClick" round class="clickBtn"
            >点击展示数据可视化图表</el-button
        >
    </div>

    <!-- 导航栏 -->
    <el-tabs v-else v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="Map" name="first"><WorldMap /></el-tab-pane>
        <el-tab-pane label="Gender" name="second"><StackedBarChartPolar /></el-tab-pane>
        <el-tab-pane label="Age" name="third"><RingChart /></el-tab-pane>
        <el-tab-pane label="Time" name="fourth"><BarChart /></el-tab-pane>
    </el-tabs>

    <div style="height: 60vh"></div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { useTransition } from "@vueuse/core";
import { ChatLineRound, Male } from "@element-plus/icons-vue";
import type { TabsPaneContext } from "element-plus";

import WorldMap from "@/components/graph/WorldMap.vue";
import BarChart from "@/components/graph/BarChart.vue";
import SlideSelect from "@/components/graph/SlideSelect.vue";
import StackedBarChartPolar from "@/components/graph/StackedBarChartPolar.vue";
import RingChart from "@/components/graph/RingChart.vue";
import LineChart from "@/components/graph/LineChart.vue";

// 控制界面展示
const showCtrl = ref(true); // 默认展示数据卡片
const onClick = () => {
    showCtrl.value = false;
};

// 控制数据卡片
const raw_volume = ref(0);
const raw_tables = ref(0);
const raw_sloc = ref(0);
const raw_man_hour = ref(0);

const volume = useTransition(raw_volume, {
    duration: 2600,
});
const tables = useTransition(raw_tables, {
    duration: 1500,
});
const sloc = useTransition(raw_sloc, {
    duration: 1900,
});
const man_hour = useTransition(raw_man_hour, {
    duration: 2300,
});

raw_volume.value = 9331036512;
raw_tables.value = 18;
raw_sloc.value = 2345;
raw_man_hour.value = 88888;

// 控制标签切换
const activeName = ref("first");

const handleClick = (tab: TabsPaneContext, event: Event) => {
    console.log(tab, event);
};
</script>

<style scoped>
.el-row {
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    height: 10vw;
    padding-top: 2vw;
    margin-top: 5vw;
}
.el-col {
    text-align: center;
}

.el-statistic {
    --el-statistic-content-font-size: xx-large;
}
.title {
    font-size: large;
    padding-bottom: 1vw;
}
.clickBtn {
    float: right;
    margin-right: 2vw;
    height: 3vw;
    margin-top: 2vw;
}
</style>
