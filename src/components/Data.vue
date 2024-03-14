<template>
    <h1>我是数据可视化</h1>
    <WorldMap />
    <StackedBarChartPolar />
    <BarChart />
    <RingChart />
    <LineChart />
</template>

<script setup>
import WorldMap from "@/components/graph/WorldMap.vue";
import BarChart from "@/components/graph/BarChart.vue";
import StackedBarChartPolar from "@/components/graph/StackedBarChartPolar.vue";
import RingChart from "@/components/graph/RingChart.vue";
import LineChart from "@/components/graph/LineChart.vue";

</script>
