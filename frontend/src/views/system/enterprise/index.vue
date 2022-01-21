<template>
	<div class="system-dept-container">
		<el-card shadow="hover">
      <!--查询栏-->
			<div class="system-dept-search mb15">
				<el-input size="small" placeholder="请输入企业名称" style="max-width: 180px"> </el-input>
				<el-button size="small" type="primary" class="ml10">
					<el-icon>
						<elementSearch />
					</el-icon>
					查询
				</el-button>
				<el-button size="small" type="success" class="ml10" @click="onOpenAddDept">
					<el-icon>
						<elementFolderAdd />
					</el-icon>
					新增企业
				</el-button>
			</div>
      <!--数据列表栏-->
			<el-table
				:data="tableData.data"
				style="width: 100%"
				row-key="id"
				default-expand-all
				:tree-props="{ children: 'children', hasChildren: 'hasChildren' }"
			>
				<el-table-column prop="account" label="企业账号" show-overflow-tooltip> </el-table-column>
				<el-table-column prop="full_name" label="企业名全称" show-overflow-tooltip> </el-table-column>
				<el-table-column prop="abbreviation_name" label="企业名简称" show-overflow-tooltip> </el-table-column>
				<el-table-column prop="enterprise_type" label="企业类型" show-overflow-tooltip> </el-table-column>
				<el-table-column prop="architecture" label="体系xfsw" show-overflow-tooltip> </el-table-column>
				<el-table-column prop="unified_social_credit_code" label="社会信用代码" show-overflow-tooltip> </el-table-column>
				<el-table-column prop="established_date" label="成立日期" show-overflow-tooltip> </el-table-column>
				<el-table-column prop="status" label="企业状态" show-overflow-tooltip>
					<template #default="scope">
						<el-tag type="success" size="small" v-if="scope.row.is_available">启用</el-tag>
						<el-tag type="info" size="small" v-else>禁用</el-tag>
					</template>
				</el-table-column>

        <el-table-column label="操作" show-overflow-tooltip width="140">
					<template #default="scope">
						<el-button size="mini" type="text" @click="onOpenAddDept(scope.row)">新增</el-button>
						<el-button size="mini" type="text" @click="onOpenEditDept(scope.row)">修改</el-button>
						<el-button size="mini" type="text" @click="onTabelRowDel(scope.row)">删除</el-button>
					</template>
				</el-table-column>
			</el-table>
		</el-card>
    <!--添加企业弹窗组件-->
		<AddEnterprise ref="addEnterpriseRef" />
    <!--修改企业弹窗组件-->
		<EditEnterprise ref="editEnterpriseRef" />
	</div>
</template>

<script lang="ts">
import { ref, toRefs, reactive, onMounted } from 'vue';
import { ElMessageBox, ElMessage } from 'element-plus';
import AddEnterprise from '/@/views/system/enterprise/component/addEnterprise.vue';
import EditEnterprise from '/@/views/system/enterprise/component/editEnterprise.vue';
import {getPageEnterprises} from "/@/api/enterprise";


export default {
	name: 'systemDept',
	components: { AddEnterprise, EditEnterprise },
	setup() {
		const addEnterpriseRef = ref();
		const editEnterpriseRef = ref();
		const state = reactive({
			tableData: {
				data: [] as Array<any>,
				total: 0,
				loading: false,
				param: {
					pageNum: 0,
					pageSize: 10,
				},
			},
		});

    // 初始化表格数据
		const initTableData = async () => {
      getPageEnterprises({limit:state.tableData.param.pageSize, offset: state.tableData.param.pageNum}).then((res)=>{
        console.log('==res==', res.result_body);
        res.result_body.forEach((item:any, i:any)=> {
          state.tableData.data.push({
            account: item.account,
            full_name: item.full_name,
            abbreviation_name: item.abbreviation_name,
            enterprise_type: item.enterprise_type,
            architecture: item.architecture,
            unified_social_credit_code: item.unified_social_credit_code,
            established_date: item.established_date,
            is_available: item.is_available,
          });
        });
      }).catch(()=>{
        ElMessage.warning('出错啦。。。')
      });


    };

		// 打开新增菜单弹窗
		const onOpenAddDept = () => {
			addEnterpriseRef.value.openDialog();
		};
		// 打开编辑菜单弹窗
		const onOpenEditDept = (row: object) => {
			editEnterpriseRef.value.openDialog(row);
		};
		// 删除当前行
		const onTabelRowDel = (row: object) => {
			ElMessageBox.confirm(`此操作将永久删除部门：${row.deptName}, 是否继续?`, '提示', {
				confirmButtonText: '删除',
				cancelButtonText: '取消',
				type: 'warning',
			})
				.then(() => {
					ElMessage.success('删除成功');
				})
				.catch(() => {});
		};
		// 页面加载时
		onMounted(() => {
			initTableData();
      console.log('==state.tableData.data==', state.tableData.data)
		});






		return {
			addEnterpriseRef,
			editEnterpriseRef,
			onOpenAddDept,
			onOpenEditDept,
			onTabelRowDel,
			...toRefs(state),
		};
	},
};
</script>
