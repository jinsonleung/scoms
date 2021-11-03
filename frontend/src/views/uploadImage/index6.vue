<template>
  <h1>==上传图片测试(正确...,测试一个测试中....)</h1>
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
            class="upload-demo"
            action=""
            @on-change="handleOnChange"
            :on-success="handleUploadSuccess"
            :http-request="handleHttpRequest"
        >
          <el-button size="small" type="primary">添加图片</el-button>
          <template #tip>
            <div class="el-upload__tip">
              jpg/png files with a size less than 500kb
            </div>
          </template>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
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
    const form = reactive({
      goods_title: '电动牙刷',
      goods_price: '498.0',
      goods_image: '',
      goods_kind: '电子设备',
    })

    const onSubmit = () => {
      let formData = new FormData();
      formData.append('goods_title', form.goods_title);
      formData.append('goods_price', form.goods_price);
      formData.append('goods_kind', form.goods_kind);
      formData.append('goods_image', form.goods_image);
      // http.post('goods/addNewGoods', formData).then((res: any) => {
      http.post('goods/savefile', formData).then((res: any) => {
        console.log(res);
      }).catch((err: any) => {
        console.log(err);
      })
    }

    const handleHttpRequest = (item: any) => {
      console.log('==handleHttpRequest->item.file==', item.file)
      // form.goods_image = URL.createObjectURL(item.file)  //用示显示的dom
      form.goods_image = item.file  //转给后台的格式
    }
    const handleUploadSuccess = (res: any) => {
      console.log('==handleUploadSuccess->res==', res)
    }

    const handleOnChange = (file: any, fileList: any) => {
      console.log('==handleOnChange==', file)
    }

    return {
      form,
      handleHttpRequest,
      handleUploadSuccess,
      handleOnChange,
      onSubmit,
    }
  }
});
</script>
<style scoped>
</style>