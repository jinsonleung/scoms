<template>
  <div class="system-edit-dept-container">
    <div v-dialogdrag>
      <el-dialog title="修改供应商信息" v-model="isShowDialog" width="800px">
        <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
          <el-tab-pane label="基本信息" name="baseInfoTab">
            <el-form ref="ruleFormRef" :model="ruleForm" size="small" label-width="110px">
              <el-row :gutter="10">
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="账号" prop="account">
                    <el-input v-model="ruleForm.account" placeholder="请输入供应商账号" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="供应商简称" prop="abbreviation_name">
                    <el-input v-model="ruleForm.abbreviation_name" placeholder="请输入供应商简称" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="供应商全称" prop="full_name">
                    <el-input v-model="ruleForm.full_name" placeholder="请输入供应商名全称" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="体系结构" prop="architecture">
                    <el-select v-model="ruleForm.architecture" placeholder="请选择体系结构" clearable class="w100">
                      <el-option
                          v-for="item in enterpriseArchitectureOptions"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value"
                      ></el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="社会信用代码" prop="unified_social_credit_code">
                    <el-input v-model="ruleForm.unified_social_credit_code" placeholder="请输入统一社会信用代码"
                              onkeyup="this.value=this.value.toUpperCase()" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="注册资本" prop="registered_capital">
                    <el-input v-model="ruleForm.registered_capital" placeholder="请输入注册资本" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="注册地址" prop="registered_address">
                    <el-input v-model="ruleForm.registered_address" placeholder="请输入注册地址" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="成立日期" prop="established_date">
                    <el-date-picker v-model="ruleForm.established_date" type="date" placeholder="请选择成立日期"
                                    value-format="YYYY-MM-DD" class="w100"></el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="营业期限(起)" prop="effective_start_date">
                    <el-date-picker v-model="ruleForm.effective_start_date" type="date" placeholder="请选择营业期限(起)"
                                    value-format="YYYY-MM-DD" class="w100"></el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="营业期限(止)" prop="effective_end_date">
                    <el-date-picker v-model="ruleForm.effective_end_date" type="date" placeholder="请选择营业期限(止)"
                                    value-format="YYYY-MM-DD" class="w100"></el-date-picker>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="供应商地址" prop="office_address">
                    <el-input v-model="ruleForm.office_address" placeholder="办公地址" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="经营范围" prop="business_scope">
                    <el-input v-model="ruleForm.business_scope" placeholder="请输入经营范围" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在城市" prop="city">
                    <el-input v-model="ruleForm.city" placeholder="请选择所在城市" clearable></el-input>

                    <!--                <el-cascader-->
                    <!--                    v-model="ruleForm.city"-->
                    <!--                    :options="threeLevelLinkageList"-->
                    <!--                    :props="{ expandTrigger: 'hover', value: 'code', label: 'name' }"-->
                    <!--                    size="small"-->
                    <!--                    placeholder="请选择所在城市"-->
                    <!--                    class="w100"-->
                    <!--                    clearable-->
                    <!--                >-->
                    <!--                </el-cascader>-->
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在行业" prop="industry">
                    <el-select v-model="ruleForm.industry" placeholder="请选择所在行业" clearable class="w100">
                      <el-option
                          v-for="item in industryOptions"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value"
                      ></el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="供应商网站" prop="website">
                    <el-input v-model="ruleForm.website" placeholder="请输入供应商网站" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="法人姓名" prop="legal_person_name">
                    <el-input v-model="ruleForm.legal_person_name" placeholder="请输入法人姓名" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="法人邮箱" prop="legal_person_phone">
                    <el-input v-model="ruleForm.legal_person_phone" placeholder="请输入法人电话" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="法人邮箱" prop="legal_person_email">
                    <el-input v-model="ruleForm.legal_person_email" placeholder="请输入法人邮箱" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="是否启用" prop="is_available">
                    <el-switch v-model="ruleForm.is_available" inline-prompt active-text="Y" inactive-text="N"
                               active-color="green"
                               inactive-color="red"></el-switch>
                  </el-form-item>
                </el-col>
              </el-row>
            </el-form>
          </el-tab-pane>
          <el-tab-pane label="营业执照" name="LicenseTab">
            <el-upload
                class="upload-demo"
                drag
                action=""
            @on-change="handleOnChange"
            :on-success="handleUploadSuccess"
            :http-request="handleHttpRequest"
                multiple
            >
              <el-icon class="el-icon--upload">
                <upload-filled/>
              </el-icon>
              <div class="el-upload__text">
                拖放文件到这里或点击<em>上传图片</em>
              </div>
              <template #tip>
                <div class="el-upload__tip">
                  jpg/png files with a size less than 500kb
                </div>
              </template>
            </el-upload>
          </el-tab-pane>
          <el-tab-pane label="银行对公账户" name="BankAccountTab">
            <el-input v-model="ruleForm.banking_account_info" type="textarea" placeholder="请输入银行对公账户" :rows="8"
                      maxlength="256"></el-input>
          </el-tab-pane>
          <el-tab-pane label="企业描述" name="descriptionTab">
            <el-input v-model="ruleForm.description" type="textarea" placeholder="请输入企业描述" :rows="8"
                      maxlength="256"></el-input>
          </el-tab-pane>

          <el-tab-pane label="是否启用" name="isAvailableTab">
                <el-switch v-model="ruleForm.is_available" inline-prompt active-text="Y" inactive-text="N"
                           active-color="green"
                           inactive-color="red"></el-switch>
                {{ruleForm.is_available}}
            <div>
                供应商状态：<span> {{ruleForm.is_available ? "已激活":"未激活"}}</span>
              <span>新建：供应商处于新创建状态，不可正常使用，若需要正常使用，则更新为“生效”状态<br/>
