<template>
  <div class="system-dept-container">
    <el-card shadow="hover">
      <!--查询栏-->
      <div class="system-dept-search mb15">
        <el-input v-model="queryText" size="small" placeholder="请输入企业名称" style="max-width: 180px"></el-input>
        <el-button size="small" type="primary" class="ml10" @click="onSearchEnterprise">
          <el-icon>
            <elementSearch/>
          </el-icon>
          查询
        </el-button>
        <el-button size="small" type="success" class="ml10" @click="onOpenAddEnterprise">
          <el-icon>
            <elementFolderAdd/>
          </el-icon>
          新增企业
        </el-button>
      </div>
      <!--数据列表栏-->
      <el-table
          :data="tableData.data"
          :header-row-style="{height:'30px'}"
          :header-cell-style="{padding:0}"
          :row-style="{height:'30px'}"
          :cell-style="{padding:'0'}"
          style="width: 100%; font-size: 10px"
          row-key="id"
      >
        <el-table-column type="index" label="序号" show-overflow-tooltip fixed sortable
                         width="50px"></el-table-column>
        <el-table-column prop="account" label="企业账号" show-overflow-tooltip fixed sortable
                         width="100px"></el-table-column>
        <el-table-column prop="full_name" label="企业名全称" show-overflow-tooltip sortable width="200px"></el-table-column>
        <el-table-column prop="abbreviation_name" label="企业名简称" show-overflow-tooltip sortable
                         width="120px"></el-table-column>
        <el-table-column prop="enterprise_type" label="企业类型" show-overflow-tooltip width="120px"></el-table-column>
        <el-table-column prop="architecture" label="体系结构" show-overflow-tooltip width="80px"></el-table-column>
        <el-table-column prop="unified_social_credit_code" label="社会信用代码" show-overflow-tooltip
                         width="180px"></el-table-column>
        <el-table-column prop="established_date" label="成立日期" show-overflow-tooltip width="120px"></el-table-column>
        <el-table-column prop="status" label="企业状态" show-overflow-tooltip width="80px">
          <template #default="scope">
            <el-tag size="small" type="success"  v-if="scope.row.is_available">启用</el-tag>
            <el-tag size="small" type="info"  v-else>禁用</el-tag>
          </template>
        </el-table-column>

        <el-table-column label="操作" show-overflow-tooltip width="140">
          <template #default="scope">
            <el-button size="mini" type="text" @click="onOpenAddEnterprise(scope.row)">新增</el-button>
            <el-button size="mini" type="text" @click="onOpenEditEnterprise(scope.row)">修改</el-button>
            <el-button size="mini" type="text" @click="onTableRowDel(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <!--分页导航栏-->
      <el-pagination
          @size-change="onHandleSizeChange"
          @current-change="onHandleCurrentChange"
          class="mt15"
          :pager-count="5"
          :page-sizes="[10, 20, 30]"
          v-model:current-page="tableData.param.page_num"
          background
          v-model:page-size="tableData.param.page_size"
          layout="total, sizes, prev, pager, next, jumper"
          :total="tableData.total"
      >
      </el-pagination>
    </el-card>
    <!--添加企业弹窗组件-->
    <AddEnterprise ref="addEnterpriseRef"/>
    <!--修改企业弹窗组件-->
    <EditEnterprise ref="editEnterpriseRef" />
  </div>
</template>

<script lang="ts">
import {ref, toRefs, reactive, onMounted} from 'vue';
import {ElMessageBox, ElMessage} from 'element-plus';
import AddEnterprise from '/@/views/system/enterprise/component/addEnterprise.vue';
import EditEnterprise from '/@/views/system/enterprise/component/editEnterprise.vue';
import {getPageEnterprises, deleteEnterprises} from "/@/api/enterprise";
import moment from "moment";
import {
  enterpriseTypeOptions,
  enterpriseArchitectureOptions,
  industryOptions,
  getOptionsLabel
} from '/@/views/system/enterprise/enterpriseOptions';



