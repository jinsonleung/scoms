<template>
  <h2>==上传图片(正确)==</h2>
  <div class="right">
    <el-upload
        class="upload-poster"
        action="https://jsonplaceholder.typicode.com/posts/"
        :show-file-list="false"
        :on-change="handleOnChange"
        :auto-upload="false">
      <img v-if="formMovie.posterURL" :src="formMovie.posterURL" class="avatar" alt="头像">
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>
  </div>
</template>

<script lang='ts'>
import {defineComponent, reactive} from "vue";
import {ElMessage} from "element-plus"
import http from '@/utils/http2/index'

export default defineComponent({
  name: "SecuritySetting",
  setup() {
    const formMovie = reactive({
      posterURL: ''
    })
    //文件上传之前的钩子
    const beforeUploadFile = (file: any) => {
      let FileExt = file.name.replace(/.+\./, "");
      if (["xls", "xlsx"].indexOf(FileExt.toLowerCase()) === -1) {
        ElMessage.success({
          type: "warning",
          message: "请上传后缀名为xls、xlsx的附件！"
        });
        return false;
      }
    };

    //文件超出个数时的钩子
    const exceedFile = (files: any, fileList: any) => {
      console.log("文件超出个数：", files)
      ElMessage.warning('选多了')
    };

    let uploadSuccess = (file: any) => {
      // ElMessage.success('上传成功......')
    };

    const handleOnChange = (file: any, fileList: any) => {
      let fileName = file.name;
      console.log('==file==', file)
      let regex = /(.jpg|.jpeg|.gif|.png|.bmp)$/;
      if (regex.test(fileName.toLowerCase())) {
        let img_url = URL.createObjectURL(file.raw)
        formMovie.posterURL = img_url
        console.log('==formMovie.posterURL==', formMovie.posterURL)
        // ElMessage.success('上传成功！')
        http.post('/ocr/accurateocr',{'img_url':img_url}).then((res:any)=>{
          console.log(res)
        })




      } else {
        ElMessage.error('请选择图片文件');
      }
    };
    return {
      formMovie,
      handleOnChange,
      beforeUploadFile,
      exceedFile,
      uploadSuccess
    };
  }
});
</script>
<style scoped>
</style>