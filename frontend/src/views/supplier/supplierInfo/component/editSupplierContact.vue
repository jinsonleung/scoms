<template>
  <div class="supplier-edit-contact-container">
    <div v-dialogdrag>
      <el-dialog title="新增联系人" v-model="isShowDialog" width="800px">
        <el-form ref="ruleFormRef" :model="ruleForm" size="small" label-width="100px">
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
                <el-input v-model="ruleForm.remark" type="textarea" rows="5" placeholder="请输入备注" clearable></el-input>
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
import {reactive, toRefs, onMounted, ref} from 'vue';
import {ElMessage} from "element-plus";
import {CompanyTypes, CompanyArchitectureTypes, SupplierServiceTypes} from '/@/utils/publicOptionItems';
import {Session} from "/@/utils/storage";
import {editSupplierContact} from "/@/api/supplier";

export default {
  name: 'supplierEditContact',
  setup() {
    const ruleFormRef = ref(null);
    const state = reactive({
      isShowDialog: false,
      ruleForm: {},
    });

    // 打开弹窗
    const openDialog = (row: any) => {
      state.ruleForm = row
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

    // 提交
    const onSubmit = async () => {
      // 获取当前用户名
      state.ruleForm.update_by = Session.get('userInfo').userName;
      // console.log('==state.ruleForm==', state.ruleForm)
      editSupplierContact(state.ruleForm).then((res: any) => {
        // console.log('==res==', res)
        if (res) {
          if (ruleFormRef.value) ruleFormRef.value.resetFields();
          closeDialog();
          ElMessage.success('修改联系人成功.');
        }
      }).catch((e: any) => {
        ElMessage.warning(e);
      });
    };

    // 页面加载时
    onMounted(() => {
      // state.ruleForm.status=statusOptions[0].value;
    });
    return {
      ruleFormRef,
      CompanyTypes,
      CompanyArchitectureTypes,
      SupplierServiceTypes,
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
  margin-right: 20px;
}

.el-overlay .el-overlay-dialog .el-dialog .el-dialog__body {
  padding: 20px !important;
  margin-right: 10px;
}


</style>