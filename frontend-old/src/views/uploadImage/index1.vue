<template>
  <h2>==上传图片(测试中)==</h2>
  <div class="right">
    <el-upload
        action=""
        :file-list="fileList"
        @on-change="handleChange"
        :on-success="uploadSuccess"
        :http-request="getFile"
    >
      <el-button size="small" type="primary">上传</el-button>
    </el-upload>
    <img v-if="img_url" :src="img_url" class="avatar" alt="头像"><br>
    <el-button size="small" type="success" @click="upload">确认上传</el-button>
  </div>
</template>

<script lang='ts'>
import {defineComponent, reactive, ref} from "vue";
import {ElMessage} from "element-plus"
import http from '@/utils/http2/index'

export default defineComponent({
  name: "SecuritySetting",
  setup() {
    const files = ref('')
    const fileList = reactive([]) //响应区数组
    const img_url = ref('')
    const handleChange = (file: any, fileList: any) => {
      console.log('==handleChange==',file)
    }
    const upload = () => {
      // console.log('===upload==')
      // const fd = new FormData()
      // fd.append('filename', files.value)
      // console.log('==fd in upload==',fd)

      const config = {headers: {'Content-Type': 'multipart/form-data'}}
      // this.$request.post('/uploading', fd, config
      // ).then(response => {
      //   this.$message.success(response.retCode)
      // })

      const params = {'img_url': img_url.value}
      http.post('/ocr/accurateocr',params).then((res:any)=>{
          console.log(res)
        })
    }

    const getFile = (item: any) => {
      console.log('==getFile1,item==',item )
      img_url.value = URL.createObjectURL(item.file)
      // files.value = img_url
      // console.log('==getFile2==',files.value )
    }

    const uploadSuccess = (res: any) => {
      console.log('==uploadSuccess,res==',res )
      // let img_url = URL.createObjectURL(item)
      // files.value = img_url
      // console.log('==getFile2==',files.value )
    }

    return {
      files,
      fileList,
      img_url,
      handleChange,
      uploadSuccess,
      getFile,
      upload,
    };
  }
});
</script>
<style scoped>
</style>