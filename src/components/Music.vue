<script setup>
import MusicCard from "@/components/MusicCard.vue";
</script>

<template>
    <h1>我是音乐推荐</h1>
    <el-carousel :interval="4000" type="card" height="40vh">
        <el-carousel-item v-for="item in 6" :key="item">
            <MusicCard />
        </el-carousel-item>
    </el-carousel>
</template>

<style scoped>
.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>
