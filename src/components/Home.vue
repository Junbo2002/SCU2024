<template>
    <el-menu router default-active="this.$route.path" mode="horizontal">
        <el-menu-item index="/home/trackrank" style="font-size: large">Track</el-menu-item>
        <el-menu-item index="/home/playlistrank" style="font-size: large">User</el-menu-item>
        <el-menu-item index="/home/artistrank" style="font-size: large">Singer</el-menu-item>
    </el-menu>
    <RouterView></RouterView>
</template>
