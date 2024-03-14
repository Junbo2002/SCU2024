<script setup>
import MUsicRec from "@/components/MusicRec.vue";
import { ref, onBeforeMount, onMounted } from "vue";
import { $base_url } from "@/assets/theme.js";
import axios from "axios";

const formInline = ref({
    userId: "",
}); //

const onSubmit = () => {
    // console.log(formInline.value.userId);
    formInline.value.userId = "";
};
</script>

<template>
    <!-- 用户登录 -->
    <el-form :inline="true" :model="formInline">
        <el-form-item label="User ID">
            <el-select
                v-model="formInline.userId"
                placeholder="Select a user"
                clearable
                style="--el-select-width: 220px">
                <el-option label="10020" value="10020" />
                <el-option label="10021" value="10021" />
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">Reset</el-button>
            <!-- <el-button @click="resetForm">Reset</el-button> -->
        </el-form-item>
    </el-form>
    <h1 v-if="!formInline.userId">请选择一个用户</h1>
    <MUsicRec v-else :userId="formInline.userId" />
</template>
