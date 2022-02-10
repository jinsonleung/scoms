<template>
  <div class="system-add-dept-container">
    <div v-dialogdrag>
      <el-dialog title="新增企业" v-model="isShowDialog" width="800px">
        <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" size="small" label-width="110px">
          <el-row :gutter="10">
            <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="上级企业" prop="superior_level">
                <el-cascader
                    :options="enterpriseData"
                    :props="{ checkStrictly: true, value: 'deptName', label: 'deptName' }"
                    placeholder="请选择上级企业"
                    clearable
                    class="w100"
                    v-model="ruleForm.superior_level"
                >
                  <template #default="{ node, data }">
                    <span>{{ data.deptName }}</span>
                    <span v-if="!node.isLeaf"> ({{ data.children.length }}) </span>
                  </template>
                </el-cascader>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12" class="mb20">
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业账号" prop="account">
                <el-input v-model="ruleForm.account" placeholder="请输入企业账号" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业名全称" prop="full_name">
                <el-input v-model="ruleForm.full_name" placeholder="请输入企业名全称" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业名简称" prop="abbreviation_name">
                <el-input v-model="ruleForm.abbreviation_name" placeholder="请输入企业名简称" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业类型" prop="enterprise_type">
                <el-select v-model="ruleForm.enterprise_type" placeholder="请选择企业类型" clearable class="w100">
                  <el-option
                    v-for="item in enterpriseTypeOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  ></el-option>
                </el-select>
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
                <!--输入后将小写自动转为大写-->
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
              <el-form-item label="企业地址" prop="address">
                <el-input v-model="ruleForm.address" placeholder="请输入企业地址" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="所在城市" prop="city">
                <el-cascader
                    v-model="ruleForm.city"
                    :options="threeLevelLinkageList"
                    :props="{ expandTrigger: 'hover', value: 'code', label: 'name' }"
                    size="small"
                    placeholder="请选择所在城市"
                    class="w100"
                    clearable
                >
                </el-cascader>
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
              <el-form-item label="企业网站" prop="website">
                <el-input v-model="ruleForm.website" placeholder="请输入企业网站" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业法人姓名" prop="legal_person_name">
                <el-input v-model="ruleForm.legal_person_name" placeholder="请输入企业法人姓名" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业法人邮箱" prop="legal_person_email">
                <el-input v-model="ruleForm.legal_person_email" placeholder="请输入企业法人邮箱" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="联系人姓名" prop="contact_name">
                <el-input v-model="ruleForm.contact_name" placeholder="请输入联系人姓名" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="联系人电话" prop="contact_tel">
                <el-input v-model="ruleForm.contact_tel" placeholder="请输入联系人电话" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="联系人手机" prop="contact_phone">
                <el-input v-model="ruleForm.contact_phone" placeholder="请输入联系人手机" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="联系人邮箱" prop="contact_email">
                <el-input v-model="ruleForm.contact_email" placeholder="请输入联系人邮箱" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="mb20">
              <el-form-item label="经营范围" prop="business_scope">
                <el-input v-model="ruleForm.business_scope" type="textarea" placeholder="请输入经营范围" :rows="6"
                          maxlength="512"></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="mb20">
              <el-form-item label="备注" prop="remark">
                <el-input v-model="ruleForm.remark" type="textarea" placeholder="请输入备注" :rows="4"
                          maxlength="256"></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="是否启用" prop="is_available">
                <el-switch v-model="ruleForm.is_available" inline-prompt active-text="启" inactive-text="否"></el-switch>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
        <template #footer>
					<span class="dialog-footer">
						<el-button @click="onReset" size="small">重 置</el-button>
						<el-button @click="onCancel" size="small">取 消</el-button>
						<el-button type="primary" @click="onSubmit" size="small">新 增</el-button>
					</span>
        </template>
      </el-dialog>
    </div>
  </div>
</template>

<script lang="ts">
import {ref, reactive, toRefs, onMounted} from 'vue';
import {addNewEnterprise} from '/@/api/enterprise';
import threeLevelLinkageJson from '/@/mock/threeLevelLinkage.json';
import {Session} from "/@/utils/storage";
import {ElMessage} from "element-plus";
import {enterpriseTypeOptions, enterpriseArchitectureOptions, industryOptions} from '/@/views/system/enterprise/enterpriseOptions';

