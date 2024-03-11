<script setup>
import MusicCard from "@/components/MusicCard.vue";
import { ref, onBeforeMount, onMounted } from "vue";
import { $background, $p_carousel_item, $a_carousel_item } from "@/assets/theme.js";
import axios from "axios";

const ids = ref([]);
const recommends = ref([]);

const carousel = ref();
const carouselId = ref();

const carouselChange = (now) => {
    carouselId.value = now + 1; // 12345 => 51234
    const carousel_item = document.getElementById(carouselId.value);

    var carousel_last_item_id = carouselId.value - 1;
    if (carousel_last_item_id === 0) {
        carousel_last_item_id = 5;
    }

    const carousel_last_item = document.getElementById(carousel_last_item_id);
    const carousel_next_item = document.getElementById((carouselId.value % 5) + 1);
    carousel_last_item.style.backgroundColor = $p_carousel_item;
    carousel_next_item.style.backgroundColor = $p_carousel_item;
    carousel_item.style.backgroundColor = $a_carousel_item;
};

onBeforeMount(() => {
    ids.value = [
        "1407cad7-82bd-487b-b127-5126f174fe8b",
        "80f2a7b2-916c-4de6-a9ca-e0bb7697b923",
        "20d2bfd1-2a81-4e60-a9f3-e67bff04e0e9",
        "d0f4d334-231d-4529-811b-595390986623",
        "4fc88a59-2d09-4736-a18d-e96bde02961f",
    ];
    for (const id of ids.value) {
        axios
            .get(
                `http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=b0d36553a3d96fb804b15692f31eaf63&mbid=${id}&format=json`
            )
            .then((response) => {
                recommends.value.push(response.data.track);
            })
            .catch((error) => {
                console.error(error);
            });
    }
});

onMounted(() => {
    document.getElementById(1).style.backgroundColor = $a_carousel_item;
    for (let i = 2; i < 6; i++) {
        document.getElementById(i).style.backgroundColor = $p_carousel_item;
    }
});
</script>

<template>
    <div style="height: 20vh"></div>
    <el-carousel
        indicator-position="outside"
        :interval="400000"
        type="card"
        height="42vh"
        @change="carouselChange"
        :style="{ backgroundColor: $background }"
        ref="carousel">
        <el-carousel-item v-for="index in 5" :key="index" :id="index">
            <MusicCard :data="recommends[index - 1]" />
        </el-carousel-item>
    </el-carousel>
</template>

<style scoped>
/* .el-carousel__item h3 {
    color: red;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
    background-color: rgb(240,240,240)
} */

.el-carousel__item {
    border-radius: 10px;
    box-shadow: 5px 5px 1vh 1px rgba(0, 0, 0, 0.3);
    height: 38vh;
    flex: none;
    left: -20px;
}
</style>
