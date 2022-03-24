<template>
  <div class="universalCode-Airport-container">
    <el-card shadow="hover">
    <el-table :data="tableData.data" stripe row-key="id" style="width: 100%"
              :cell-style="{padding:'0px'}">
      <!--嵌套子表：供应商联系人-->
      <el-table-column type="expand" label="C/P" min-width="20px">
        <template #default="scope">
          <el-table class="child-table" :data="scope.row.contact" stripe  style="width: 100%">
            <el-table-column align="center" label="供应商联系方式">
              <el-table-column align="center" show-overflow-tooltip type="index" label="№" min-width="20px" ></el-table-column>
              <el-table-column align="center" show-overflow-tooltip prop="department" label="部门" min-width="40px" ></el-table-column>
              <el-table-column align="center" show-overflow-tooltip prop="title" label="职位" min-width="40px"></el-table-column>
              <el-table-column align="center" show-overflow-tooltip prop="chn_name" label="中文名" min-width="40px"></el-table-column>
              <el-table-column align="center" show-overflow-tooltip prop="eng_name" label="英文名" min-width="60px"></el-table-column>
              <el-table-column align="center" show-overflow-tooltip prop="tel" label="电话" min-width="60px"></el-table-column>
              <el-table-column align="center" show-overflow-tooltip prop="phone" label="手机" min-width="60px"></el-table-column>
              <el-table-column align="center" show-overflow-tooltip prop="email" label="邮箱" min-width="100px"></el-table-column>
              <el-table-column align="center" label="操作" show-overflow-tooltip width="180px">
                <template #header >
                  <el-button-group>
                    <el-tooltip>操作</el-tooltip>
                    <el-button type="primary" style="margin-left:5px; float: right">新建</el-button>
                  </el-button-group>
                </template>

                <template #default="scope">
                  <el-button type="text" plain :icon="ZoomIn" title="详情" @click="onOpenDetailDialog(scope.row)"></el-button>
                  <el-button type="text" plain :icon="Edit" title="编辑" @click="onOpenDetailDialog(scope.row)"></el-button>
                  <el-button type="text" plain :icon="Delete" title="删除" @click="onOpenDetailDialog(scope.row)"></el-button>
                </template>
              </el-table-column>
            </el-table-column>
          </el-table>
        </template>
      </el-table-column>

      <!--主表：供应商信息表-->
      <el-table-column align="center" show-overflow-tooltip type="index" label="№" min-width="20px"></el-table-column>
      <el-table-column align="center" show-overflow-tooltip prop="account" label="账号"
                       min-width="60px"></el-table-column>
      <el-table-column align="center" show-overflow-tooltip prop="abbreviation_name" label="简称"
                       min-width="60px"></el-table-column>
      <el-table-column align="center" show-overflow-tooltip prop="full_name" label="全称"
                       min-width="100px"></el-table-column>
      <el-table-column align="center" show-overflow-tooltip prop="established_date" label="成立日期"
                       min-width="80px"></el-table-column>
      <el-table-column align="center" show-overflow-tooltip prop="office_address" label="办公地址"
                       min-width="150px"></el-table-column>
      <el-table-column align="center" show-overflow-tooltip prop="industry" label="所在行业"
                       min-width="80px"></el-table-column>
      <el-table-column align="center" show-overflow-tooltip prop="business_scope" label="经营范围"
                       min-width="80px"></el-table-column>
      <el-table-column align="center" show-overflow-tooltip prop="is_available" label="是否启用"
                       min-width="80px"></el-table-column>
      <el-table-column align="center" label="操作" show-overflow-tooltip width="100px">
        <template #default="scope">
          <el-button type="text" plain :icon="ZoomIn" title="详情" @click="onOpenDetailDialog(scope.row)"></el-button>
          <el-button type="text" plain :icon="Edit" title="编辑" @click="onOpenEditDialog(scope.row)"></el-button>
          <el-button type="text" plain :icon="Delete" title="删除" @click="onDeleteRow(scope.row)"></el-button>
        </template>
      </el-table-column>
    </el-table>
    </el-card>
    <SupplierDetail ref="supplierDetailRef"/>
    <SupplierEdit ref="supplierEditRef"/>
  </div>
</template>
<script lang="ts">

import {onMounted, reactive, ref, toRefs} from "vue";
import {getPageSuppliers} from '/@/api/supplier/index';
import SupplierDetail from '/@/views/supplier/supplierInfo/component/supplierDetail.vue';
import SupplierEdit from '/@/views/supplier/supplierInfo/component/suppliverEdit.vue';
import {ZoomIn, Edit, Delete,} from '@element-plus/icons-vue';
import {ElMessage, ElMessageBox} from "element-plus";
import {deleteEnterprises} from "/@/api/enterprise";
// 嵌套表参考 https://blog.csdn.net/qq_34310906/article/details/98962682

export default {
  name: 'supplierSupplierInfo',
  components: {SupplierDetail,SupplierEdit,},
  setup() {
    const supplierDetailRef = ref();
    const supplierEditRef = ref();
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

    // 供应商详细情况弹窗
    const onOpenDetailDialog = (row: object) => {
      supplierDetailRef.value.openDialog(row);
    };
    // 编辑供应商情况弹窗
    const onOpenEditDialog = (row: object) => {
      supplierEditRef.value.openDialog(row);
    };
    // 删除供应商弹窗
    const onOpenDeleteDialog = (row: object) => {
      // airlineDetailailRef.value.openDialog(row);
    };

        // 删除当前行
    const onDeleteRow = async (row: any) => {
      ElMessageBox.confirm(`删除账号：${row.account} 的供应商记录, 是否继续?`, '提示', {
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


    onMounted(()=>{
      let pageNum = 1;
      let pageSize = 10;
      getPageSuppliers({pageNum, pageSize}).then((res: any) => {
        console.log('==res==', res)
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    });

    return {
      ZoomIn,
      Edit,
      Delete,
      ...toRefs(state),
      supplierDetailRef,
      supplierEditRef,
      onOpenDetailDialog,
      onOpenEditDialog,
      onDeleteRow,
    };
  },
};
</script>
<style lang="scss" scoped>
@import "/@/theme/public/eltable.scss";
</style>