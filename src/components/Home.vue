<template>
    <el-menu router default-active="this.$route.path" mode="horizontal">
        <el-menu-item index="/home/trackrank">热歌榜</el-menu-item>
        <el-menu-item index="/home/playlistrank">听歌榜</el-menu-item>
        <el-menu-item index="/home/artistrank">歌手榜</el-menu-item>
    </el-menu>
    <RouterView></RouterView>
</template>
