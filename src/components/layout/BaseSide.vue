<template>
    <el-aside width="16vw">
        <h1 style="margin-left: 1vw">音乐推荐系统</h1>
        <el-menu
            router
            :default-active="this.$route.path"
            style="height: 100vh"
            :style="{ backgroundColor: $background }">
            <el-menu-item index="/home">
                <el-icon><TrophyBase /></el-icon>
                <span>排行榜</span>
            </el-menu-item>
            <el-menu-item index="/music">
                <el-icon><Headset /></el-icon>
                <span>音乐推荐</span>
            </el-menu-item>
            <el-menu-item index="/data">
                <el-icon><PieChart /></el-icon>
                <span>数据可视化</span>
            </el-menu-item>
        </el-menu>
    </el-aside>
</template>

<script setup>
import { $background } from "@/assets/theme.js";
</script>

<style scoped></style>
