<template>
  <div class="login-body">
    <div class="login-container">
      <div class="head">
        <img class="logo" src="public/security-4.png" />
        <div class="name">
          <div class="title">安全设备管理系统</div>
          <div class="tips">场站安全设备管理系统 V1.0</div>
        </div>
      </div>
      <el-form label-position="top" :rules="rules" :model="ruleForm" ref="loginForm" class="login-form">
        <el-form-item label="账号" prop="username">
          <el-input type="text" v-model.trim="ruleForm.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model.trim="ruleForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <div style="color: #333">登录表示您已同意<a>《服务条款》</a></div>
          <el-button style="width: 100%" type="primary" @click="submitForm">立即登录</el-button>
          <el-checkbox v-model="checked" @change="!checked">下次自动登录</el-checkbox>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
//import axios from '@/utils/axios'
import http from '@/utils/http2/index'
import md5 from 'js-md5'
import '@/mock/mockServer'

import { reactive, ref, toRefs } from 'vue'
//import { localSet } from '@/utils'
export default {
  name: 'Login',
  setup() {
    const loginForm = ref(null)
    const state = reactive({
      ruleForm: {
        username: '',
        password: ''
      },
      checked: true,
      rules: {
        username: [
          { required: 'true', message: '账户不能为空', trigger: 'blur' }
        ],
        password: [
          { required: 'true', message: '密码不能为空', trigger: 'blur' }
        ]
      }
    })
    const submitForm222 = async () => {
      loginForm.value.validate((valid) => {
        console.log(valid)
        if (valid) {
          //console.log("password:", md5(state.ruleForm.password))
          axios.post('/adminUser/login', {
            userName: state.ruleForm.username || '',
            passwordMd5: md5(state.ruleForm.password)
          }).then(res => {
            console.log(res.data)
            //localSet('token', res)
            //window.location.href = '/'
          })
        } else {
          console.log('error submit!!')
          return false;
        }
      })
    }

    const submitForm = async () => {
      loginForm.value.validate((valid) => {
        //console.log(valid)
        if (valid) {
          // console.log("password:", md5(state.ruleForm.password))
          http.post('/adminUser/checkLogin', {
            userName: state.ruleForm.username || '',
            passwordMd5: md5(state.ruleForm.password)
          }).then(res => {
            console.log(res.data)
            if (res.data.success) {
              alert("用户及密码正确，欢迎您！")
              //localSet('token', res)
              window.location.href = '/'
            }else{
              alert("用户及密码错误！")
            }

          })
        } else {
          console.log('error submit!!')
          return false;
        }
      })
    }

    const resetForm = () => {
      loginForm.value.resetFields();
    }
    return {
      ...toRefs(state),
      loginForm,
      submitForm,
      resetForm
    }
  }
}
</script>

<style scoped>
  .login-body {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    background-color: #fff;
    /* background-image: linear-gradient(25deg, #077f7c, #3aa693, #5ecfaa, #7ffac2); */
  }
  .login-container {
    width: 420px;
    height: 500px;
    background-color: #fff;
    border-radius: 4px;
    box-shadow: 0px 21px 41px 0px rgba(0, 0, 0, 0.2);
  }
  .head {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px 0 20px 0;
  }
  .head img {
    width: 50px;
    height: 50px;
    margin-right: 20px;
  }
  .head .title {
    font-size: 20px;
    color: #1BAEAE;
    font-weight: bold;
  }
  .head .tips {
    font-size: 12px;
    color: #999;
  }
  .login-form {
    width: 70%;
    margin: 0 auto;
  }
</style>
<style>
  .el-form--label-top .el-form-item__label {
    padding: 0;
  }
  .login-form .el-form-item {
    margin-bottom: 12px;
  }
</style>