<template>
  <h1>==上传图片测试(测试中...)==</h1>
  <div class="container">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="商品">
        <el-input v-model="form.goods_title" placeholder="请输入名称"></el-input>
      </el-form-item>
      <el-form-item label="价格">
        <el-input v-model="form.goods_price" placeholder="请输入价格"></el-input>
      </el-form-item>
      <el-form-item label="分类">
        <el-input v-model="form.goods_kind" placeholder="请输入分类"></el-input>
      </el-form-item>
      <el-form-item label="图片">
        <el-upload
            class="upload-poster"
            action="https://jsonplaceholder.typicode.com/posts/"
            :show-file-list="false"
            :on-change="handleOnChange"
            :auto-upload="false">
          <img v-if="uploadForm.posterURL" :src="uploadForm.posterURL" class="avatar" alt="头像">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">确认添加</el-button>
        <el-button type="success">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>


<script lang='ts'>
import {defineComponent, reactive, ref} from "vue";
import {ElMessage} from "element-plus"
import http from '@/utils/http2/index'

export default defineComponent({
  name: "Index5",
  setup() {
    const formTitle = ref('编辑')
    const dialogFormVisible = ref(false)
    const form = reactive({
      goods_title: 'bb',
      goods_price: '289.0',
      goods_image: '',
      goods_kind: '电子数码',
    })

    const uploadForm = reactive({
      posterURL: ''
    })

    const getImageFile = (e: any) => {
      let file = e.target.files[0];
      form.goods_image = file;
    }
    const onSubmit = () => {
      let formData = new FormData();
      formData.append('goods_title', form.goods_title);
      formData.append('goods_price', form.goods_price);
      formData.append('goods_kind', form.goods_kind);
      formData.append('goods_image', form.goods_image);
      http.post('goods/addNewGoods', formData).then((res: any) => {
        console.log(res);
      }).catch((err: any) => {
        console.log(err);
      })
    }

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
    }
    return {
      form,
      getImageFile,
      onSubmit,
      uploadForm,
      handleOnChange
    }
  }
});
</script>
<style scoped>
</style>