<script setup>
import MUsicRec from "@/components/recommend/MusicRec.vue";
import { useId } from "element-plus";
import { ref } from "vue";
import { useStore } from "vuex";

const formInline = ref({
    userId: "",
}); //

const onReset = () => {
    formInline.value.userId = "";
};

const store = useStore()
const handleChange = () => {
    store.commit('increment', formInline.value.userId)
    console.log(formInline.value.userId)
    console.log(store.state.id)
}

</script>

<template>
    <!-- 用户登录 -->
    <el-form :inline="true" :model="formInline">
        <el-form-item label="User ID">
            <el-select
                @change="handleChange"
                v-model="formInline.userId"
                placeholder="Select a user"
                clearable
                style="--el-select-width: 220px">
                <el-option label="10010" value="10010" />
                <el-option label="10032" value="10032" />
                <el-option label="11097" value="11097" />
                <el-option label="11140" value="11140" />
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onReset" round>Reset</el-button>
        </el-form-item>
    </el-form>
    <h1 v-if="!formInline.userId">请选择一个用户</h1>
    <MUsicRec v-else :userId="formInline.userId" />
</template>
