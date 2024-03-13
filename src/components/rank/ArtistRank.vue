<template>
    <!-- <h1>{{ tableData }}</h1>
    <h1>{{ typeof tableData[0] }}</h1> -->
    <el-table :data="tableData" style="width: 100%; font-size: medium">
        <el-table-column width="80">
            <template #default="scope">
                <div style="display: flex; align-items: center; justify-content: center">
                    <span class="index">{{ scope.$index + 1 }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column label="Artist" width="350">
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
        <el-table-column prop="listeners" label="Listeners" width="150" />
        <el-table-column prop="playcount" label="Playcount" width="150" />
        <!-- <el-table-column label="Tag">
            <template #default="scope">
                <el-tag
                    style="margin-left: 3px; margin-bottom: 3px"
                    v-for="tag in scope.row.artist.tags.tag.slice(0, 5)"
                    :key="tag.name"
                    round
                    effect="plain">
                    {{ tag.name }}
                </el-tag>
            </template>
        </el-table-column> -->
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
