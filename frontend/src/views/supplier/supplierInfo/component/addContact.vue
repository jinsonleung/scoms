<template>
  <div class="supplier-add-contact-container">
    <div v-dialogdrag>
      <el-dialog title="新增联系人" v-model="isShowDialog" width="800px">
        <el-form ref="ruleFormRef" :model="ruleForm" size="small" label-width="110px">
              <el-row :gutter="10">
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="部门名称" prop="department">
                    <el-input v-model="ruleForm.department" placeholder="请输入部门名称" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="职位" prop="title">
                    <el-input v-model="ruleForm.title" placeholder="请输入职位" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="中文名" prop="chn_name">
                    <el-input v-model="ruleForm.chn_name" placeholder="请输入中文名" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="英文名" prop="eng_name">
                    <el-input v-model="ruleForm.eng_name" placeholder="请输入英文名" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="电话" prop="tel">
                    <el-input v-model="ruleForm.tel" placeholder="请输入电话" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="手机" prop="phone">
                    <el-input v-model="ruleForm.phone" placeholder="请输入手机" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="邮箱" prop="email">
                    <el-input v-model="ruleForm.email" placeholder="请输入邮箱" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="微信号" prop="wechat">
                    <el-input v-model="ruleForm.wechat" placeholder="请输入微信号" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="QQ号" prop="qq">
                    <el-input v-model="ruleForm.qq" placeholder="请输入QQ号" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="其他社交账号" prop="social_account">
                    <el-input v-model="ruleForm.social_account" placeholder="请输入其他社交账号" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="备注" prop="remark">
                    <el-input v-model="ruleForm.remark" placeholder="请输入备注" clearable></el-input>
                  </el-form-item>
                </el-col>


                  </el-row>
                </el-form>
        <template #footer>
					<span class="dialog-footer">
						<el-button @click="onCancel" size="small">取消</el-button>
						<el-button type="primary" @click="onSubmit" size="small">确定</el-button>
					</span>
        </template>

      </el-dialog>
    </div>
  </div>
</template>


<script lang="ts">
import {reactive, toRefs, onMounted, ref, getCurrentInstance} from 'vue';
import {addSupplier, updateSupplier} from "/@/api/supplier";
import {ElMessage,ElNotification} from "element-plus";
import type {TabsPaneContext } from 'element-plus';
import {CompanyTypes, Architectures, Industries} from '/@/utils/publicOptionItems';
import {objectToFormData} from '/@/utils/tsHelper'
import {Session} from "/@/utils/storage";
import {addNewEnterprise} from "/@/api/enterprise";

export default {
  name: 'supplierAddContact',
  setup() {
    const { proxy }  = getCurrentInstance() as any;
    const ruleFormRef = ref(null);
    const state = reactive({
      isShowDialog: false,
      ruleForm: {
        department: '',
        title: '',
        chn_name: '',
        eng_name: '',
        tel: '',
        phone: '',
        email: '',
        wechat: '',
        qq: '',
        social_account: '',
        remark: '',
      },
    });

    // 打开弹窗
    const openDialog = () => {
      state.isShowDialog = true;
    };
    // 关闭弹窗
    const closeDialog = () => {
      state.isShowDialog = false;
    };
    // 取消
    const onCancel = () => {
      closeDialog();
    };

    // 提交保存
    const onSubmit = async () => {
      // 文件及图片上传请求头中content-type必须是”mulpart/form-data"，服务端DRF只能接受表单格式数据
      // 创建新表单数据对象
      let formData = new FormData();
      formData = objectToFormData(state.ruleForm);
      //将上传文件放到数据对象中，保存文件名
      uploadRef.fileList.forEach((file: any) => {
        formData.append('files', file.raw);
        uploadRef.fileNames.push(file.name);
      });
      // 将上传文件名放到数据对象中
      formData.append('fileNames', uploadRef.fileNames);
      formData.set('status',0);
      // 发送axios请求
      addSupplier(formData).then((res: any) => {
        if (res) {
          console.log('==proxy.uploadRef==', proxy.uploadRef)
          // closeDialog();
          ElMessage.success('修改成功！');
        };
      });
    };

    // 页面加载时
    onMounted(() => {
      // state.ruleForm.status=statusOptions[0].value;
    });
    return {
      ruleFormRef,
      CompanyTypes,
      Architectures,
      Industries,
      openDialog,
      closeDialog,
      onCancel,
      onSubmit,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss" scoped>
:deep(.el-dialog__body) {
  height: 553px !important;
}

.statusDesc{
  margin:0;
  padding:0;
  li {
    font-size: small;
    list-style: none;
    line-height: 20px;
  }
}
</style>