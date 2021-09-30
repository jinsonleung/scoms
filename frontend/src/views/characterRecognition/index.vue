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
    <h1>==文字识别==</h1>
    <el-upload
        class="upload-demo"
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :before-remove="beforeRemove"
        multiple
        :limit="3"
        :on-exceed="handleExceed"
        :file-list="fileList"
    >
      <el-button size="small" type="primary">Click to upload</el-button>
      <template #tip>
        <div class="el-upload__tip">
          jpg/png files with a size less than 500kb
        </div>
      </template>
    </el-upload>
  </div>

</template>

<script lang='ts'>
import {ref, defineComponent} from "vue";

export default defineComponent({
  name: "CharacterRecognition",
  setup() {
    const refData = ref(0);
    return {
      refData
    };
  }
});
</script>
<style scoped>
</style>