export default {
  name: 'systemAddEnterprise',
  setup() {
    const ruleFormRef = ref(null);
    const state = reactive({
      isShowDialog: false,
      ruleForm: {
        superior_level: '', // 上级企业
        account: '', // 企业账号
        full_name: '', // 企业名全称
        abbreviation_name: '', // 企业名简称
        enterprise_type: '', // 企业类型（外商投资企业/股份制企业/私营企业/其他）
        architecture: '', // 体系结构（总部/子公司/办事事/其他）
        unified_social_credit_code: '', // 统一社会信用代码
        registered_capital: '人民币0.0000万',  // 注册资本，默认为:人民币0.0000万
        established_date: '', // 成立日期
        effective_start_date: '', // 营业期限(起)
        effective_end_date: '', // 营业期限(止)
        address: '', // 公司地址
        city: '', // 省市区三级联动
        industry: '', // 所在行业
        website: '', // 企业网站
        legal_person_name: '', // 企业法人姓名
        legal_person_email: '', // 企业法人邮箱
        contact_name: '', // 联系人姓名
        contact_tel: '', // 联系人电话
        contact_phone: '', // 联系人手机
        contact_email: '', // 联系人邮箱
        business_scope: '', // 经营范围
        remark: '', // 备注
        is_available: false, // 是否启用,默认为还没激活
        create_by: '',  //创建人
        update_by: '',  //更新人
      },
      enterpriseData: [] as Array<any>, // 企业数据
      // 省市区三级联动
      // threeLevelLinkage: '',
      threeLevelLinkageList: [],
      linkage: {
        province: '',
        city: '',
        area: '',
        provinceList: [], // 省
        cityList: [], // 市
        areaList: [], // 区
      },
      // 表单检验规则
      rules: {
        account: {required: true, message: '请输入企业账号', trigger: 'blur'},
        full_name: {required: true, message: '请输入企业名全称', trigger: 'blur'},
        abbreviation_name: {required: true, message: '请输入企业名简称', trigger: 'blur'},
        enterprise_type: {required: true, message: '请选择企业类型', trigger: 'blur'},
        architecture: {required: true, message: '请选择体系结构', trigger: 'blur'},
        established_date: {required: true, message: '请选择成立日期', trigger: 'blur'},
        industry: {required: true, message: '请选择所在行业', trigger: 'blur'},
      },
    });

    // 初始化城市数据
    const initCityData = () => {
      state.threeLevelLinkageList = threeLevelLinkageJson;
      state.linkage.provinceList = threeLevelLinkageJson;
    };
    // 省下拉改变时
    const onProvinceChange = (name: string) => {
      state.linkage.city = '';
      state.linkage.area = '';
      state.linkage.cityList = [];
      state.linkage.areaList = [];
      state.linkage.provinceList.map((v: any) => {
        if (v.name === name) state.linkage.cityList = v.children;
      });
    };
    // 市下拉改变时
    const onCityChange = (name: string) => {
      state.linkage.area = '';
      state.linkage.areaList = [];
      state.linkage.cityList.map((v: any) => {
        if (v.name === name) state.linkage.areaList = v.children;
      });
    };
    // 页面加载时
    onMounted(() => {
      initCityData();
    });

    // 重置表单
    const onReset = () => {
      // resetFields不是vue函数，是element ui函数，type断言机制报红，不要紧
      if (ruleFormRef.value) ruleFormRef.value.resetFields()
    };

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
    // 新增
    const onSubmit = async () => {
      state.ruleForm.create_by = Session.get('userInfo').userName;
      state.ruleForm.update_by = Session.get('userInfo').userName;
      // 将省市区三级联动list转为字符串，如['220000', '220300', '220322']，转为'220000,220300,220322'
      console.log('==typeof(state.ruleForm.city)==', typeof(state.ruleForm.city))
      if (typeof(state.ruleForm.city) === "object") state.ruleForm.city = state.ruleForm.city.join(',')
      console.log('==type(state.ruleForm)==', state.ruleForm)
      addNewEnterprise(state.ruleForm).then((res: any) => {
        console.log('==res==', res)
        if (res) {
          // if (ruleFormRef.value) ruleFormRef.value.resetFields();
          ElMessage.success('修改企业成功！');
        }
      }).catch((e:any)=>{
        console.log('==e==', e)

      });
    };

    return {
      ruleFormRef,
      // rules,
      enterpriseTypeOptions,
      enterpriseArchitectureOptions,
      industryOptions,
      onReset,
      onProvinceChange,
      onCityChange,
      openDialog,
      closeDialog,
      onCancel,
      onSubmit,
      ...toRefs(state),
    };
  },
}
</script>
