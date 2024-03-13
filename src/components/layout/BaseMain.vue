<template>
    <el-container>
        <el-header class="custom-header">
            <div class="left-text">Hi!</div>
            <div class="right-text">{{ data.name }}</div>
        </el-header>
        <el-main><slot></slot></el-main>
    </el-container>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const data = ref({ name: "" });

onMounted(() => {
    axios
        .get(
            "http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=alex-devil&api_key=b0d36553a3d96fb804b15692f31eaf63&format=json"
        )
        .then((response) => {
            data.value = response.data.user;
        })
        .catch((error) => {
            console.error(error);
        });
});
</script>

<style>
.custom-header {
    display: flex;
    align-items: center;
    /* background-color: #e9e9eb; */
    background-image: linear-gradient(-90deg, white, #e9e9eb, #e9e9eb, #e9e9eb, white);
    height: 7vh;
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
