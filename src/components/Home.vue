<template>
    <el-menu router default-active="this.$route.path" mode="horizontal">
        <el-menu-item index="/home/trackrank" style="font-size: medium">Track</el-menu-item>
        <el-menu-item index="/home/userrank" style="font-size: medium">User</el-menu-item>
        <el-menu-item index="/home/artistrank" style="font-size: medium">Artist</el-menu-item>
    </el-menu>
    <RouterView></RouterView>
</template>
