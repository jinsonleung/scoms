<template>
  <div class="supplier-add-container">
    <div v-dialogdrag>
      <el-dialog title="新增供应商" v-model="isShowDialog" width="800px">
        <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
          <el-tab-pane label="基本信息" name="baseInfoTab" >
            <el-form ref="ruleFormRef" :model="ruleForm" size="small" label-width="110px">
              <el-row :gutter="10">
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="账号" prop="account">
                    <el-input v-model="ruleForm.account" placeholder="账号自动生成" clearable disabled></el-input>
                  </el-form-item>
                </el-col>
                <!--空列-->
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
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
                          v-for="item in Architectures"
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
                  <el-form-item label="办公地址" prop="office_address">
                    <el-input v-model="ruleForm.office_address" placeholder="请输入办公地址" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="经营范围" prop="business_scope">
                    <el-input v-model="ruleForm.business_scope" placeholder="请输入经营范围" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在国家" prop="country">
                    <el-input v-model="ruleForm.country" placeholder="请选择所在国家" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在省(洲)" prop="province">
                    <el-input v-model="ruleForm.province" placeholder="请选择所在省(洲)" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在城市" prop="city">
                    <el-input v-model="ruleForm.city" placeholder="请选择所在城市" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在区(县)" prop="district">
                    <el-input v-model="ruleForm.district" placeholder="请选择所在区(县)" clearable></el-input>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在行业" prop="industry">
                    <el-select v-model="ruleForm.industry" placeholder="请选择所在行业" clearable class="w100">
                      <el-option
                          v-for="item in Industries"
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
              </el-row>
            </el-form>
          </el-tab-pane>
          <el-tab-pane label="营业执照" name="LicenseTab">
            <el-upload
                ref="uploadRef"
                class="upload-demo"
                drag
                action=""
                accept=".png, .jpg, .jpeg"
                :limit="1"
                :multiple="false"
                :disabled="uploadRef.isUploading"
                :on-change="handleUploadOnChange"
                :before-remove="handleUploadBeforeRemove"
                :on-success="handleUploadSuccess"
                :on-preview="handleUploadPreview"
                :auto-upload="false"
                :http-request="handleUploadHttpRequest"
                :file-list="uploadRef.fileList"
                :on-exceed="handleUploadExceed"
            >
              <el-icon class="el-icon--upload"><upload-filled/></el-icon>
              <div class="el-upload__text">拖放文件到这里或点击<em>上传图片</em></div>
              <template #tip>
                <div class="el-upload__tip">
                  只能上传一张作为营业执照格式为 jpg/jpeg/png，不超过 2MB
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
          <el-tab-pane label="状态" name="statusTab">
                <el-form size="small" label-width="110px">
                  <el-row :gutter="10">
                    <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="mb20">
                      <el-form-item label="状态" prop="status">
                        <el-select v-model="ruleForm.status" placeholder="Select">
                          <el-option
                            v-for="item in statusOptions"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value"
                            :disabled="item.disabled"

                          >
                            <span style="float: left">{{ item.label }}</span>
                            <span
                              style="
                                float: right;
                                color: var(--el-text-color-secondary);
                                font-size: 13px;
                              "
                              >{{ item.value }}</span
                            >
                          </el-option>
                        </el-select>
                      </el-form-item>
                    </el-col>
                    <el-col :xs="24" :sm="12" :md="24" :lg="24" :xl="24" class="mb20">
                      <el-form-item label="状态备注" prop="status_description">
                        <el-input v-model="ruleForm.status_description" type="textarea" :rows="8" maxlength="256" placeholder="请输入状态备注" clearable></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :xs="24" :sm="12" :md="24" :lg="24" :xl="24" class="mb20">
                      <el-form-item label="状态说明" >
                        <div class="statusDesc">
                          <ul>
                            <li>新建[自动设置]：供应商处于新创建状态，不可正常使用，若需要正常使用，则更新为“生效”状态</li>
                            <li>生效[需手动设置]：供应商处于生效状态中，可正常使用</li>
                            <li>失效[自动设置]：供应商处于营业执照过期失效中，不可正常使用</li>
                            <li>冻结[需手动设置]：供应商处于冻结中，不可正常使用</li>
                          </ul>
                        </div>
                      </el-form-item>
                    </el-col>

                  </el-row>
                </el-form>

          </el-tab-pane>

        </el-tabs>
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

<!--2022/4/1drf提交文件异常解决方法-->
<!--https://huyu.info/blog/detail/148-->

<script lang="ts">
import {reactive, toRefs, onMounted, ref, getCurrentInstance} from 'vue';
import {addSupplier, updateSupplier} from "/@/api/supplier";
import {ElMessage,ElNotification} from "element-plus";
import type {TabsPaneContext } from 'element-plus';
import {UploadFilled} from '@element-plus/icons-vue';
import {CompanyTypes, Architectures, Industries} from '/@/utils/publicOptionItems';
import {objectToFormData} from '/@/utils/tsHelper'
import {Session} from "/@/utils/storage";
import {addNewEnterprise} from "/@/api/enterprise";

