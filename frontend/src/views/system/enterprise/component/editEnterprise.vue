<template>
	<div class="system-edit-dept-container">
		<div v-dialogdrag>
      <el-dialog title="修改企业信息" v-model="isShowDialog" width="800px">
        <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" size="small" label-width="110px">
          <el-row :gutter="10">
            <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="上级企业" prop="enterpriseLevel">
                <el-cascader
                    :options="enterpriseData"
                    :props="{ checkStrictly: true, value: 'deptName', label: 'deptName' }"
                    placeholder="请选择上级企业"
                    clearable
                    class="w100"
                    v-model="ruleForm.enterpriseLevel"
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
              <el-form-item label="企业名简称" prop="abbreviationName">
                <el-input v-model="ruleForm.abbreviationName" placeholder="请输入企业名简称" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业类型" prop="enterpriseType">
                <el-select v-model="ruleForm.enterpriseType" placeholder="请选择企业类型" clearable class="w100">
                  <el-option label="外商投资企业" value="1"></el-option>
                  <el-option label="股份制企业" value="2"></el-option>
                  <el-option label="私营企业" value="3"></el-option>
                  <el-option label="其他" value="4"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="体系结构" prop="architecture">
                <el-select v-model="ruleForm.architecture" placeholder="请选择体系结构" clearable class="w100">
                  <el-option label="总公司" value="1"></el-option>
                  <el-option label="子公司" value="2"></el-option>
                  <el-option label="办事处" value="3"></el-option>
                  <el-option label="其他" value="4"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="社会信用代码" prop="unifiedSocialCreditCode">
                <!--输入后将小写自动转为大写-->
                <el-input v-model="ruleForm.unifiedSocialCreditCode" placeholder="请输入统一社会信用代码"
                          onkeyup="this.value=this.value.toUpperCase()" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="注册资本" prop="registeredCapital">
                <el-input v-model="ruleForm.registeredCapital" placeholder="请输入注册资本" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="成立日期" prop="establishedDate">
                <el-date-picker v-model="ruleForm.establishedDate" type="date" placeholder="请选择成立日期"
                                value-format="YYYY-MM-DD" class="w100"></el-date-picker>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="营业期限(起)" prop="effectiveStartDate">
                <el-date-picker v-model="ruleForm.effectiveStartDate" type="date" placeholder="请选择营业期限(起)"
                                value-format="YYYY-MM-DD" class="w100"></el-date-picker>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="营业期限(止)" prop="effectiveEndDate">
                <el-date-picker v-model="ruleForm.effectiveEndDate" type="date" placeholder="请选择营业期限(止)"
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
                  <el-option label="物流运输" value="1"></el-option>
                  <el-option label="国际贸易" value="2"></el-option>
                  <el-option label="跨境电商" value="3"></el-option>
                  <el-option label="其他" value="4"></el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业网站" prop="website">
                <el-input v-model="ruleForm.website" placeholder="请输入企业网站" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业法人姓名" prop="legalPersonName">
                <el-input v-model="ruleForm.legalPersonName" placeholder="请输入企业法人姓名" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="企业法人邮箱" prop="legalPersonEmail">
                <el-input v-model="ruleForm.legalPersonEmail" placeholder="请输入企业法人邮箱" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="联系人姓名" prop="contactName">
                <el-input v-model="ruleForm.contactName" placeholder="请输入联系人姓名" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="联系人电话" prop="contactTel">
                <el-input v-model="ruleForm.contactTel" placeholder="请输入联系人电话" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="联系人手机" prop="contactPhone">
                <el-input v-model="ruleForm.contactPhone" placeholder="请输入联系人手机" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
              <el-form-item label="联系人邮箱" prop="contactEmail">
                <el-input v-model="ruleForm.contactEmail" placeholder="请输入联系人邮箱" clearable></el-input>
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="mb20">
              <el-form-item label="经营范围" prop="businessScope">
                <el-input v-model="ruleForm.businessScope" type="textarea" placeholder="请输入经营范围" :rows="6"
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
              <el-form-item label="是否启用" prop="isAvailable">
                <el-switch v-model="ruleForm.isAvailable" inline-prompt active-text="启" inactive-text="否"></el-switch>
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
import {reactive, toRefs, onMounted, ref} from 'vue';
import {addNewEnterprise} from "/@/api/enterprise";
import {ResponseData} from "/@/store/interface";
export default {
	name: 'systemEditEnterprise',
	setup() {
    const ruleFormRef = ref(null);
    const state = reactive({
      isShowDialog: false,
      ruleForm: {
        enterpriseLevel: '', // 上级企业
        account: '', // 企业账号
        full_name: '', // 企业名全称
        abbreviationName: '', // 企业名简称
        enterpriseType: '', // 企业类型（外商投资企业/股份制企业/私营企业/其他）
        architecture: '', // 体系结构（总部/子公司/办事事/其他）
        unifiedSocialCreditCode: '', // 统一社会信用代码
        registeredCapital: '人民币0.0000万',  // 注册资本，默认为:人民币0.0000万
        establishedDate: '', // 成立日期
        effectiveStartDate: '', // 营业期限(起)
        effectiveEndDate: '', // 营业期限(止)
        address: '', // 公司地址
        city: '', // 省市区三级联动
        industry: '', // 所在行业
        website: '', // 企业网站
        legalPersonName: '', // 企业法人姓名
        legalPersonEmail: '', // 企业法人邮箱
        contactName: '', // 联系人姓名
        contactTel: '', // 联系人电话
        contactPhone: '', // 联系人手机
        contactEmail: '', // 联系人邮箱
        businessScope: '', // 经营范围
        remark: '', // 备注
        isAvailable: false, // 是否启用,默认为还没激活
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
        abbreviationName: {required: true, message: '请输入企业名简称', trigger: 'blur'},
        enterpriseType: {required: true, message: '请选择企业类型', trigger: 'blur'},
        architecture: {required: true, message: '请选择体系结构', trigger: 'blur'},
        establishedDate: {required: true, message: '请选择成立日期', trigger: 'blur'},
        industry: {required: true, message: '请选择所在行业', trigger: 'blur'},
      },
    });
		// 打开弹窗
		const openDialog = (row: Object) => {
      console.log('==edit->row==', row)
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
		// 新增
		const onSubmit = () => {
			closeDialog();
		};
		// 初始化企业数据
		// const initTableData = () => {
		// 	state.deptData.push({
		// 		deptName: 'vueNextAdmin',
		// 		createTime: new Date().toLocaleString(),
		// 		status: true,
		// 		sort: Number.parseInt(Math.random()),
		// 		describe: '顶级企业',
		// 		id: Math.random(),
		// 		children: [
		// 			{
		// 				deptName: 'IT外包服务',
		// 				createTime: new Date().toLocaleString(),
		// 				status: true,
		// 				sort: Number.parseInt(Math.random()),
		// 				describe: '总部',
		// 				id: Math.random(),
		// 			},
		// 			{
		// 				deptName: '资本控股',
		// 				createTime: new Date().toLocaleString(),
		// 				status: true,
		// 				sort: Number.parseInt(Math.random()),
		// 				describe: '分部',
		// 				id: Math.random(),
		// 			},
		// 		],
		// 	});
		// };
		// 页面加载时
		onMounted(() => {
			// initTableData();
		});
		return {
			openDialog,
			closeDialog,
			onCancel,
			onSubmit,
			...toRefs(state),
		};
	},
};
</script>
