<template>
	<div class="system-add-dept-container">
		<div v-dialogdrag>
			<el-dialog title="新增企业" v-model="isShowDialog" width="769px">
				<el-form :model="ruleForm" size="small" label-width="90px">
					<el-row :gutter="35">
						<el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="mb20">
							<el-form-item label="上级企业">
								<el-cascader
									:options="deptData"
									:props="{ checkStrictly: true, value: 'deptName', label: 'deptName' }"
									placeholder="请选择企业"
									clearable
									class="w100"
									v-model="ruleForm.deptLevel"
								>
									<template #default="{ node, data }">
										<span>{{ data.deptName }}</span>
										<span v-if="!node.isLeaf"> ({{ data.children.length }}) </span>
									</template>
								</el-cascader>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业账号">
								<el-input v-model="ruleForm.deptName" placeholder="请输入企业账号" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业名全称">
								<el-input v-model="ruleForm.person" placeholder="请输入企业名全称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业名简称">
								<el-input v-model="ruleForm.phone" placeholder="请输入企业名简称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业类别">
								<el-input v-model="ruleForm.email" placeholder="请输入企业类别" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业名简称">
								<el-input v-model="ruleForm.phone" placeholder="请输入企业名简称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业类别">
								<el-input v-model="ruleForm.email" placeholder="请输入企业类别" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业名简称">
								<el-input v-model="ruleForm.phone" placeholder="请输入企业名简称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业类别">
								<el-input v-model="ruleForm.email" placeholder="请输入企业类别" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业名简称">
								<el-input v-model="ruleForm.phone" placeholder="请输入企业名简称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业类别">
								<el-input v-model="ruleForm.email" placeholder="请输入企业类别" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业名简称">
								<el-input v-model="ruleForm.phone" placeholder="请输入企业名简称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业类别">
								<el-input v-model="ruleForm.email" placeholder="请输入企业类别" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="排序">
								<el-input-number v-model="ruleForm.sort" :min="0" :max="999" controls-position="right" placeholder="请输入排序" class="w100" />
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="企业状态">
								<el-switch v-model="ruleForm.status" inline-prompt active-text="启" inactive-text="禁"></el-switch>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="mb20">
							<el-form-item label="企业描述">
								<el-input v-model="ruleForm.describe" type="textarea" placeholder="请输入企业描述" maxlength="150"></el-input>
							</el-form-item>
						</el-col>
					</el-row>
				</el-form>
				<template #footer>
					<span class="dialog-footer">
						<el-button @click="onCancel" size="small">取 消</el-button>
						<el-button type="primary" @click="onSubmit" size="small">新 增</el-button>
					</span>
				</template>
			</el-dialog>
		</div>
	</div>
</template>

<script lang="ts">
import { reactive, toRefs, onMounted } from 'vue';
import { addNewDepartment, editDepartment } from '/@/api/department';
export default {
	name: 'systemAddDept',
	setup() {
		const state = reactive({
			isShowDialog: false,
			ruleForm: {
				deptLevel: [], // 上级企业
				deptName: '', // 企业名称
				person: '', // 负责人
				phone: '', // 手机号
				email: '', // 邮箱
				sort: 0, // 排序
				status: true, // 企业状态
				describe: '', // 企业描述
			},
			deptData: [] as Array<any>, // 企业数据
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
			openDialog,
			closeDialog,
			onCancel,
			onSubmit,
			...toRefs(state),
		};
	},
};
</script>
