<template>
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
                        :src="scope.row.artist.image[0]['#text']"
                        fit="fill" />
                    <span class="track-name">{{ scope.row.artist.name }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="artist.stats.listeners" label="Listeners" width="150" />
        <el-table-column prop="artist.stats.playcount" label="Playcount" width="150" />
        <el-table-column label="Tag">
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
        </el-table-column>
    </el-table>
</template>

<script setup>
import artistInfo from "@/assets/getArtistInfo.json";
const tableData = [artistInfo];
console.log(tableData);
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
