<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 15:35:52
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 15:37:49
 * @Description:
 * @FilePath: \vue3-vite-ssis\src\views\security\SecurityAccident.vue
-->
<template>
    <div class="app-container">
      <h1>==图片上传==</h1>
  </div>
  <el-upload action="#" list-type="picture-card" :auto-upload="false">
    <template #default>
      <i class="el-icon-plus"></i>
    </template>
    <template #file="{ file }">
      <div>
        <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
        <span class="el-upload-list__item-actions">
          <span
            class="el-upload-list__item-preview"
            @click="handlePictureCardPreview(file)"
          >
            <i class="el-icon-zoom-in"></i>
          </span>
          <span
            v-if="!disabled"
            class="el-upload-list__item-delete"
            @click="handleDownload(file)"
          >
            <i class="el-icon-download"></i>
          </span>
          <span
            v-if="!disabled"
            class="el-upload-list__item-delete"
            @click="handleRemove(file)"
          >
            <i class="el-icon-delete"></i>
          </span>
        </span>
      </div>
    </template>
  </el-upload>
  <el-dialog v-model="dialogVisible">
    <img width="100%" :src="dialogImageUrl" alt="" />
  </el-dialog>
</template>

<script lang='ts'>
import {ref, defineComponent, reactive} from "vue";
export default defineComponent({
  name: "SecuritySetting",
  setup() {
    const refData = ref(0);
    const state = reactive({
      dialogImageUrl:'',
      dialogVisible: false,
      disabled: false,
    })

    const handleRemove =(file:any) => {
      console.log(file)
    };
    const handlePictureCardPreview = (file:any)=> {
      state.dialogImageUrl = file.url
      state.dialogVisible = true
    };
    const handleDownload = (file:any) => {
      console.log(file)
    };

    return {
      refData,
      handleRemove,
      handlePictureCardPreview,
      handleDownload
    };
  }
});
</script>
<style scoped>
</style>