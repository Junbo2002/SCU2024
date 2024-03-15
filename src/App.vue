<script setup>
import BaseMain from "@/components/layout/BaseMain.vue";
import BaseSide from "@/components/layout/BaseSide.vue";
import { $background } from "@/assets/theme.js";

// import { RouterLink, RouterView } from "vue-router";
</script>

<template>
    <div :style="{ backgroundColor: $background }">
        <el-container>
            <BaseSide />
            <BaseMain><RouterView /></BaseMain>
        </el-container>
    </div>
</template>

<style scoped></style>
