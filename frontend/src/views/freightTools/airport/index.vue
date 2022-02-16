<template>
  <div class="freightTools-Airport-container">
    <el-card shadow="hover" header="机场代码查询">
      <el-input v-model="queryText" size="small" placeholder="输入机场代码/机场名称/国家(地区)/城市" clearable style="max-width: 280px"> </el-input>
      <el-button type="primary" @click="onQueryAirports" size="small">查询</el-button>
      <el-table :data="tableData.data" style="width: 100%">
        <el-table-column type="index" label="序号" width="50px"></el-table-column>
				<el-table-column prop="iata_code" label="IATA" sortable></el-table-column>
				<el-table-column prop="icao_code" label="ICAO" sortable></el-table-column>
				<el-table-column prop="airport_chn_name" label="机场名称" sortable></el-table-column>
				<el-table-column prop="country_chn_name" label="国家（地区）" sortable></el-table-column>
				<el-table-column prop="city_chn_name" label="城市" sortable></el-table-column>
        <el-table-column label="操作" show-overflow-tooltip width="140">
          <template #default="scope">
            <el-button size="mini" type="text" @click="onOpenDetailAirport(scope.row)">详细</el-button>
            <el-button
              size="small"
              type="warning"
              @click="onOpenDetailAirport(scope.row)"
              >详情</el-button
            >
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
    <!--机场详情弹窗-->
    <DetailAirport ref="detailAirportRef" />
  </div>
</template>

<script lang="ts">

import {reactive, ref, toRefs} from "vue";
import {queryAirports} from "/@/api/freightTools";
import DetailAirport from "/@/views/freightTools/airport/component/detailAirport.vue"

export default {
  name: 'freightToolsAirport',
  components: {DetailAirport},
  setup() {
    const queryText = ref('');
    const detailAirportRef = ref();
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

    // 初始化表格
    const initTableData = async () => {
      state.tableData.data = [];
      state.tableData.param.page_num = 1;
      state.tableData.param.page_size = 10;
    }

    // 获取查询结果，以分页方式返回
    const getPageAirports = async (query_text:string, page_num: number, page_size: number)=> {
      queryAirports({query_text,page_num,page_size}).then((res:any)=>{
        state.tableData.data=res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    }

    // 分长改变
		const onHandleSizeChange = (val: number) => {
			state.tableData.param.page_size = val;
      state.tableData.param.page_num = 1;
      queryAirports({queryText: queryText.value, page_num:state.tableData.param.page_num, page_size:state.tableData.param.page_size});
		};

		// 分页改变
		const onHandleCurrentChange = (val: number) => {
			state.tableData.param.page_num = val;
      getPageAirports(queryText.value,state.tableData.param.page_num,state.tableData.param.page_size);
		};

    // 查询
		const onQueryAirports = () => {
      console.log('==airport search==', 'searching...',queryText.value);
      initTableData();
      let query_text = queryText.value.trim()
      if (query_text != '') getPageAirports(queryText.value,1,10);
		};

    // 机场详细情况
    const onOpenDetailAirport = (row: object) => {
      console.log('==open==')
      detailAirportRef.value.openDialog(row);
    }

    return {
      queryText,
      detailAirportRef,
      onHandleSizeChange,
      onHandleCurrentChange,
      onOpenDetailAirport,
      onQueryAirports,
      ...toRefs(state),
    };
  },
};
</script>