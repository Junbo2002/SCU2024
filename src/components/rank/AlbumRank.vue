<template>
    <!-- <el-table :data="tableData" style="width: 100%; font-size: medium">
        <el-table-column width="80">
            <template #default="scope">
                <div style="display: flex; align-items: center; justify-content: center">
                    <span class="index">{{ scope.$index + 1 }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column label="Album" width="350">
            <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image
                        style="width: 7vw; height: 7vw"
                        :src="scope.row.album.image[3]['#text']"
                        fit="fill" />
                    <span class="track-name">{{ scope.row.album.name }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="album.artist" label="Artist" width="150" />
        <el-table-column prop="album.playcount" label="Playcount" width="150" />
        <el-table-column label="Tag">
            <template #default="scope">
                <el-tag
                    style="margin-left: 3px; margin-bottom: 3px"
                    v-for="tag in scope.row.album.tags.tag.slice(0, 5)"
                    :key="tag.name"
                    round
                    effect="plain">
                    {{ tag.name }}
                </el-tag>
            </template>
        </el-table-column>
    </el-table> -->
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
        .get($base_url + "/visualize/userrank?count=5")
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
