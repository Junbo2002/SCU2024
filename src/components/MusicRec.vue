<script setup>
import MusicCard from "@/components/MusicCard.vue";
import { ref, onBeforeMount, onMounted } from "vue";
import { $background, $p_carousel_item, $a_carousel_item, $base_url } from "@/assets/theme.js";
import axios from "axios";

const ids = ref([]);
const recommends = ref([]);

const carousel = ref();
const carouselId = ref();

const props = defineProps({
    userId: String,
});

// 走马灯切换
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
    axios
        .get(`${$base_url}/rec?userid=${props.userId}&count=10`)
        .then((res) => {
            ids.value = res.data.rec;
            console.log(res.data.rec);
            for (const id of ids.value) {
                axios
                    .get(
                        // `http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=b0d36553a3d96fb804b15692f31eaf63&mbid=${id}&format=json`
                        `${$base_url}/request/track/${id}`
                    )
                    // TODO
                    .then((response) => {
                        if (response.data.error === undefined) {
                            recommends.value.push(response.data.track);
                        } else {
                            console.log(response.data);
                        }
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            }
        })
        .catch((error) => {
            console.error(error);
        });

    // ids.value = [
    //     "638f3fc4-9772-4ef6-ac88-ed4645a7492c",
    //     "36c9d819-c497-4ac0-a53c-88586a450043",
    //     "0c920ec7-e71e-45c7-a682-e94ead1c8512",
    //     "f7a9accf-fac8-40d7-b84e-948d3bed32a6",
    //     "a9a88d65-dafb-48fd-893e-abd36781d0e8",
    //     "7f2f5d42-2e12-49cb-8659-4722df2eaa98",
    //     "65ce5ddf-d781-460f-a553-84a7f39ab8eb",
    //     "46a4d442-31f5-4118-8075-a869b5319b28",
    //     "0adb9188-be23-4be2-bc6a-f55ab7664019",
    //     "988329a8-42c4-40b5-9c4b-0ccc63797076",
    // ];
});

onMounted(() => {
    document.getElementById(1).style.backgroundColor = $a_carousel_item;
    for (let i = 2; i < 6; i++) {
        document.getElementById(i).style.backgroundColor = $p_carousel_item;
    }
});
</script>

<template>
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
