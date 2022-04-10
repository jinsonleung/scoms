<template>
  <div class="universalCode-Airport-container">
    <el-card shadow="hover">
      <!--1.查询框-->
      <div class="query-container">
        <el-row>
          <el-input v-model="queryText" size="small" placeholder="请输入供应商账号/公司名" clearable
                    style="max-width: 360px"></el-input>
          <el-button type="primary" @click="onHandleQuery(queryButtonIndex)" size="small" style="margin-left: 10px">
            <el-icon><elementSearch/></el-icon>查询
          </el-button>
        </el-row>
        <el-button type="primary" @click="onOpenAddDialog">新增</el-button>
      </div>
      <!--2.表单-->
      <el-table :data="tableData.data" stripe row-key="id" style="width: 100%">
        <!--1.1嵌套子表：供应商联系人-->
        <el-table-column type="expand" label="C/E" min-width="20px">
          <template #default="scope">
            <el-table class="child-table" :data="scope.row.contact" stripe style="width: 100%">
              <el-table-column align="center" label="供应商联系方式">
                <el-table-column align="center" show-overflow-tooltip type="index" label="№"
                                 min-width="20px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="department" label="部门"
                                 min-width="40px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="title" label="职位"
                                 min-width="40px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="chn_name" label="中文名"
                                 min-width="40px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="eng_name" label="英文名"
                                 min-width="60px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="tel" label="电话"
                                 min-width="60px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="phone" label="手机"
                                 min-width="60px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="email" label="邮箱"
                                 min-width="100px"></el-table-column>
                <el-table-column align="center" label="操作" show-overflow-tooltip width="180px">
                  <template #header>
                    <el-button-group>
                      <el-tooltip>操作</el-tooltip>
                      <el-button type="primary" style="margin-left:5px; float: right">新建</el-button>
                    </el-button-group>
                  </template>

                  <template #default="scope">
                    <el-button type="text" plain :icon="ZoomIn" title="详情"
                               @click="onOpenDetailDialog(scope.row)"></el-button>
                    <el-button type="text" plain :icon="Edit" title="编辑"
                               @click="onOpenDetailDialog(scope.row)"></el-button>
                    <el-button type="text" plain :icon="Delete" title="删除"
                               @click="onOpenDetailDialog(scope.row)"></el-button>
                  </template>
                </el-table-column>
              </el-table-column>
            </el-table>
          </template>
        </el-table-column>
        <!--1.2主表：供应商信息表-->
        <el-table-column align="center" show-overflow-tooltip type="index" label="№" min-width="20px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="account" label="账号"
                         min-width="80px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="abbreviation_name" label="简称"
                         min-width="120px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="full_name" label="全称"
                         min-width="100px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="established_date" label="成立日期"
                         min-width="80px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="office_address" label="办公地址"
                         min-width="150px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="industry" label="所在行业"
                         min-width="80px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="status_label" label="状态" min-width="80px">
<!--        <el-table-column align="center" show-overflow-tooltip prop="status" label="状态" min-width="80px">-->
          <template #default="scope">