export default {
  name: 'supplierAddSupplier',
  components: {UploadFilled},
  setup() {
    const { proxy }  = getCurrentInstance() as any;
    const activeName = ref('baseInfoTab');
    const ruleFormRef = ref(null);
    const statusValue = ref('');
    const state = reactive({
      isShowDialog: false,
      ruleForm: {
        account: '',
        abbreviation_name: '',
        full_name: '',
        architecture: '',
        unified_social_credit_code: '',
        business_licence_image: '',
        registered_capital: '',
        registered_address: '',
        established_date: '',
        effective_start_date: '',
        effective_end_date: '',
        office_address: '',
        business_scope: '',
        country: '',
        province: '',
        city: '',
        district: '',
        industry: '',
        website: '',
        legal_person_name: '',
        legal_person_phone: '',
        legal_person_email: '',
        banking_account_info: '',
        description: '',
        status: '',
        status_description: '',
      },
    });
    const uploadRef = reactive({
      open: false,  // 是否显示弹出层（放在el-dialog :visible.syn="upload.open"）
      title: '',  // 弹出层的标题（放在el-dialog :title="upload.title"）
      isUploading: false,  // 是否禁用上传
      updateSupport: 0,   // 是否更新已存在的用户数据
      // headers: {Authorization: getToken()},   // 上传请求头
      url: import.meta.env.VITE_API_URL + 'media/businessLicenceImage/upload',   // 上传地址
      fileList: [],   //文件列表
      fileNames: [],   //文件名列表
    });


    // const formData= new FormData();

    const statusOptions = [
  {
    value: '自动生成',
    label: '新建',
    disabled: true,
  },
  {
    value: '手动配置',
    label: '生效',
  },
  {
    value: '自动生成',
    label: '失效',
    disabled: true,
  },
  {
    value: '手动配置',
    label: '冻结',
  },
];

    const handleClick = (tab: TabsPaneContext, event: Event) => {
      console.log(tab, event)
    }

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



    // 修改
    const onSubmit_old = async () => {
      // 文件及图片上传请求头中content-type必须是”mulpart/form-data"，服务端DRF只能接受表单格式数据
      // 创建新表单数据对象
      let formData = new FormData();
      formData = objectToFormData(state.ruleForm)
      //将上传文件放到数据对象中，保存文件名
      uploadRef.fileList.forEach((file:any)=>{
        formData.append('files', file.raw);
        uploadRef.fileNames.push(file.name);
      })
      // 将上传文件名放到数据对象中
      formData.append('fileNames', uploadRef.fileNames);
      // 移除联系人信息，联系人信息单独处理
      formData.delete('contact')
      // formData.delete('business_licence_image')

      // 发送axios请求
      updateSupplier(formData).then((res: any) => {
        if (res) {
        }
      });
    };

    // 文件上传成功时的钩子
    const handleUploadSuccess = (res: any) => {
      ElMessage.success('文件上传成功啦。。。。')
      // console.log('==handleUploadSuccess->res==', res)
    }

    // 文件状态改变时的钩子，添加文件、上传成功和上传失败时都会被调用
    const handleUploadOnChange = (file: any, fileList: any) => {

      uploadRef.fileList = fileList;
      console.log('==handleUploadOnChange==', fileList)
      // console.log('==uploadRef.fileList==', uploadRef.fileList)

    }
    // 删除文件之前的钩子
    const handleUploadBeforeRemove = (file: any, fileList: any) => {
      uploadRef.fileList = fileList;
      // console.log('==handleUploadOnChange==', fileList)
      // console.log('==uploadRef.fileList==', uploadRef.fileList)
    };

    const handleUploadHttpRequest = (item: any) => {
    };

    // 当超出个数限制时执行的钩子函数
    const handleUploadExceed = (files: any, fileList: any)=>{
      console.log('==proxy.uploadRef.fileList.length==', proxy.uploadRef.fileList.length)
      console.log('==fileList.length==', fileList.length)
      if (fileList.length==1){
        ElMessage.warning('只能上传一个图片文件，请移除不需要的再重新上传');
      }
    };

    //点击文件列表中已上传的文件时的钩子
    const handleUploadPreview=(file: any)=>{
        ElMessage.info('preview pic');
    };



    // 页面加载时
    onMounted(() => {
      state.ruleForm.status=statusOptions[0].value;
    });
    return {
      ruleFormRef,
      statusValue,
      statusOptions,
      activeName,
      CompanyTypes,
      Architectures,
      Industries,
      handleClick,
      openDialog,
      closeDialog,
      handleUploadOnChange,
      handleUploadBeforeRemove,
      handleUploadHttpRequest,
      handleUploadSuccess,
      handleUploadPreview,
      handleUploadExceed,
      onCancel,
      onSubmit,
      uploadRef,
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