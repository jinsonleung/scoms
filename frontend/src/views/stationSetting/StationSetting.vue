<template>
<div class="box">
  <el-form :model="ruleForm" :rules="rules" ref="ruleFormRef" label-width="100px">
    <el-form-item label="场站代码" prop="station_code">
      <el-input v-model="ruleForm.station_code"></el-input>
    </el-form-item>
    <el-form-item label="场站名称" prop="station_name">
      <el-input v-model="ruleForm.station_name"></el-input>
    </el-form-item>
    <el-form-item label="场站地址" prop="station_address">
      <el-input v-model="ruleForm.station_address"></el-input>
    </el-form-item>
    <el-form-item label="设备代码" prop="facility_code">
      <el-input v-model="ruleForm.facility_code"></el-input>
    </el-form-item>
    <el-form-item label="场站人数" prop="employees">
      <el-input v-model="ruleForm.employees"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" size="medium" @click="submitForm">添加</el-button>
    </el-form-item>
  </el-form>
</div>
</template>

<script>
import {reactive,ref,unref } from 'vue'
export default {
  setup(props) {
    const ruleFormRef = ref(null);
    // 定义变量
    const ruleForm = reactive({
      station_code: '',
      station_name: '',
      station_address: '',
      facility_code: '',
      employees: '',
    })

    const rules = {
      station_code: [
        { required: true, message: '请输入站场代码', trigger: 'blur' },
      ],
      station_name: [
        { required: true, message: '请输入站场名称', trigger: 'blur' },
      ],
      facility_code: [
        { required: true, message: '请输入设备代码', trigger: 'blur' }
      ]
    }

    const submitForm = async () => {
      const form = unref(ruleFormRef);
      if (!form) return
      try {
        await form.validate()
        const { station_code, station_name, facility_code } = ruleForm
        console.log(station_code, station_name, facility_code)
      } catch (error) {
      }
    }
    return {
      ruleForm,
      rules,
      submitForm,
      ruleFormRef
    }
  }
}
</script>

<style lang="less">
</style>