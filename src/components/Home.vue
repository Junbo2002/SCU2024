<template>
    <h1>我是排行榜</h1>
    <el-menu router default-active="this.$route.path" mode="horizontal">
        <el-menu-item index="/home/trackrank">热歌榜</el-menu-item>
        <el-menu-item index="/home/playlistrank">歌单榜</el-menu-item>
        <el-menu-item index="/home/artistrank">歌手榜</el-menu-item>
        <el-sub-menu index="/home">
            <template #title>分类榜单</template>
            <el-menu-item index="2-1">类别1</el-menu-item>
            <el-menu-item index="2-2">类别2</el-menu-item>
            <el-menu-item index="2-3">类别3</el-menu-item>
        </el-sub-menu>
    </el-menu>
    <RouterView></RouterView>
</template>
