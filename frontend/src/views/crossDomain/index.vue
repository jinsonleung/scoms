<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 15:35:52
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 15:37:49
 * @Description:
 * @FilePath: \vue3-vite-ssis\src\views\security\SecurityAccident.vue
-->
<template>
  <div class="app-container">
      <h1>==跨域==</h1>
    <el-button type="primary" round @click="handleButtonEvent">发送POST跨域请求</el-button>

  </div>
</template>

<script lang='ts'>
import { ref, defineComponent } from "vue";
import api from '@/api'
import { ElMessage } from 'element-plus'


export default defineComponent({
  name: "SecuritySetting",
  setup() {
    const refData = ref(0);
        const handleButtonEvent = () => {
      let data = {
        'contact_person_mobile': '13500052811',
        'need_pic_code': '101'
      }
      api.shortMessages.send(data)
        .then((res:any) => {
          console.log(res)
          ElMessage.success(res.msg)
        })
        .catch(e => {
          console.log(e)
        })
    }
    return {
      refData,
    handleButtonEvent
    };
  }
});
</script>
<style scoped>
</style>