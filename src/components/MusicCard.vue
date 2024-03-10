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
                <div class="title" style="margin-bottom: 15%">Believe</div>
                <div class="data">
                    <el-icon><Avatar /></el-icon>
                    <div>Cher</div>
                </div>
                <div class="data">
                    <el-icon><CollectionTag /></el-icon>
                    <div>pop</div>
                </div>
                <div class="data">
                    <el-icon><Headset /></el-icon>
                    <div>281445</div>
                </div>
            </div>
        </el-col>
    </el-row>
</template>

<script setup></script>

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
