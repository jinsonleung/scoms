<template>
  <h1>==上传图片==</h1>
  <div id="app">
    <el-upload
        action="#"
        list-type="picture-card"
        :auto-upload="false"
        :on-change="handleChange"
        :file-list="fileList"
    >
      <template #default>
        <i class="el-icon-plus"></i>
      </template>
      <template #file="{ file }">
        <div>
          <img
              class="el-upload-list__item-thumbnail"
              :src="file.url"
              alt=""
          />
          <span class="el-upload-list__item-actions">
                <span
                    class="el-upload-list__item-delete"
                    @click="handleRemove(file)"
                >
                  <i class="el-icon-delete"></i>
                </span>
              </span>
        </div>
      </template>
    </el-upload>
  </div>
</template>
<script>

import {reactive} from "vue";

export default {
  setup() {
    const dataSet = reactive({
      imgUrl: '',
      imgCount: 0
    });
    const handleRemove = (file) => {
      this.fileList = this.fileList.filter((el) => {
        return el.fileId != file.fileId;
      });
      console.log(this.fileList)
      this.$forceUpdate();
    };
    const handleChange = (file, fileList) => {
      var fileType = file.name.substring(file.name.lastIndexOf(".") + 1);
      if (fileType.indexOf("png") == -1 && fileType.indexOf("jpg") == -1 && fileType.indexOf("jpeg") == -1) {
        console.log("只能上传图片")
        var arrList = fileList;
        this.fileList = arrList.filter((el) => {
          return el.name != file.name;
        });
        // this.$forceUpdate();
        // console.log(this.fileList)
        //输入fileList数据正确 但是还是渲染了 同一个不是图片的文件上传两次或者更多 但是第一次有时候是可以刷新页面的 后面再上次就不会刷新页面
      }
    };
    return {
      handleRemove,
      handleChange,
      dataSet,
    };

  }
}
</script>
