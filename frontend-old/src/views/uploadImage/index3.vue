<template>
  <h2>==上传图片(测试中)==</h2>
  <el-upload
      action=""
      :show-file-list="false"
      :on-change="handleOnChange"
      :auto-upload="false">
    >
    <template #trigger>
      <el-button size="small" type="primary">select file</el-button>
    </template>
    <el-button
        style="margin-left: 10px"
        size="small"
        type="success"
        @click="submitUpload"
    >upload to server
    </el-button>
    <template #tip>
      <div class="el-upload__tip">
        jpg/png files with a size less than 500kb
      </div>
    </template>
  </el-upload>
</template>

<script lang='ts'>
import {defineComponent, reactive} from "vue";
import {ElMessage} from "element-plus"
import http from '@/utils/http2/index'

export default defineComponent({
  name: "SecuritySetting",
  setup() {
    const state = reactive({
      img_raw: {},
      img_name: ''
    })

    const handleOnChange = (file: any, fileList: any) => {
      console.log('==handleOnChange,file.raw==', file.raw)
      state.img_raw = URL.createObjectURL(file.raw)
      console.log('==handleOnChange,state.img_raw==', state.img_raw)
      // console.log('==handleOnChange==', state.img_raw)
      // state.img_name = file.raw.name
      // console.log('==handleOnChange==', state.img_name)

      // http.post('/ocr/accurateocr',{'img_raw':img_raw}).then((res:any)=>{
      //   console.log(res)
    }

    // 转换成base64方法
    const getBase64 = (file: any) => {
      return new Promise(function (resolve, reject) {
        let reader = new FileReader();
        let imgResult = "";
        reader.readAsDataURL(file);
        reader.onload = function () {
          imgResult = reader.result;
        };
        reader.onerror = function (error) {
          reject(error);
        };
        reader.onloadend = function () {
          resolve(imgResult);
        };
      });
    }

    const uploadBase = (base64: any) => {
          var that = this
          var uploadData = {
            base64Str: base64
          }
          that.$axios
              .post(host_klx + "/api/Sys/Upload", uploadData)
              .then((res) => {
                //返回数据
                console.log(res)
              })
              .catch((err) => {
                console.log(err)
              });
        }

    const submitUpload = () => {
      console.log('==submitUpload==', state.img_raw)
      http.post('/ocr/accurateocr', {'img_raw': img_raw}).then((res: any) => {
        console.log(res)
      })
    }

    return {
      state,
      handleOnChange,
      submitUpload
    }
  }
});
</script>
<style scoped>
</style>