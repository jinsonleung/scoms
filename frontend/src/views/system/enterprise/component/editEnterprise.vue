<template>
	<div class="system-edit-dept-container">
		<div v-dialogdrag>
			<el-dialog title="修改企业" v-model="isShowDialog" width="769px">
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
							<el-form-item label="企业名称">
								<el-input v-model="ruleForm.deptName" placeholder="请输入企业名称" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="负责人">
								<el-input v-model="ruleForm.person" placeholder="请输入负责人" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="手机号">
								<el-input v-model="ruleForm.phone" placeholder="请输入手机号" clearable></el-input>
							</el-form-item>
						</el-col>
						<el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12" class="mb20">
							<el-form-item label="邮箱">
								<el-input v-model="ruleForm.email" placeholder="请输入" clearable></el-input>
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
						<el-button type="primary" @click="onSubmit" size="small">修 改</el-button>
					</span>
				</template>
			</el-dialog>
		</div>
	</div>
</template>

<script lang="ts">
import { reactive, toRefs, onMounted } from 'vue';
import {addNewEnterprise} from "/@/api/enterprise";
import {ResponseData} from "/@/store/interface";
export default {
	name: 'systemEditDept',
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
			deptData: [], // 企业数据
		});
		// 打开弹窗
		const openDialog = (row: Object) => {
			row.deptLevel = ['vueNextAdmin'];
			row.person = 'lyt';
			row.phone = '12345678910';
			row.email = 'vueNextAdmin@123.com';
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
		const initTableData = () => {
			state.deptData.push({
				deptName: 'vueNextAdmin',
				createTime: new Date().toLocaleString(),
				status: true,
				sort: Number.parseInt(Math.random()),
				describe: '顶级企业',
				id: Math.random(),
				children: [
					{
						deptName: 'IT外包服务',
						createTime: new Date().toLocaleString(),
						status: true,
						sort: Number.parseInt(Math.random()),
						describe: '总部',
						id: Math.random(),
					},
					{
						deptName: '资本控股',
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
