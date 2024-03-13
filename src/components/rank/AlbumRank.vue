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
        <!-- 用户名 -->
        <!-- <el-table-column label="username" width="350">
            <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image
                        style="width: 7vw; height: 7vw"
                        :src="scope.row.album.image[3]['#text']"
                        fit="fill" />
                    <span class="track-name">{{ scope.row.last_username }}</span>
                </div>
            </template>
        </el-table-column> -->
        <el-table-column prop="lastfm_username" label="Username" width="150" />
        <el-table-column prop="gender" label="Gender" width="150" />
        <el-table-column prop="age" label="Age" width="150" />
        <el-table-column prop="country" label="Country" width="150" />
        <el-table-column prop="playcount" label="Playcount" width="150" />
        <el-table-column prop="subscribertype" label="Subscribertype" width="150" />
    </el-table>
</template>

<script setup>
// import albemInfo from "@/assets/getAlbumInfo.json";
// const tableData = [albemInfo];

import axios from "axios";
import { $base_url } from "@/assets/theme.js";
import { ref, onMounted } from "vue";

const tableData = ref([]);

console.log($base_url + "/visualize/userrank?count=5");
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
