<template>
    <el-aside width="200px">
        <h1 style="margin-left: 1vw">音乐推荐系统</h1>
        <el-menu router :default-active="this.$route.path" style="height: 100vh">
            <el-menu-item index="/home">
                <el-icon><Menu /></el-icon>
                <span>首页</span>
            </el-menu-item>
            <el-menu-item index="/music">
                <el-icon><Headset /></el-icon>
                <span>音乐推荐</span>
            </el-menu-item>
            <el-menu-item index="/data">
                <el-icon><Histogram /></el-icon>
                <span>数据可视化</span>
            </el-menu-item>
        </el-menu>
    </el-aside>
</template>

<script setup></script>

<style scoped></style>
