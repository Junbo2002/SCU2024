<template>
    <el-table :data="tableDataNew" style="width: 100%; font-size: medium">
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
                        style="width: 8vw; height: 8vw"
                        :src="scope.row.fm_image"
                        fit="fill" />
                    <span class="track-name">{{ scope.row.fm_name }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="fm_artist" label="Artist" width="150" />
        <el-table-column
            prop="duration"
            label="Duration"
            :formatter="duration_formatter"
            width="120" />
        <el-table-column
            prop="playcount"
            label="Playcount"
            width="120"
            :formatter="number_formatter" />
        <!-- 还可以放点tag -->
        <el-table-column label="Tags">
            <template #default="scope">
                <el-tag
                    v-for="tag in scope.row.fm_tags.slice(0, 3)"
                    :key="tag"
                    type="primary"
                    round
                    >{{ tag.name }}</el-tag
                >
                <!-- <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)"
                    >Delete</el-button
                > -->
            </template>
        </el-table-column>
    </el-table>
</template>

<script setup>
import axios from "axios";
import { $base_url } from "@/assets/theme.js";
import { ref, onBeforeMount } from "vue";

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

const number_formatter = (row, col, cellValue) => {
    return new Intl.NumberFormat("en-US").format(cellValue);
};

const tableData = ref([]);
const tableDataNew = ref([]);

onBeforeMount(() => {
    axios
        .get($base_url + "/visualize/trackrank?count=20") // 获取音乐排行
        .then((response) => {
            tableData.value = response.data;
            for (let track of tableData.value) {
                axios
                    .get(
                        // `http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=b0d36553a3d96fb804b15692f31eaf63&mbid=${track.MBID}&format=json`
                        `${$base_url}/request/track/${track.MBID}` // 获取音乐信息
                    )
                    .then((res) => {
                        if (res.data.error === undefined) {
                            let tmp = track;
                            tmp.fm_image = res.data.track.album.image[2]["#text"];
                            tmp.fm_name = res.data.track.name;
                            tmp.fm_artist = res.data.track.artist.name;
                            tmp.fm_tags = res.data.track.toptags.tag;
                            tableDataNew.value.push(tmp);
                        } else {
                            console.log("歌曲不存在");
                        }
                    });
            }
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
