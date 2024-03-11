<script setup>
import { onMounted, ref, watch } from "vue";

const props = defineProps({
    data: Object,
});
const loadedData = ref({
    name: "",
    mbid: "",
    duration: "",
    listeners: "",
    playcount: "",
    artist: {
        name: "",
    },
    toptags: {
        tag: [],
    },
});

onMounted(() => {
    watch(
        () => props.data, // 监听的目标数据
        (newValue) => {
            loadedData.value = newValue;
            console.log(loadedData.value);
        }
    );
});
</script>

<template>
    <el-row>
        <el-col :span="14"
            ><div class="container-l">
                <el-image
                    style="width: 90%; height: 80%"
                    src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
                    fit="fill" /></div
        ></el-col>
        <el-col :span="10">
            <div class="container-r">
                <div class="title" style="margin-bottom: 15%">{{ loadedData.name }}</div>
                <div class="data">
                    <el-icon><Avatar /></el-icon>
                    <div>{{ loadedData.artist.name }}</div>
                </div>
                <div class="data">
                    <el-icon><CollectionTag /></el-icon>
                    <div v-for="tag in loadedData.toptags.tag" :key="tag">{{ tag.name }}</div>
                </div>
                <div class="data">
                    <el-icon><Headset /></el-icon>
                    <div>{{ loadedData.playcount }}</div>
                </div>
            </div>
        </el-col>
    </el-row>
</template>

<style scoped>
.title {
    font-size: 5vh;
    font-weight: bold;
}
.container-l {
    display: flex;
    height: 40vh;
    align-items: center;
    justify-content: center;
}
.container-r {
    margin-top: 25%;
    margin-left: 5%;
}
.data {
    margin-left: 3%;
    margin-top: 2%;
    display: flex;
    align-items: center;
}
</style>
