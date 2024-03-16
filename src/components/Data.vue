<template>
    <div class="container" v-if="showCtrl">
        <!-- 数据展示 -->
        <div class="anchor" style="margin-top: 2vw"># Our work</div>
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
                <el-statistic :value="rows">
                    <template #title> <div class="title">Rows</div> </template>
                </el-statistic>
            </el-col>
        </el-row>
        <div style="text-align: center">
            <el-button type="primary" @click="onClick" round class="clickBtn"
                >Click here to show charts</el-button
            >
        </div>
        <!-- 项目进度 -->
        <div class="anchor" style="margin-top: 6vw"># Project progress</div>
        <div class="processBox">
            <div class="timelineProcessBox">
                <el-timeline class="timeline">
                    <el-timeline-item
                        class="lineitem"
                        :class="activity.done ? 'active' : 'inactive'"
                        v-for="(activity, index) in activities"
                        :key="index"
                        :timestamp="activity.time">
                        <span style="display: flex; flex-direction: column">
                            <span style="margin: 10px 0; font-size: 16px">
                                {{ activity.content }}
                            </span>
                        </span>
                    </el-timeline-item>
                </el-timeline>
            </div>
        </div>
    </div>

    <!-- 导航栏 -->
    <!-- <WorldMap />
    <StackedBarChartPolar />
    <RingChartOne />
    <BarChart />
    <LineChart /> -->

    <el-tabs v-else v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="Listener Map" name="first"><WorldMap /></el-tab-pane>
        <el-tab-pane label="Play Map" name="second"><WorldMapPlay /></el-tab-pane>
        <el-tab-pane label="Age" name="third"><StackedBarChartPolar /></el-tab-pane>
        <el-tab-pane label="Play" name="fourth"><BarChart /></el-tab-pane>
        <el-tab-pane label="Gender" name="fifth"><RingChartOne /></el-tab-pane>
    </el-tabs>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { useTransition } from "@vueuse/core";
import { ChatLineRound, Male } from "@element-plus/icons-vue";
import type { TabsPaneContext } from "element-plus";

import WorldMap from "@/components/graph/WorldMap.vue";
import WorldMapPlay from "@/components/graph/WorldMapPlay.vue";
import BarChart from "@/components/graph/BarChart.vue";
import StackedBarChartPolar from "@/components/graph/StackedBarChartPolar.vue";
import RingChartOne from "@/components/graph/RingChartOne.vue";
import LineChart from "@/components/graph/LineChart.vue";

// 时间线

const activities = [
    {
        content: "Learning Stage",
        time: "2024-02-26",
        done: true,
    },
    {
        content: "Requirements Phase",
        done: true,
        time: "2024-04-03",
    },
    {
        content: "Design Phase",
        done: true,
        time: "2024-04-03",
    },
    {
        content: "Development Phase",
        done: true,
        time: "2024-03-17",
    },
    {
        content: "Acceptance Phase",
        done: true,
        time: "2024-03-17",
    },
];

// 控制界面展示
const showCtrl = ref(true); // 默认展示数据卡片
const onClick = () => {
    showCtrl.value = false;
};

// 控制数据卡片
const raw_volume = ref(0);
const raw_tables = ref(0);
const raw_sloc = ref(0);
const raw_rows = ref(0);

const volume = useTransition(raw_volume, {
    duration: 2600,
});
const tables = useTransition(raw_tables, {
    duration: 1500,
});
const sloc = useTransition(raw_sloc, {
    duration: 1900,
});
const rows = useTransition(raw_rows, {
    duration: 2300,
});

raw_volume.value = 9331036512;
raw_tables.value = 12;
raw_sloc.value = 2345;
raw_rows.value = 88888;

// 控制标签切换
const activeName = ref("first");

const handleClick = (tab: TabsPaneContext, event: Event) => {
    console.log(tab, event);
};
</script>

<style lang="scss" scoped>
.anchor {
    font-size: larger;
    font-weight: bold;
}

.demo-tabs {
    width: 100%;
    padding-top: 0;
}

.el-row {
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    height: 10vw;
    padding-top: 2vw;
    margin-top: 2vw;
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
    height: 3vw;
    margin-top: 3vw;
    font-size: large;
}

.processBox {
    height: 6vw;

    .title {
        font-size: 16px;
        font-weight: 600;
        padding-left: 32px;
        padding-top: 16px;
    }
    .timelineProcessBox {
        .timeline {
            display: flex;
            width: 95%;
            margin: 40px auto;
            .lineitem {
                transform: translateX(50%);
                width: 18%;
            }
        }
    }
}

:deep(.el-timeline-item__tail) {
    border-left: none;
    border-top: 2px solid #e4e7ed;
    width: 100%;
    position: absolute;
    top: 6px;
}
:deep(.el-timeline-item__wrapper) {
    padding-left: 0;
    position: absolute;
    top: 20px;
    transform: translateX(-50%);
    text-align: center;
}
:deep(.el-timeline-item__timestamp) {
    font-size: 14px;
}
.active {
    :deep(.el-timeline-item__node) {
        background-color: #409eff;
    }
    :deep(.el-timeline-item__tail) {
        border-color: #409eff;
    }
}
// 有active样式的下一个li
.active + li {
    :deep(.el-timeline-item__node) {
        background-color: #409eff;
    }
}
</style>
