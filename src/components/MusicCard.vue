<script setup>
import { onMounted, ref, watch } from "vue";
import { $base_url } from "@/assets/theme";
import axios from "axios";

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
        tag: [{ name: "" }],
    },
    image: "",
});

onMounted(() => {
    watch(
        () => props.data, // 监听的目标数据
        (newValue) => {
            loadedData.value = newValue;
            axios
                .get(
                    // `http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=b0d36553a3d96fb804b15692f31eaf63&mbid=${loadedData.value.mbid}&format=json`
                    `${$base_url}/request/track/${loadedData.value.mbid}`
                )
                .then((response) => {
                    // console.log(response.data.track.album.image[0]["#text"]);
                    loadedData.value.image = response.data.track.album.image[3]["#text"];
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    );
});
</script>

<template>
    <el-row>
        <el-col :span="14"
            ><div class="container-l">
                <el-image
                    style="width: 80%; height: 70%; border-radius: 20px"
                    :src="loadedData.image"
                    fit="fill" /></div
        ></el-col>
        <el-col :span="10">
            <div class="container-r">
                <div class="title" style="margin-bottom: 15%; max-height: 6vw">
                    {{ loadedData.name }}
                </div>
                <div class="data">
                    <el-icon><Avatar /></el-icon>
                    <div>{{ loadedData.artist.name }}</div>
                </div>
                <div class="data">
                    <el-icon><CollectionTag /></el-icon>
                    <el-tag
                        effect="plain"
                        size="small"
                        round
                        style="background-color: transparent"
                        >{{ loadedData.toptags.tag[0].name }}</el-tag
                    >
                    <!-- <div v-for="tag in loadedData.toptags.tag" :key="tag">{{ tag.name }}</div> -->
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
    font-size: 2vw;
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
    margin-left: 0;
}
.data {
    margin-left: 3%;
    margin-top: 2%;
    display: flex;
    align-items: center;
}
</style>
