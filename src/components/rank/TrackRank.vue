<template>
    <el-table :data="tableData" style="width: 100%; font-size: medium">
        <el-table-column width="80">
            <template #default="scope">
                <div style="display: flex; align-items: center; justify-content: center">
                    <span class="index">{{ scope.$index + 1 }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column label="Track" width="350">
            <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image
                        style="width: 7vw; height: 7vw"
                        :src="scope.row.image[3]['#text']"
                        fit="fill" />
                    <span class="track-name">{{ scope.row.name }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="artist.name" label="Artist" width="150" />
        <el-table-column prop="playcount" label="Playcount" width="150" />
        <el-table-column prop="duration" label="Duration" :formatter="duration_formatter" />
    </el-table>
</template>

<script setup>
const duration_formatter = (row, column, cellValue) => {
    const parsedMillisecond = parseInt(cellValue, 10);
    if (isNaN(parsedMillisecond)) {
        return "--";
    }
    const parsedSeconds = parsedMillisecond / 1000;
    const minutes = Math.floor(parsedSeconds / 60);
    const remainingSeconds = parsedSeconds % 60;
    const formattedMinutes = String(minutes).padStart(2, "0");
    const formattedSeconds = String(remainingSeconds).padStart(2, "0");
    return `${formattedMinutes}:${formattedSeconds}`;
};

import axios from "axios";
import { ref, onMounted } from "vue";

const tableData = ref([]);
onMounted(() => {
    axios
        .get(
            "http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=b0d36553a3d96fb804b15692f31eaf63&format=json&limit=5"
        )
        .then((response) => {
            tableData.value = response.data.tracks.track;
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
