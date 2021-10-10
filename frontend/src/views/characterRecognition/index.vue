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
        action="/books/getall"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :on-success="handleSuccess"
        :before-remove="beforeRemove"
        :before-upload="action"
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
import {ref, defineComponent, reactive} from "vue"
import {envs} from '@/utils/env'
import "@/mock/mockServer"
import http from "@/utils/http2/index"

export default defineComponent({
  name: "CharacterRecognition",
  setup() {
    const refData = ref(0)
    const env = ref(envs())
    const fileList = reactive([
      {
        name: 'food.jpeg',
        url: '@/assets/food.jpeg'
      },
      {
        name: 'food2.jpeg',
        url: '@/assets/food2.jpeg'
      },
    ])
    const handleRemove = (file: any, fileList: any) => {
      console.log('handleRemove....', file, fileList)
      //console.log('Proxy.name',Proxy.name)
    }
    const handlePreview = (file: any) => {
      console.log('handlePreview....', file)
    }
    const handleSuccess = (res: any, file: any) => {
      console.log('handleSuccessres', res)
      console.log('handleSuccessfile', file)
      if (res) {
        setTimeout(() => {
          alert('上传成功')
        }, 1500);

      } else {
        alert('视频上传失败，请重新上传！');
      }
    }
    const handleExceed = (files: any, fileList: any) => {
      console.log('handleExceed....', files, fileList)

      alert(
          `The limit is 3, you selected ${
              files.length
          } files this time, add up to ${files.length + fileList.length} totally`
      )
    }
    const beforeRemove = (file: any, fileList: any) => {
      console.log('beforeRemove....', file, fileList)
      //return this.$confirm(`Cancel the transfert of ${file.name} ?`)
    }

    const action =()=>{
      http.get("http://127.0.0.1:8000/books/getall").then((res: any) => {
        console.log("==这是axios二次封装请求返回的数据==");
        console.log(res.data);
      });
    }

    // const action = () => { //正确
    //   console.log("==action()==",)
    //   http.get("/user/info").then((res: any) => {
    //     console.log("==这是axios二次封装请求返回的数据==");
    //     console.log(res.data);
    //   });
    // }

    return {
      fileList,
      env,
      handleRemove,
      handlePreview,
      handleSuccess,
      handleExceed,
      beforeRemove,
      action,
      refData
    };
  }
});
</script>
<style scoped>
</style>