<template>
    <el-aside width="15vw">
        <h1 style="margin-left: 2vw">MIR</h1>
        <el-menu
            router
            :default-active="currentPath"
            style="height: 90vh"
            :style="{ backgroundColor: $background }">
            <el-menu-item index="/home">
                <el-icon><TrophyBase /></el-icon>
                <span>Ranking</span>
            </el-menu-item>
            <el-menu-item index="/music">
                <el-icon><Headset /></el-icon>
                <span>Recommendation</span>
            </el-menu-item>
            <el-menu-item index="/data">
                <el-icon><PieChart /></el-icon>
                <span>Visualizaion</span>
            </el-menu-item>
        </el-menu>
    </el-aside>
</template>

<script setup>
import { $background } from "@/assets/theme.js";
import { useRoute, useRouter } from "vue-router";
import { ref } from "vue";
const route = useRoute();
const router = useRouter();
const currentPath = ref("");

// 在当前路径发生变化时更新 currentPath 的值
currentPath.value = route.path;
</script>

<style scoped></style>
