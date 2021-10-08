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
import {ref, defineComponent, reactive} from "vue";

export default defineComponent({
  name: "CharacterRecognition",
  setup() {
    const refData = ref(0)
    const  fileList =reactive([
        {
          name: 'food.jpeg',
          url: '@/assets/food.jpeg'
        },
        {
          name: 'food2.jpeg',
          url: '@/assets/food2.jpeg'
        },
      ]),
    handleRemove = (file:any, fileList: any) => {
      console.log('handleRemove....', file, fileList)
      //console.log('Proxy.name',Proxy.name)
    },
    handlePreview = (file:any) => {
      console.log('handlePreview....', file)
    },
    handleExceed = (files:any, fileList: any) => {
        console.log('handleExceed....', file, fileList)

        alert(
          `The limit is 3, you selected ${
            files.length
          } files this time, add up to ${files.length + fileList.length} totally`
        )
    },
    beforeRemove = (file:any, fileList: any) => {
      console.log('beforeRemove....', file, fileList)
      //return this.$confirm(`Cancel the transfert of ${file.name} ?`)
    }

    return {
      fileList,
      handleRemove,
      handlePreview,
      handleExceed,
      beforeRemove,
      refData
    };
  }
});
</script>
<style scoped>
</style>