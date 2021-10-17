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
    <h1>==跨域请求==</h1>
    <el-button type="primary" round @click="handleButtonEvent">发送POST跨域请求</el-button>
    <el-button type="primary" round @click="handleButtonEvent2">发送POST跨域请求2</el-button>
    <el-button type="primary" round @click="handleButtonEvent3">发送POST跨域请求3</el-button>
    <el-button type="primary" round @click="handleButtonEvent4">发送GET跨域请求4</el-button>
    <el-button type="primary" round @click="handleButtonEvent5">发送GET跨域请求5</el-button>
    <el-button type="primary" round @click="handleButtonEvent6">发送POST跨域请求6</el-button>

  </div>
</template>

<script lang='ts'>
import {ref, defineComponent} from "vue";
import api from '@/api'
import {ElMessage} from 'element-plus'
import http from '@/utils/http2'

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
          .then((res: any) => { //正确
            console.log('==res.data1==', res)
            ElMessage.success(res.msg)
          })
          .catch(e => {
            console.log(e)
          })
    }

    const handleButtonEvent2 = () => {  //正确
      http.post('ec/api.php?mod=leads&act=getvalidatecode', {'aaa': '113234234', 'bb': '2893'}).then((res: any) => {
        console.log('===res.data2===', res.data)
        ElMessage.success(res.data.msg)
      }).catch((e: any) => {
        console.log(e)
      })
    }

    const handleButtonEvent3 = () => {  //请求正确，但没有返回数据，必须有就一个前缀'abc/'，可修改成任何前缀
      http.post('abc/sug', {'code': 'utf-8', 'q': '皮鞋', 'callback': 'data'}).then((res: any) => {
        console.log('===res.data3===', res.data)  //空
        console.log('===res.status===', res.status) //200
        ElMessage.success(res.data.msg)
      }).catch((e: any) => {
        console.log(e)
      })
    }

    const handleButtonEvent4 = () => {  //请求错误
      http.get('cc/json/mobile_tel_segment.htm?tel=13500052811').then((res: any) => {
        console.log('===res.data34==', res.data)  //空
        console.log('===res.status===', res.status) //200
        ElMessage.success(res.data.msg)
      }).catch((e: any) => {
        console.log(e)
      })
    }

    const handleButtonEvent5 = () => {  // 正确
      http.get('books/getall').then((res: any) => {
        console.log('===res.data5==', res.data)  //空
        console.log('===res.status===', res.status) //200
        ElMessage.success(res.data.msg)
      }).catch((e: any) => {
        console.log(e)
      })
    }

    const handleButtonEvent6 = () => {  // 正确
      // http://localhost:3000/api/v1/auth/register
      // 请求地址：https://imissu.herokuapp.com/api/v1/auth/register?name=aa223&email=19839283@qq.com&password=222333&password2=222333&role=user
      let params = {"name":"aaa","email":"afad232fa2@qq.com","password":"232323","password2":"232323","role":"user"}
      http.post('api/v1/auth/register', params).then((res: any) => {
        console.log('===res.data6==', res.data)  //空
        console.log('===res.status===', res.status) //200
        ElMessage.success(res.data.msg)
      }).catch((e: any) => {
        console.log(e)
      })
    }


    return {
      refData,
      handleButtonEvent,
      handleButtonEvent2,
      handleButtonEvent3,
      handleButtonEvent4,
      handleButtonEvent5,
      handleButtonEvent6
    };
  }
});
</script>
<style scoped>
</style>