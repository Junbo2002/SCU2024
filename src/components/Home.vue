<template>
    <h1>我是排行榜</h1>
    <el-table :data="tableData" style="width: 100%; font-size: medium">
        <el-table-column width="80">
            <template #default="scope">
                <div style="display: flex; align-items: center; justify-content: center">
                    <span class="index">{{ scope.$index + 1 }}</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column prop="name" label="歌曲" width="500">
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
        <el-table-column prop="artist" label="歌手" width="180" />
        <el-table-column prop="duration" label="时长" :formatter="duration_formatter" />
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

const tableData = [
    {
        name: "Believe",
        artist: "Cher",
        duration: "240000",
    },
    {
        name: "Believe",
        artist: "Cher",
        duration: "240000",
    },
    {
        name: "Believe",
        artist: "Cher",
        duration: "",
    },
    {
        name: "Believe",
        artist: "Cher",
        duration: "240000",
    },
    {
        name: "Believe",
        artist: "Cher",
        duration: "240000",
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
