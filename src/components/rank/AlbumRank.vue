<template>
    <el-table :data="tableData" style="width: 100%; font-size: medium">
        <el-table-column width="80">
            <template #default="scope">
                <div style="display: flex; align-items: center; justify-content: center">
                    <span class="index">{{ scope.$index + 1 }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="name" label="Album" width="400">
            <template #default="scope">
                <div style="display: flex; align-items: center">
                    <el-image
                        style="width: 7vw; height: 7vw"
                        src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
                        fit="fill" />
                    <span class="track-name">{{ scope.row.name }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="listeners" label="Listeners" width="150" />
        <el-table-column prop="playcount" label="Playcount" width="150" />
        <el-table-column prop="tag" label="Tag">
            <template #default="scope">
                <el-tag round effect="plain">{{ scope.row.tag }}</el-tag>
            </template>
        </el-table-column>
    </el-table>
    <div class="flex gap-2 mt-4"></div>
</template>

<script setup>
const tableData = [
    {
        name: "Believe",
        artist: "Cher",
        listeners: "47602",
        playcount: "212991",
        tag: "pop",
    },
    {
        name: "Believe",
        artist: "Cher",
        listeners: "47602",
        playcount: "212991",
        tag: "pop",
    },
    {
        name: "Believe",
        artist: "Cher",
        listeners: "47602",
        playcount: "212991",
        tag: "pop",
    },
    {
        name: "Believe",
        artist: "Cher",
        listeners: "47602",
        playcount: "212991",
        tag: "pop",
    },
    {
        name: "Believe",
        artist: "Cher",
        listeners: "47602",
        playcount: "212991",
        tag: "pop",
    },
];
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
