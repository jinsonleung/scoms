<template>
  <div class="universalCode-Airport-container">
    <el-table :data="tableData.data" stripe row-key="id">


<!--            <el-table-column width="50">-->
<!--              <template #default="scope">-->
<!--                <i class="iconfont icon-crew_feature" @click="toogleExpand(scope.row)"></i>-->
<!--              </template>-->
<!--            </el-table-column>-->
            <el-table-column class="sectable" type="expand" width="100">
              <template #default="scope">
                <el-table :data="scope.row.contact" stripe style="width: 100%">
                  <el-table-column type="index"></el-table-column>
                  <el-table-column prop="department" label="部门"></el-table-column>
                  <el-table-column prop="title" label="职位"></el-table-column>
                  <el-table-column prop="chn_name" label="中文名"></el-table-column>
                  <el-table-column prop="tel" label="电话"></el-table-column>
                </el-table>
              </template>
            </el-table-column>



      <el-table-column align="center" type="index" label="No" min-width="40px"></el-table-column>
      <el-table-column align="center" prop="account" label="账号" min-width="60px"></el-table-column>
      <el-table-column align="center" prop="abbreviation_name" label="简称" min-width="60px"></el-table-column>
      <el-table-column align="center" prop="full_name" label="全称" min-width="80px"></el-table-column>
      <el-table-column align="center" prop="registered_capital" label="注册资本" min-width="80px"></el-table-column>
      <el-table-column align="center" prop="office_address" label="办公地址" min-width="80px"></el-table-column>
      <el-table-column align="center" prop="industry" label="所在行业" min-width="80px"></el-table-column>
    </el-table>
  </div>
</template>
<script lang="ts">

import {onMounted, reactive, toRefs} from "vue";

interface User {
  id: number
  date: string
  name: string
  hasChildren?: boolean
  children?: User[]
}

// 嵌套表参考 https://blog.csdn.net/qq_34310906/article/details/98962682

import {getPageSuppliers} from '/@/api/supplier/index'
import {queryAirlines} from "/@/api/universalCode";

export default {
  name: 'supplierSupplierInfo',
  components: {},
  setup() {
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

    const toogleExpand = (row: any) => {
      let childTable = state.childTable;
      childTable.toggleRowExpansion(row);
      // console.log(this.$route.params.taskId)
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
      ...toRefs(state),
      toogleExpand,
    };
  },
};
</script>
<style lang="scss" scoped>

</style>