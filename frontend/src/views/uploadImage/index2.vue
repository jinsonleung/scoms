<template>
  <h2>==上传图片(测试中)==</h2>
  <div class="right">
    <el-upload
        :action="state.action"
        :file-list="modeList"
        :http-request="modeUpload"
    >
      <el-button size="small" type="primary">上传</el-button>
    </el-upload>
    <el-button @click="upload">点击上传文件</el-button>
  </div>
</template>

<script lang='ts'>
import {defineComponent, reactive, ref} from "vue";
import {ElMessage} from "element-plus"
import http from '@/utils/http2/index'
export default defineComponent({
  name: "SecuritySetting",
  setup() {
    const state = reactive({
      action: 'https://jsonplaceholder.typicode.com/posts/',
      mode: ''
    })
    const modeUpload = (item: any) => {
      console.log(item.file);
      state.mode = item.file
    }
    const upload = ()=>{
      console.log(state.mode);
      let fd = new FormData()
      fd.append('templateFile', state.mode)
      console.log('==fd==', fd)
    }
    return {
      state,
      modeUpload,
      upload
    };
  }
});
</script>
<style scoped>
</style>