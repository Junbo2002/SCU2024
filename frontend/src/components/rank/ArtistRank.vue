<template>
    <el-table :data="tableData" style="width: 100%; font-size: medium">
        <el-table-column width="80">
            <template #default="scope">
                <div style="display: flex; align-items: center; justify-content: center">
                    <span class="index">{{ scope.$index + 1 }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column label="Artist" width="300">
            <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image style="width: 7vw; height: 7vw" :src="scope.row.img" fit="fill" />
                    <span class="track-name">{{ scope.row.name }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="listeners" label="Listeners" width="150" />
        <el-table-column prop="playcount" label="Playcount" width="150" />
        <el-table-column label="Url">
            <template #default="scope">
                <el-link type="primary" :href="scope.row.url">{{ scope.row.url }}</el-link>
            </template>
        </el-table-column>
    </el-table>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { $base_url } from "@/assets/theme";

const tableData = ref([]);
onMounted(() => {
    axios
        .get(
            // "http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=b0d36553a3d96fb804b15692f31eaf63&format=json&limit=5"
            `${$base_url}/request/topartists?limit=10`
        )
        .then((response) => {
            tableData.value = response.data.artists.artist;
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
