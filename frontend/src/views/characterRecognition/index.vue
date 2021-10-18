<template>
  <div class="app">
    <!-- 覆盖默认的上传行为 -->
    <el-upload
      class="upload-demo"
      drag
      action=""
      :http-request="uploadFile"
      v-if="!data.url"
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    </el-upload>

    <div style="margin-top: 150px">
      <img
        :src="data.url"
        alt=""
        style="width: 500px; border: 1px dashed rgba(0, 0, 0, 0.2)"
        @click="data.url = ''"
      />
      <p>{{ data.url }}</p>
    </div>
    <div>
      <el-image
        style="width: 100px; height: 100px"
        :src="dataSet.imgUrl"
        :fit="fill"
      ></el-image>
    </div>

  </div>
</template>

<script>

// import { getUploadToken } from "@/apis/token";
import { upload } from "@/api/upload";
import {ref, defineComponent, reactive, onMounted} from "vue"
import {ElMessage} from "element-plus";

export default {
  setup() {
    const dataSet = reactive({
      imgUrl: '',
      imgCount: 0
    })
    let data = reactive({
      params: {
        token: ``,
      },
    });
    // 上传成功后操作
    let uploadSuccess = (res) => {
      data.url = `http://img.gkh0305.top/${res.key}`;
      ElMessage.success('上传成功')
    };
    // 获取上传凭证
    async function getToken() {
      let res = await getUploadToken();
      if (res) {
        data.params.token = res.data.token;
      }
    }
    // 重写上传程序
    async function uploadFile(params,imgUrl) {
      var { file } = params;
      var formData = new FormData();
      console.log('===file.name===',file)
      dataSet.imgUrl = file.name
      //formData.append("token", data.params.token);
      //formData.append("file", file);
      let res = await upload(formData);
      if (res) {
        uploadSuccess(res.data);
      }
    }
    onMounted(() => {
      //getToken();
    });
    return {
      data,
      uploadSuccess,
      uploadFile,
      dataSet,
    };
  },
};
</script>

<style lang="scss">
.app {
  height: 100vh;
  text-align: center;
  color: #5b5b5b;
  .el-upload {
    margin-top: 150px;
  }
}
</style>