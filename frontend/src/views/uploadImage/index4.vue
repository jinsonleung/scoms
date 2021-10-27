<template>
  <!-- 弹框 -->
<!--  参考：https://blog.csdn.net/qq_42894622/article/details/93260525-->
  <div class="dialog">
      <el-form :model="form">
        <el-form-item label="图标" label-width="7.5rem">
          <!-- :data="upLoadData" -->
          <el-upload class="avatar-uploader"
                     action="https://jsonplaceholder.typicode.com/posts/"
                     :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
            <img v-if="form.imageUrl" :src="form.imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
        <el-form-item label="分类名" label-width="7.5rem">
          </el-form-item>
        <el-form-item label="中文" label-width="7.5rem">
          <el-input v-model="form.chinese" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="英文" label-width="7.5rem">
          <el-input v-model="form.english" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="sureFormSubmit">确 定</el-button>
      </div>
  </div>
</template>

<script lang='ts'>
import {defineComponent, reactive, ref} from "vue";
import {ElMessage} from "element-plus"
import http from '@/utils/http2/index'

export default defineComponent({
  name: "SecuritySetting",
  setup() {
    const formTitle = ref('编辑')
    const dialogFormVisible = ref(false)
    const form = reactive({
      imageUrl: '',
      english: '',
      chinese: ''
    })

    const beforeAvatarUpload = (file:any) => {
     	let api = '/ocr/accurateocr';
      let fd = new FormData();
      fd.append('file',file);//传文件
      // fd.append('srid',this.upLoadData.srid);//传其他参数
      http.post(api,fd).then((res:any)=>{
              console.log('成功');
      })
      return false//屏蔽了action的默认上传
    }
    const handleAvatarSuccess = (res:any,file:any) => {
      form.imageUrl = URL.createObjectURL(file.raw)
    }
    const sureFormSubmit = () => {
       let _this = this;
      let api = '';
      axios.post(api,{}).then((res:any)=>{console.log(res)});
    }

    return {
      formTitle,
      dialogFormVisible,
      form,
      handleAvatarSuccess,
      beforeAvatarUpload,
      sureFormSubmit
    }
  }
});
</script>
<style scoped>
</style>