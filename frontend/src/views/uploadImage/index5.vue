<template>
  <h1>==上传图片测试==</h1>
  <h7>参考：https://blog.csdn.net/qq_43964958/article/details/113665626</h7>
  <div class="container">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="商品名称">
        <el-input v-model="form.goods_title" placeholder="请输入商品名称"></el-input>
      </el-form-item>
      <el-form-item label="商品价格">
        <el-input v-model="form.goods_price" placeholder="请输入商品价格"></el-input>
      </el-form-item>
      <el-form-item label="商品分类">
        <el-input v-model="form.goods_kind" placeholder="请输入商品分类"></el-input>
      </el-form-item>
      <el-form-item label="商品图片">
        <input type="file" @change="getImageFile" id="img">
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
      goods_title: 'aa',
      goods_price: '22',
      goods_image: '',
      goods_kind: 'sdf',
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
      http.post('ocr/addNewGoods', formData).then((res: any) => {
        console.log(res);
      }).catch((err: any) => {
        console.log(err);
      })
    }

    return {

      form,
      getImageFile,
      onSubmit
    }
  }
});
</script>
<style scoped>
</style>