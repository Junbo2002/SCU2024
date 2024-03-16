<template>
    <el-table :data="tableData" style="width: 100%; font-size: medium">
        <!-- 索引 -->
        <el-table-column width="80">
            <template #default="scope">
                <div style="display: flex; align-items: center; justify-content: center">
                    <span class="index">{{ scope.$index + 1 }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="lastfm_username" label="Username" width="150" />
        <el-table-column prop="gender" label="Gender" :formatter="formatter" width="150" />
        <el-table-column prop="age" label="Age" :formatter="formatter" width="150" />
        <el-table-column prop="country" label="Country" :formatter="formatter" width="150" />
        <el-table-column
            prop="playcount"
            label="Playcount"
            :formatter="number_formatter"
            width="150" />
        <el-table-column prop="subscribertype" label="Subscribertype">
            <template #default="scope">
                <el-tag v-if="scope.row.subscribertype === 'base'" type="success">{{
                    scope.row.subscribertype
                }}</el-tag>
                <el-tag v-else type="warning">{{ scope.row.subscribertype }}</el-tag>
            </template>
        </el-table-column>
    </el-table>
</template>

<script setup>
import axios from "axios";
import { $base_url } from "@/assets/theme.js";
import { ref, onMounted } from "vue";

const tableData = ref([]);

const formatter = (row, column, cellValue) => {
    if (cellValue === "") {
        return "-";
    }
    return cellValue;
};

const number_formatter = (row, col, cellValue) => {
    return new Intl.NumberFormat("en-US").format(cellValue);
};

onMounted(() => {
    axios
        .get($base_url + "/visualize/userrank?count=20")
        .then((response) => {
            tableData.value = response.data;
        })
        .catch((error) => {
            console.error(error);
        });
});
</script>

<style scoped>
.track-name {
    margin-left: 2vw;
    font-size: large;
    font-weight: 800;
}
.index {
    font-size: large;
}
</style>
