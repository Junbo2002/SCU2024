<template>
    <el-menu router default-active="this.$route.path" mode="horizontal">
        <el-menu-item index="/home/trackrank">Top Song</el-menu-item>
        <el-menu-item index="/home/playlistrank">Top User</el-menu-item>
        <el-menu-item index="/home/artistrank">Top Singer</el-menu-item>
    </el-menu>
    <RouterView></RouterView>
</template>
