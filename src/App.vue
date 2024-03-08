<script setup>
import BaseSide from "./BaseSide.vue";

// import { RouterLink, RouterView } from "vue-router";
</script>

<template>
    <el-container class="layout-container-demo" style="height: 100vh">
        <BaseSide></BaseSide>
        <a href="http://localhost:5175/about">111</a>
        <router-link to="/">Go to Home</router-link>
        <router-link to="/about">Go to About</router-link>
        <RouterView />
    </el-container>
</template>

<style scoped></style>
