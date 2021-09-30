<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 15:33:15
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 16:26:19
 * @Description: 場站設置
 * @FilePath: \vue3-vite-ssis\src\views\stationSetting\StationSetting.vue
-->

<template>
  <div class="app-container">
    <h1>==場站設置==</h1>
    <el-row :gutter="20">
        <el-col :span="8"><div class="grid-content"><el-input v-model="state.num1"/></div></el-col>
        <el-col :span="8"><div class="grid-content"><el-input v-model="state.num2"/></div></el-col>
        <el-col :span="8"><div class="grid-content"><el-input v-model="state.total"/></div></el-col>
    </el-row>
    <el-row :gutter="20">
        <el-col :span="4"><div class="grid-content">{{isActives}}</div></el-col>
        <el-col :span="4"> <el-button @click="handleClick">{{state.text}}</el-button></el-col>
        <el-col :span="4"></el-col>
        <el-col :span="4"></el-col>
        <el-col :span="4"></el-col>
        <el-col :span="4"></el-col>
    </el-row>
  </div>
</template>

<script lang='ts'>
import { ref, reactive, defineComponent, computed } from "vue";
export default defineComponent({
  name: "StationSetting",
  setup() {
    const isActives = ref(false)
    const state:any = reactive({
        msg: '哈哈哈~~',
        num1: '',
        num2: '',
        total: computed(()=>{
             return parseInt(state.num1) + parseInt(state.num2)
        })
    })
    const handleClick = ()=>{
        console.log("state.msg", state.msg)
    }
    return {
      isActives,
      state,
      handleClick,
    };
  }
});
</script>
<style scoped>
</style>