<!--            {{scope.row.get_status_display}}-->
            <el-tag :type="tagType[scope.row.status_label]" size="mini" effect="dark">{{scope.row.status_label}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column align="center" label="操作" show-overflow-tooltip width="80px">
          <template #default="scope">
            <el-button type="text" plain :icon="ZoomIn" title="详情" @click="onOpenDetailDialog(scope.row)"></el-button>
            <el-button type="text" plain :icon="Edit" title="编辑" @click="onOpenEditDialog(scope.row)"></el-button>
            <el-button type="text" plain :icon="Delete" title="删除" @click="onDeleteRow(scope.row)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <!--1.3分页导航栏-->
      <el-pagination
          @size-change="onHandlePageSizeChange"
          @current-change="onHandlePageNumChange"
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
    <!--3.子组件-->
    <SupplierDetail ref="supplierDetailRef"/>
    <EditSupplier ref="editSupplierRef"/>
    <AddSupplier ref="addSupplierRef"/>
  </div>
</template>
<script lang="ts">

import {computed, onMounted, reactive, ref, toRefs} from "vue";
import {getPageSuppliers,queryPageSuppliers, addSupplier} from '/@/api/supplier/index';
import SupplierDetail from '/@/views/supplier/supplierInfo/component/supplierDetail.vue';
import EditSupplier from '/@/views/supplier/supplierInfo/component/editSupplier.vue';
import AddSupplier from '/@/views/supplier/supplierInfo/component/addSupplier.vue';
import {ZoomIn, Edit, Delete,} from '@element-plus/icons-vue';
import {ElMessage, ElMessageBox} from "element-plus";
import {queryAirports} from "/@/api/universalCode";

// 嵌套表参考 https://blog.csdn.net/qq_34310906/article/details/98962682




export default {
  name: 'supplierSupplierInfo',
  components: {SupplierDetail,EditSupplier,AddSupplier,},
  setup() {
    const queryText = ref('');
    const supplierDetailRef = ref();
    const editSupplierRef = ref();
    const addSupplierRef = ref();
    const state = reactive({
      tableData: {
        data: [] as Array<any>,
        total: 0,
        loading: false,
        param: {
          pageNum: 1,
          pageSize: 10,
        },
      },
      childTable: [],
    });

    // 供应商状态el-tag标签类型字典
    const tagType:{[key:string]: string} = {
      "新建": "info",
      "生效": "success",
      "失效": "warning",
      "冻结": "danger",
    };


    //获取分页数据
    const getPageData = async (queryText: any, pageNum: number, pageSize: number) => {
      queryPageSuppliers({queryText, pageNum, pageSize}).then((res: any) => {
        console.log('==res==', res)
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };

    // 页长改变事件
    const onHandlePageSizeChange = (pageSize: number) => {
      state.tableData.param.pageSize = pageSize;
      state.tableData.param.pageNum = 1;
      let pageNum =1;
      getPageData(queryText.value, pageNum, pageSize)
    };

    // 页码改变事件
    const onHandlePageNumChange = (pageNum: number) => {
      state.tableData.param.pageNum = pageNum;
      let pageSize = state.tableData.param.pageSize;
      getPageData(queryText.value, pageNum, pageSize)
    };

    // 查询事件
    const onHandleQuery = () => {
      let pageNum= state.tableData.param.pageNum;
      let pageSize = state.tableData.param.pageSize;
      getPageData(queryText.value.trim(), pageNum, pageSize)
    };

    // 供应商详细情况弹窗
    const onOpenDetailDialog = (row: object) => {
      supplierDetailRef.value.openDialog(row);
    };
    // 编辑供应商情况弹窗
    const onOpenEditDialog = (row: object) => {
      editSupplierRef.value.openDialog(row);
    };

    // 删除当前行
    const onDeleteRow = async (row: any) => {
      ElMessageBox.confirm(`删除账号：${row.account} 的供应商, 是否继续?`, '提示', {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(()=>{
        // return deleteEnterprises({id: row.id});
      }).then((res) => {
        // console.log('==delete res==', res)
        // state.tableData.data = [];
        // initTableData();
        // ElMessage.success('删除成功。');
      })
    };

    const onOpenAddDialog = () => {
      addSupplierRef.value.openDialog();
    }

    const onOpenAddDialog_old = ()=>{
      console.log('==add....==')
      const data = {
        'account': '',
        'full_name': '雅思国际集团公司',
        'status': 0
      };
      addSupplier(data).then((res:any)=>{
        console.log('==addSupplier.res==', res)
      })
    }

    // 钩子函数，获取第1页数据
    onMounted(()=>{
      getPageData(queryText.value, 1, 10)
    });

    return {
      ZoomIn,
      Edit,
      Delete,
      queryText,
      ...toRefs(state),
      supplierDetailRef,
      editSupplierRef,
      addSupplierRef,
      tagType,
      getPageData,
      onHandleQuery,
      onHandlePageSizeChange,
      onHandlePageNumChange,
      onOpenDetailDialog,
      onOpenEditDialog,
      onDeleteRow,
      onOpenAddDialog,
    };
  },
};
</script>
<style lang="scss" scoped>
@import "/@/theme/public/eltable.scss";
.query-container{
  margin-bottom: 10px;
}
:deep(.el-tag--small){
    height: 24px;
    line-height: 22px;
}
</style>