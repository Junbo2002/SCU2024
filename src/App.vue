<script setup>
import BaseMain from "@/components/layout/BaseMain.vue";
import BaseSide from "@/components/layout/BaseSide.vue";

// import { RouterLink, RouterView } from "vue-router";
</script>

<template>
    <el-container>
        <BaseSide />
        <BaseMain><RouterView /></BaseMain>
    </el-container>
</template>

<style scoped></style>
