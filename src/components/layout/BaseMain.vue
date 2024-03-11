<template>
    <el-container>
    <el-header style="text-align: center; font-size: 4vh; background-color: lightblue; height: 8vh;">
        <el-text class="mx-1" tag="b" style="align-items: center">Your ID:</el-text>
        <!-- <div class="toolbar">
          <el-dropdown>
            <el-icon style="margin-right: 8px; margin-top: 1px"
              ><setting
            /></el-icon>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item>View</el-dropdown-item>
                <el-dropdown-item>Add</el-dropdown-item>
                <el-dropdown-item>Delete</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
          <span>Tom</span>
        </div> -->
      </el-header>
    <el-main><slot></slot></el-main>
</el-container>
</template>

<script setup></script>
