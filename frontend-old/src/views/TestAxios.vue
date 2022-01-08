<!--
 * @Author: JinsonLiang
 * @Date: 2021-07-02 17:43:09
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-30 14:23:45
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\views\TestAxios.vue
-->

<template>
  <div>
    <h1>==AXIOS TEST PAGE==</h1>
    <hr />
    <button @click="getLoginMock">axios原始</button>
    <button @click="getLoginMock2">axios二次封装</button>
  </div>
</template>

  <script lang="ts">
import { ref, defineComponent, getCurrentInstance } from "vue"
import "@/mock/mockServer"
import http from "@/utils/http2/index"

export default defineComponent({
  name: "Login",
  setup() {
    const refData = ref(0);
    const { proxy }: any = getCurrentInstance();
    const getLoginMock = () => {
      proxy.$axios.get("/user/info").then((res: any) => {
        console.log("==这是原始axios请求返回的数据==");
        console.log(res.data);
      });
    };

    const getLoginMock2 = () => {
      http.get("/user/info").then((res: any) => {
        console.log("==这是axios二次封装请求返回的数据==");
        console.log(res.data);
      });
    };


    return {
      refData,
      getLoginMock,
      getLoginMock2,
    };
  },
});
</script>
  <style scoped lang='scss'>
h1 {
  color: green;
  font-size: unit($number: 12);
}
button {
  background-color: violet;
}
</style>
