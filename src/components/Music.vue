<script setup>
import MusicCard from "@/components/MusicCard.vue";
import { ref, onBeforeMount } from "vue";
import axios from "axios";

const ids = ref([]);
const recommends = ref([]);

onBeforeMount(() => {
    ids.value = [
        "b9b6a894-56b2-47f1-a24c-01afbad0cec6",
        "e890b57f-a9ab-4e7e-b04c-f15481078d43",
        "2b1fef5d-a774-4f57-961d-fde08e35afc1",
    ];
    for (const id of ids.value) {
        axios
            .get(
                `http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=b0d36553a3d96fb804b15692f31eaf63&mbid=${id}&format=json`
            )
            .then((response) => {
                recommends.value.push(response.data.track);
                console.log(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }
});
</script>

<template>
    <el-carousel :interval="4000" type="card" height="40vh">
        <el-carousel-item v-for="index in 3" :key="index">
            <MusicCard :data="recommends[index - 1]" />
        </el-carousel-item>
    </el-carousel>
</template>

<style scoped>
.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>
