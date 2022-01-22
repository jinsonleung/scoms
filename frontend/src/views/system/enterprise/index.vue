<template>
  <div class="system-dept-container">
    <el-card shadow="hover">
      <!--查询栏-->
      <div class="system-dept-search mb15">
        <el-input size="small" placeholder="请输入企业名称" style="max-width: 180px"></el-input>
        <el-button size="small" type="primary" class="ml10">
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
          style="width: 100%"
          row-key="id"
      >
        <el-table-column prop="account" label="企业账号" show-overflow-tooltip fixed sortable
                         width="100px"></el-table-column>
        <el-table-column prop="fullName" label="企业名全称" show-overflow-tooltip sortable width="200px"></el-table-column>
        <el-table-column prop="abbreviationName" label="企业名简称" show-overflow-tooltip sortable
                         width="120px"></el-table-column>
        <el-table-column prop="enterpriseType" label="企业类型" show-overflow-tooltip width="120px"></el-table-column>
        <el-table-column prop="architecture" label="体系结构" show-overflow-tooltip width="80px"></el-table-column>
        <el-table-column prop="unifiedSocialCreditCode" label="社会信用代码" show-overflow-tooltip
                         width="180px"></el-table-column>
        <el-table-column prop="establishedDate" label="成立日期" show-overflow-tooltip width="120px"></el-table-column>
        <el-table-column prop="status" label="企业状态" show-overflow-tooltip width="80px">
          <template #default="scope">
            <el-tag type="success" size="small" v-if="scope.row.isAvailable">启用</el-tag>
            <el-tag type="info" size="small" v-else>禁用</el-tag>
          </template>
        </el-table-column>

        <el-table-column label="操作" show-overflow-tooltip width="140">
          <template #default="scope">
            <el-button size="mini" type="text" @click="onOpenAddEnterprise(scope.row)">新增</el-button>
            <el-button size="mini" type="text" @click="onOpenEditEnterprise(scope.row)">修改</el-button>
            <el-button size="mini" type="text" @click="onTabelRowDel(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
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
      getPageEnterprises({limit: state.tableData.param.pageSize, offset: state.tableData.param.pageNum}).then((res) => {
        console.log('==res==', res.result_body);
        res.result_body.forEach((item: any, i: any) => {
          state.tableData.data.push({
            id: item.id,
            enterpriseLevel: item.enterprise_level,
            account: item.account,
            fullName: item.full_name,
            abbreviationName: item.abbreviation_name,
            enterpriseType: getOptionsLabel(enterpriseTypeOptions,item.enterprise_type),
            architecture: getOptionsLabel(enterpriseArchitectureOptions,item.architecture),
            unifiedSocialCreditCode: item.unified_social_credit_code,
            registeredCapital: item.registered_capital,
            establishedDate: moment(item.established_date).format('YYYY-MM-DD'),
            effectiveStartDate: item.effective_start_date,
            effectiveEndDate: item.effective_end_date,
            address: item.address,
            city: item.city,
            industry: item.industry,
            website: item.website,
            legalPersonName: item.legal_person_name,
            legalPersonEmail: item.legal_person_email,
            contactName: item.contact_name,
            contactTel: item.contact_tel,
            contactPhone: item.contact_phone,
            contactEmail: item.contact_email,
            businessScope: item.business_scope,
            remark: item.remark,
            isAvailable: item.is_available,
          });
        });
      }).catch(() => {
        ElMessage.warning('出错啦。。。')
      });
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
    const onTabelRowDel = async (row: object) => {
      const account = row.account;
      ElMessageBox.confirm(`删除账号：${account} 的企业记录, 是否继续?`, '提示', {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(() => {
            deleteEnterprises({id: account}).then((res: any) => {
              if (res.result_code === 200) {
                console.log('delete res', res)
                // 刷新表单
                state.tableData.data = [];
                initTableData();
                ElMessage.success('删除成功。');
              } else {
                ElMessage.success('删除失败！');
              }
            }).catch(() => {
              ElMessage.success('删除失败！');
            });
          })
    };
    // 页面加载时
    onMounted(() => {
      initTableData();
      console.log('==state.tableData.data==', state.tableData.data)
    });


    return {
      enterpriseTypeOptions,
      enterpriseArchitectureOptions,
      industryOptions,
      addEnterpriseRef,
      editEnterpriseRef,
      onOpenAddEnterprise,
      onOpenEditEnterprise,
      onTabelRowDel,
      ...toRefs(state),
    };
  },
};
</script>
