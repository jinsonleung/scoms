<template>
	<div class="system-add-dept-container">
		<div v-dialogdrag>
			<el-dialog title="新增企业" v-model="isShowDialog" width="800px">
				<el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" size="small" label-width="110px">
					<el-row :gutter="20">
						<el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12"  class="mb20">
							<el-form-item label="上级企业" prop="enterpriseLevel">
								<el-cascader
									:options="deptData"
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
            <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12"  class="mb20">
            </el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业账号" prop="account">
								<el-input v-model="ruleForm.account" placeholder="请输入企业账号" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业名全称" prop="fullName">
								<el-input v-model="ruleForm.fullName" placeholder="请输入企业名全称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业名简称" prop="abbreviationName">
								<el-input v-model="ruleForm.abbreviationName" placeholder="请输入企业名简称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业类别" prop="classification">
								<el-select v-model="ruleForm.classification" placeholder="请选择企业类别" clearable class="w100">
                  <el-option label="总公司" value="1"></el-option>
                  <el-option label="子公司" value="2"></el-option>
                  <el-option label="办事处" value="3"></el-option>
                  <el-option label="其他" value="4"></el-option>
                </el-select>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业地址" prop="address">
								<el-input v-model="ruleForm.address" placeholder="请输入企业地址" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="所在城市" prop="threeLevelLinkage">
                <el-cascader
                  v-model="threeLevelLinkage"
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
							<el-form-item label="社会信用代码" prop="unifiedSocialCreditCode">
								<el-input v-model="ruleForm.unifiedSocialCreditCode" placeholder="请输入统一社会信用代码" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="成立日期" prop="establishedDate">
                <el-date-picker v-model="ruleForm.establishedDate" type="date" placeholder="请选择成立日期" class="w100"></el-date-picker>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="营业期限(起)" prop="effectiveStartDate">
                <el-date-picker v-model="ruleForm.effectiveStartDate" type="date" placeholder="请选择营业期限(起)" style="width: 100%"></el-date-picker>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="营业期限(止)" prop="effectiveEndDate">
                <el-date-picker v-model="ruleForm.effectiveEndDate" type="date" placeholder="请选择营业期限(止)" style="width: 100%"></el-date-picker>
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
							<el-form-item label="企业描述" prop="description">
								<el-input v-model="ruleForm.description" type="textarea" placeholder="请输入企业描述" :rows="4" maxlength="512"></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="mb20">
							<el-form-item label="备注" prop="remark">
								<el-input v-model="ruleForm.remark" type="textarea" placeholder="请输入备注" maxlength="256"></el-input>
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
import { ref, reactive, toRefs, onMounted } from 'vue';
import { addNewDepartment } from '/@/api/department';
import threeLevelLinkageJson from '/@/mock/threeLevelLinkage.json';

export default {
	name: 'systemAddDept',
	setup() {
    const ruleFormRef = ref(null);
    const state = reactive({
      isShowDialog: false,
      ruleForm: {
        enterpriseLevel: [], // 上级企业
        account: '', // 企业账号
        fullName: '', // 企业名全称
        abbreviationName: '', // 企业名简称
        classification: '', // 企业分类（总部/分公司/子公司
        address: '', // 公司地址
        city: '', // 所在城市
        unifiedSocialCreditCode: '', // 统一社会信用代码
        establishedDate: '', // 成立日期
        effectiveStartDate: '', // 营业期限(起)
        effectiveEndDate: '', // 营业期限(止)
        industry: '', // 所在行业
        legalPersonName: '', // 企业法人姓名
        legalPersonEmail: '', // 企业法人邮箱
        contactName: '', // 联系人姓名
        contactTel: '', // 联系人电话
        contactPhone: '', // 联系人手机
        contactEmail: '', // 联系人邮箱
        description: '', // 企业描述
        remark: '', // 备注
        isAvailable: false, // 是否启用,默认为还没激活
      },
      deptData: [] as Array<any>, // 企业数据
      // 省市区三级联动
      threeLevelLinkage: '',
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
        fullName: {required: true, message: '请输入企业全称', trigger: 'blur'},
        classification: {required: true, message: '请选择企业类别', trigger: 'blur'},
        establishedDate: {required: true, message: '请选择成立日期', trigger: 'blur'},
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
      ruleFormRef.value.resetFields() //type断言机制报错，不要紧
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
		const onSubmit = () => {
			// closeDialog();
			const rest = addNewDepartment({id:'新公司1', tel:'19798323'})
			console.log('==rest==', rest)
		};
		// 初始化企业数据
		const initTableData = () => {
			state.deptData.push({
				deptName: '赛诚国际物流有限公司',
				createTime: new Date().toLocaleString(),
				status: true,
				sort: 0,
				describe: '顶级企业',
				id: Math.random(),
				children: [
					{
						deptName: '赛诚国际物流有限公司',
						createTime: new Date().toLocaleString(),
						status: true,
						sort: Number.parseInt(Math.random()),
						describe: '总部',
						id: Math.random(),
					},
					{
						deptName: '深圳前海赛诚物流有限公司',
						createTime: new Date().toLocaleString(),
						status: true,
						sort: Number.parseInt(Math.random()),
						describe: '分部',
						id: Math.random(),
					},
				],
			});
		};
		// 页面加载时
		onMounted(() => {
			initTableData();
		});
		return {
      ruleFormRef,
      // rules,
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
};
</script>