生效：供应商处于生效状态中，可正常使用<br/>
失效：供应商处于营业执照过期失效中，不可正常使用<br/>
冻结：供应商处理冻结中，不可正常使用</span>
            </div>
          </el-tab-pane>

        </el-tabs>
        <template #footer>
					<span class="dialog-footer">
						<el-button @click="onCancel" size="small">取 消</el-button>
						<el-button type="primary" @click="onSubmit" size="small">确定</el-button>
					</span>
        </template>

      </el-dialog>
    </div>
  </div>
</template>

<script lang="ts">
import {reactive, toRefs, onMounted, ref} from 'vue';
import {updateSupplier} from "/@/api/supplier";
import {ElMessage} from "element-plus";
import type {TabsPaneContext} from 'element-plus'
import { UploadFilled } from '@element-plus/icons-vue'

export default {
  name: 'supplierSupplierInfoSupplierEdit',
  components: {UploadFilled},
  setup() {
    const activeName = ref('baseInfoTab')
    const ruleFormRef = ref(null);
    const state = reactive({
      isShowDialog: false,
      ruleForm: {},

    });

    const handleClick = (tab: TabsPaneContext, event: Event) => {
      console.log(tab, event)
    }

    // 打开弹窗
    const openDialog = (row: any) => {
      console.log('==openDialog.row1==', row);
      state.ruleForm = row;
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

    // 修改
    const onSubmit = async () => {
      console.log('==typeof(state.ruleForm)2==', typeof (state.ruleForm), state.ruleForm)
      updateSupplier(state.ruleForm).then((res: any) => {
        if (res) {
          if (ruleFormRef.value) ruleFormRef.value.resetFields();
          closeDialog();
          ElMessage.success('修改成功！');
        }
      });
    };

    // 初始化城市数据
    const initCityData = () => {
    };

    const handleUploadSuccess = (res: any) => {
      console.log('==handleUploadSuccess->res==', res)
    }

    const handleOnChange = (file: any, fileList: any) => {
      console.log('==handleOnChange==', file)
    }

        const handleHttpRequest = (item: any) => {
      console.log('==handleHttpRequest->item.file==', item.file)
      // form.goods_image = URL.createObjectURL(item.file)  //用示显示的dom
      // form.goods_image = item.file  //转给后台的格式
      state.ruleForm.business_licence_image = item.file  //转给后台的格式
    }


    // 页面加载时
    onMounted(() => {

    });
    return {
      activeName,
      handleClick,
      openDialog,
      closeDialog,
      handleOnChange,
      handleHttpRequest,
      handleUploadSuccess,
      onCancel,
      onSubmit,

      ...toRefs(state),
    };
  },
};
</script>
<style>
.el-dialog__body {
  height: 553px;
}
</style>