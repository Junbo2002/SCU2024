<template>
    <el-container>
        <el-header class="custom-header">
            <div class="left-text">Hi!</div>
            <div class="right-text">{{ data }}</div>
        </el-header>
        <el-main><slot></slot></el-main>
    </el-container>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted, watch } from "vue";
import { $base_url } from "@/assets/theme.js";
import { useStore } from "vuex";

// const data = ref({ name: "" });
const data = ref();

const store = useStore()

// onMounted(() => {
//     axios
//         .get($base_url + "/request/user?uid=" + store.state.id)
//         .then((response) => {
//             console.log($base_url + "/request/user?uid=" + store.state.id)
//             console.log(response.data)
//             data.value = response.data;
//         })
//         .catch((error) => {
//             console.error(error);
//         });
// });

onMounted(() => {
    fetchData();
});

watch(() => store.state.id, () => {
    fetchData();
});

const fetchData = () => {
    axios
        .get($base_url + "/request/user?uid=" + store.state.id)
        .then((response) => {
            console.log($base_url + "/request/user?uid=" + store.state.id);
            console.log(response.data);
            data.value = response.data;
        })
        .catch((error) => {
            console.error(error);
        });
};

</script>

<style>
.custom-header {
    display: flex;
    align-items: center;
    background-image: linear-gradient(-90deg, white, #e9e9eb, #e9e9eb, #e9e9eb, white);
    gap: 10px;
}

.left-text {
    order: 1;
    p {
        font-family: "Times New Roman", Times, serif;
    }
    font-weight: bold;
    font-size: 2.5vh;
    margin-left: 65vw;
}

.right-text {
    order: 2;
    p {
        font-family: "Times New Roman", Times, serif;
    }
    font-weight: bold;
    font-size: 2.5vh;
}
</style>
