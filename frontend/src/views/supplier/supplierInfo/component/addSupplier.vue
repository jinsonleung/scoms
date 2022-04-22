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
                    <el-input v-model="ruleForm.account" placeholder="账号自动生成" disabled></el-input>
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
                          v-for="item in CompanyArchitectureTypes"
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
                    <el-select v-model="ruleForm.country" placeholder="请选择国家" size="small" clearable @change="onCountryChange" class="w100">
                      <el-option v-for="(v, k) in linkage.countryList" :key="k" :label="v.chn_name" :value="v.chn_name">
                            <span style="float: left">{{ v.chn_name }}</span>
                            <span style="float: right; color: var(--el-text-color-secondary);font-size: 13px;">{{ v.eng_name }}</span>
                      </el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在省(洲)" prop="province">
                    <el-select v-model="ruleForm.province" placeholder="请选择省(洲)" size="small" clearable @change="onProvinceChange" class="w100">
                      <el-option v-for="(v, k) in linkage.provinceList" :key="k" :label="v.chn_name" :value="v.chn_name">
                              <span style="float: left">{{ v.chn_name }}</span>
                              <span
                                style="
                                  float: right;
                                  color: var(--el-text-color-secondary);
                                  font-size: 13px;
                                "
                                >{{ v.eng_name }}</span
                              >
                      </el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在城市" prop="city">
                    <el-select v-model="ruleForm.city" placeholder="请选择城市" size="small" clearable @change="onCityChange" class="w100">
                      <el-option v-for="(v, k) in linkage.cityList" :key="k" :label="v.chn_name" :value="v.chn_name">
                              <span style="float: left">{{ v.chn_name }}</span>
                              <span
                                style="
                                  float: right;
                                  color: var(--el-text-color-secondary);
                                  font-size: 13px;
                                "
                                >{{ v.eng_name }}</span
                              >
                      </el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="所在区(县)" prop="district">
                    <el-select v-model="ruleForm.district" placeholder="请选择所在区(县)" size="small" clearable @change="onDistrictChange" class="w100">
                      <el-option v-for="(v, k) in linkage.districtList" :key="k" :label="v.chn_name" :value="v.chn_name">
                              <span style="float: left">{{ v.chn_name }}</span>
                              <span
                                style="
                                  float: right;
                                  color: var(--el-text-color-secondary);
                                  font-size: 13px;
                                "
                                >{{ v.eng_name }}</span
                              >
                      </el-option>
                    </el-select>
                  </el-form-item>
                </el-col>
                <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
                  <el-form-item label="公司类型" prop="enterprise_type">
                    <el-select v-model="ruleForm.enterprise_type" placeholder="请选择服务类型" clearable class="w100">
                      <el-option
                          v-for="item in SupplierServiceTypes"
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
          <el-tab-pane label="使用状态" name="statusTab">
                <el-form size="small" label-width="110px">
                  <el-row :gutter="10">
                    <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="mb20">
                      <el-form-item label="使用状态" prop="status">
                        <el-select v-model="ruleForm.status" placeholder="Select" disabled>
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
import {addSupplier} from "/@/api/supplier";
import {ElMessage} from "element-plus";
import type {TabsPaneContext } from 'element-plus';
import {UploadFilled} from '@element-plus/icons-vue';
import {CompanyTypes, CompanyArchitectureTypes, SupplierServiceTypes} from '/@/utils/publicOptionItems';
import {objectToFormData} from '/@/utils/tsHelper'
import {get4LinkageList} from "/@/utils/globalCountry4LevelLinkage";


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
        enterprise_type: '',
        website: '',
        legal_person_name: '',
        legal_person_phone: '',
        legal_person_email: '',
        banking_account_info: '',
        description: '',
        status: '',
        status_description: '',
      },
      // 全球国家省市区4层级联
      global4LevelLink: '',
      global4LevelLinkList: [],
      linkage: {
        countryList: [], // 国家
        provinceList: [], // 省
        cityList: [], // 市
        districtList: [], // 区
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
    value: '新建',
    label: '新建',
    disabled: true,
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
          ElMessage.success('新增供应商成功！');
        };
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
      // console.log('==handleUploadOnChange==', fileList)
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
      // console.log('==proxy.uploadRef.fileList.length==', proxy.uploadRef.fileList.length)
      // console.log('==fileList.length==', fileList.length)
      if (fileList.length==1){
        ElMessage.warning('只能上传一个图片文件，请移除不需要的再重新上传');
      }
    };

    //点击文件列表中已上传的文件时的钩子
    const handleUploadPreview=(file: any)=>{
        ElMessage.info('preview pic');
    };

    // 初始化国家省市区数据
		const init4LevelLinkage = () => {
      state.linkage.countryList = get4LinkageList(0)
		};
  // 国家下拉事件
		const onCountryChange = (selVal: string) => {
			state.linkage.provinceList = get4LinkageList(1, selVal);
      state.ruleForm.province = '';
			state.ruleForm.city = '';
			state.ruleForm.district = '';
			state.linkage.cityList = [];
			state.linkage.districtList = [];
		};

    // 省（洲）下拉事件
    const onProvinceChange = (selVal: any) => {
			state.linkage.cityList = get4LinkageList(2, selVal);
      state.ruleForm.city = '';
			state.ruleForm.district = '';
			state.linkage.districtList = [];
    }

    // 市下拉事件
    const onCityChange = (selVal: any) => {
      // 获取市的区域编号
      state.linkage.districtList = get4LinkageList(3, selVal);
      state.ruleForm.district = '';
    }

    // 区（县）下拉事件
    const onDistrictChange = (selVal: any) => {
      // 获取市的区域编号
      // console.log('district==', selVal)
    }
    // 页面加载时
    onMounted(() => {
      state.ruleForm.status=statusOptions[0].value;
      init4LevelLinkage();
    });
    return {
      ruleFormRef,
      statusValue,
      statusOptions,
      activeName,
      CompanyTypes,
      CompanyArchitectureTypes,
      SupplierServiceTypes,
      handleClick,
      openDialog,
      closeDialog,
      handleUploadOnChange,
      handleUploadBeforeRemove,
      handleUploadHttpRequest,
      handleUploadSuccess,
      handleUploadPreview,
      handleUploadExceed,
      init4LevelLinkage,
      onCountryChange,
      onProvinceChange,
      onCityChange,
      onDistrictChange,
      onCancel,
      onSubmit,
      uploadRef,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss" scoped>
@import "/@/theme/public/elementui-reset.scss";

//:deep(.el-dialog) {
//  border-radius: 5px;
//  margin: 0 !important;
//  .el-dialog__header{
//    //height: 40px;
//    border-radius: 5px;
//    padding: 6px 10px 5px 15px;
//    background-color: #ace5ac;
//  }
//  .el-dialog__headerbtn{
//    top:10px;
//    font-size: 18px;
//  }
//  .el-dialog__title{
//    font-size: 16px;
//  }
//  .el-dialog__body {
//  height: 555px !important;
//  }
//}

.statusDesc {
  margin: 0;
  padding: 0;

  li {
    font-size: small;
    list-style: none;
    line-height: 20px;
  }
}

</style>