export default {
  name: 'systemDept',
  components: {AddEnterprise, EditEnterprise},
  setup() {
    const queryText = ref('');
    const addEnterpriseRef = ref();
    const editEnterpriseRef = ref();
    const state = reactive({
      tableData: {
        data: [] as Array<any>,
        total: 0,
        loading: false,
        param: {
          page_num: 1,
          page_size: 10,
        },
      },
    });

    // 获取分页数据
    const getTablePageData = async (page_num: number, page_size: number) => {
      getPageEnterprises({
        page_num: page_num,
        page_size: page_size
      }).then((res: any) => {
        console.log('==getTablePageData==', res)
        const data: Array<object> = [];
        res.result_data.forEach((item: any) => {
          data.push({
            id: item.id,
            superior_level: item.superior_level,
            account: item.account,
            full_name: item.full_name,
            abbreviation_name: item.abbreviation_name,
            enterprise_type: getOptionsLabel(enterpriseTypeOptions, item.enterprise_type),
            architecture: getOptionsLabel(enterpriseArchitectureOptions, item.architecture),
            unified_social_credit_code: item.unified_social_credit_code,
            registered_capital: item.registered_capital,
            established_date: moment(item.established_date).format('YYYY-MM-DD'),
            effective_start_date: item.effective_start_date,
            effective_end_date: item.effective_end_date,
            address: item.address,
            city: item.city,
            industry: item.industry,
            website: item.website,
            legal_person_name: item.legal_person_name,
            legal_person_email: item.legal_person_email,
            contact_name: item.contact_name,
            contact_tel: item.contact_tel,
            contact_phone: item.contact_phone,
            contact_email: item.contact_email,
            business_scope: item.business_scope,
            remark: item.remark,
            is_available: item.is_available,
          });
        });
        state.tableData.data = data;
        state.tableData.total = res.result_data.count;
      });
    }

    // 初始化表格数据
    const initTableData = () => {
      getTablePageData(state.tableData.param.page_num,state.tableData.param.page_size);
    };

    // 查找
    const onSearchEnterprise = (params:object) => {

    };

    // 打开新增菜单弹窗
    const onOpenAddEnterprise = () => {
      addEnterpriseRef.value.openDialog();
    };
    // 打开编辑菜单弹窗
    const onOpenEditEnterprise = (row: object) => {
      editEnterpriseRef.value.openDialog(row);
    };
    // 删除当前行
    const onTableRowDel = async (row: any) => {
      ElMessageBox.confirm(`删除账号：${row.account} 的企业记录, 是否继续?`, '提示', {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(()=>{
        return deleteEnterprises({id: row.id});
      }).then((res) => {
        console.log('==delete res==', res)
        state.tableData.data = [];
        initTableData();
        ElMessage.success('删除成功。');
      })
    };

		// 页长改变
		const onHandleSizeChange = (val: number) => {
			state.tableData.param.page_size = val;
      state.tableData.param.page_num = 1;
      getTablePageData(state.tableData.param.page_num,state.tableData.param.page_size)
		};
		// 页码改变
		const onHandleCurrentChange = (val: number) => {
			state.tableData.param.page_num = val;
      getTablePageData(state.tableData.param.page_num,state.tableData.param.page_size)
		};
    // 页面加载时
    onMounted(() => {
      initTableData();
      // console.log('==state.tableData.data==', state.tableData.data)
    });


    return {
      queryText,
      enterpriseTypeOptions,
      enterpriseArchitectureOptions,
      industryOptions,
      addEnterpriseRef,
      editEnterpriseRef,
      onSearchEnterprise,
      onOpenAddEnterprise,
      onOpenEditEnterprise,
      onHandleSizeChange,
      onHandleCurrentChange,
      onTableRowDel,
      ...toRefs(state),
    };
  },
};
</script>
