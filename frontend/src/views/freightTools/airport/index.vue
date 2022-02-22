<template>
  <div class="freightTools-Airport-container">
    <el-card shadow="hover" header="机场代码查询">
        <div class="query-container">
          <!--查询选项（机场代码查询/航司代码查询/国家代码查询）-->
          <el-row style="margin-bottom: 10px">
            <el-button-group style="margin-right: 20px" size="small">
              <el-button type="warning" plain autofocus :class="{active: test==='1'}" @click="onHandleAirportCodeQuery">
                <el-icon>
                  <elementPosition/>
                </el-icon>
                机场代码查询
              </el-button>
              <el-button type="warning" plain @click="onHandleAirlineCodeQuery">
                <el-icon>
                  <elementVan/>
                </el-icon>
                航司代码查询
              </el-button>
              <el-button type="warning" plain @click="onHandleCountryCodeQuery">
                <el-icon>
                  <elementLocation/>
                </el-icon>
                国家代码查询
              </el-button>
            </el-button-group>
          </el-row>
          <!--查询条件-->
          <el-row>
            <el-input v-model="queryText" size="small" :placeholder=queryPlaceholder clearable
                      style="max-width: 360px"></el-input>
            <el-button type="primary" @click="onQueryAirports" size="small" style="margin-left: 10px"><el-icon>
                  <elementSearch/>
                </el-icon>查询</el-button>
          </el-row>
        </div>
        <!--查询结果表格数据展示-->
        <el-table :data="tableData.data" style="width: 100%" v-show="queryButtonIndex===0">
        <el-table-column type="index" label="序号" width="50px"></el-table-column>
				<el-table-column prop="iata_code" label="IATA" sortable></el-table-column>
				<el-table-column prop="icao_code" label="ICAO" sortable></el-table-column>
				<el-table-column prop="airport_chn_name" label="机场名称" sortable></el-table-column>
				<el-table-column prop="country_chn_name" label="国家（地区）" sortable></el-table-column>
				<el-table-column prop="city_chn_name" label="城市" sortable></el-table-column>
        <el-table-column label="操作" show-overflow-tooltip width="140">
          <template #default="scope">
            <el-button
              size="small"
              type="warning"
              @click="onOpenDetailAirport(scope.row)"
              >详情</el-button
            >
          </template>
        </el-table-column>
			</el-table>

      <el-table :data="tableData.data" style="width: 100%" v-show="queryButtonIndex===1">
        <el-table-column type="index" label="序号" width="50px"></el-table-column>
				<el-table-column prop="iata_code" label="航司代码" sortable></el-table-column>
				<el-table-column prop="icao_code" label="航司名称" sortable></el-table-column>
				<el-table-column prop="airport_chn_name" label="机场名称" sortable></el-table-column>
				<el-table-column prop="country_chn_name" label="国家（地区）" sortable></el-table-column>
				<el-table-column prop="city_chn_name" label="城市" sortable></el-table-column>
        <el-table-column label="操作" show-overflow-tooltip width="140">
          <template #default="scope">
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
    const test = ref('1')
    const queryPlaceholder = ref('')
    const queryButtonIndex = ref(0)
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
    };

    // 获取查询结果，以分页方式返回
    const getPageAirports = async (query_text:string, page_num: number, page_size: number)=> {
      queryAirports({query_text,page_num,page_size}).then((res:any)=>{
        state.tableData.data=res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };

    // 机场代码查询
    const onHandleAirportCodeQuery = (row: object) => {
      queryButtonIndex.value=0;
      queryPlaceholder.value = '输入机场代码/机场名称/国家(地区)/城市';

      console.log('==onHandleAirportCodeQuery==')

    };
    // 航司代码查询
    const onHandleAirlineCodeQuery = (row: object) => {
      queryButtonIndex.value=1;
      queryPlaceholder.value = '输入航司代码/国家(地区)/城市';
      console.log('==onHandleAirlineCodeQuery==')

    };
    // 国家代码查询
    const onHandleCountryCodeQuery = (row: object) => {
      queryButtonIndex.value=2;
      queryPlaceholder.value = '输入国家代码';
      console.log('==onHandleCountryCodeQuery==')

    };


    // 页长改变事件
		const onHandleSizeChange = (val: number) => {
			state.tableData.param.page_size = val;
      state.tableData.param.page_num = 1;
      getPageAirports(queryText.value,state.tableData.param.page_num,state.tableData.param.page_size);
		};

		// 页码改变事件
		const onHandleCurrentChange = (val: number) => {
			state.tableData.param.page_num = val;
      getPageAirports(queryText.value,state.tableData.param.page_num,state.tableData.param.page_size);
		};

    // 查询
		const onQueryAirports = () => {
      console.log('==airport11 search==', 'searching...',queryText.value);
      initTableData();
      let query_text = queryText.value.trim()
      if (query_text != '') getPageAirports(queryText.value,1,10);
		};

    // 机场详细情况
    const onOpenDetailAirport = (row: object) => {
      console.log('==open==')
      detailAirportRef.value.openDialog(row);
    };

    return {
      test,
      queryPlaceholder,
      queryButtonIndex,
      queryText,
      detailAirportRef,
      onHandleAirportCodeQuery,
      onHandleAirlineCodeQuery,
      onHandleCountryCodeQuery,
      onHandleSizeChange,
      onHandleCurrentChange,
      onOpenDetailAirport,
      onQueryAirports,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss">
  active{
    color: red;
    background-color: #1BAEAE;
  }
</style>