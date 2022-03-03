<template>
  <div class="freightTools-Airport-container">
    <el-card shadow="hover" header="机场代码查询">
        <div class="query-container">
          <!--查询选项（机场代码查询/航司代码查询/国家代码查询）-->
          <el-row style="margin-bottom: 10px">
            <el-button-group style="margin-right: 20px" size="small">
              <el-button type="warning" plain autofocus :class="{active: test==='1'}" @click="onHandleButtonGroupClick(0)">
                <el-icon>
                  <elementPosition/>
                </el-icon>
                机场代码查询
              </el-button>
              <el-button type="warning" plain @click="onHandleButtonGroupClick(1)">
                <el-icon>
                  <elementVan/>
                </el-icon>
                航司代码查询
              </el-button>
              <el-button type="warning" plain @click="onHandleButtonGroupClick(2)">
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
            <el-button type="primary" @click="onHandleQuery(queryButtonIndex)" size="small" style="margin-left: 10px"><el-icon>
                  <elementSearch/>
                </el-icon>查询</el-button>
          </el-row>
        </div>
        <!--查询结果表格数据展示-->
      <!--机场查询列表-->
        <el-table :data="tableData.data" style="width: 100%" v-show="queryButtonIndex===0">
        <el-table-column type="index" label="序号" width="50px"></el-table-column>
				<el-table-column prop="iata_code" label="IATA" sortable></el-table-column>
				<el-table-column prop="icao_code" label="ICAO" sortable></el-table-column>
				<el-table-column prop="chn_name" label="机场名称" sortable></el-table-column>
				<el-table-column prop="country.chn_name" label="国家（地区）" sortable></el-table-column>
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
      <!--航空公司查询列表-->
      <el-table :data="tableData.data" style="width: 100%" v-show="queryButtonIndex===1">
        <el-table-column type="index" label="序号" width="50px"></el-table-column>
				<el-table-column prop="iata_code" label="IATA" sortable></el-table-column>
				<el-table-column prop="icao_code" label="ICAO" sortable></el-table-column>
				<el-table-column prop="eng_name" label="航司名称" sortable></el-table-column>
				<el-table-column prop="country.chn_name" label="国家（地区）" sortable></el-table-column>
				<el-table-column prop="city.chn_name" label="城市" sortable></el-table-column>
        <el-table-column label="操作" show-overflow-tooltip width="140">
          <template #default="scope">
            <el-button
              size="small"
              type="warning"
              @click="onOpenDetailAirline(scope.row)"
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
    <DetailAirline ref="detailAirlineRef" />
  </div>
</template>

<script lang="ts">

import {onMounted, reactive, ref, toRefs} from "vue";
import {queryAirports,queryAirlines} from "/@/api/freightTools";
import DetailAirport from "/@/views/freightTools/airport/component/detailAirport.vue"
import DetailAirline from "/@/views/freightTools/airport/component/detailAirline.vue"

export default {
  name: 'freightToolsAirport',
  components: {DetailAirport,DetailAirline},
  setup() {
    const test = ref('1')
    const queryPlaceholder = ref('');
    const queryButtonIndex = ref(0);
    // const queryTextPlaceHolder = reactive(['输入机场代码/机场名称/国家(地区)/城市','输入航司代码/国家(地区)/城市','输入国家代码']);
    const queryText = ref('');
    const detailAirportRef = ref();
    const detailAirlineRef = ref();
    const state = reactive({
      queryTextPlaceHolder: ['输入机场代码/机场名称/国家(地区)/城市','输入航司代码/国家(地区)/城市','输入国家代码'],
      tableData: {
        data: [] as Array<any>,
        // data: Object,
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
      state.tableData.data = [];   // 清空数据
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

    // 获取查询结果，以分页方式返回
    const getPageAirlines = async (query_text:string, page_num: number, page_size: number)=> {
      queryAirlines({query_text,page_num,page_size}).then((res:any)=>{
        console.log('==airline res==', res)
        state.tableData.data=res.result_data.data;
        state.tableData.total = res.result_data.count;
        console.log("==state.tableData.data==", state.tableData.data)
      })
    };

    // 分类查询按钮单击事件
    const onHandleButtonGroupClick = (index: number) => {
      queryText.value = '';
      queryButtonIndex.value = index;
      queryPlaceholder.value = state.queryTextPlaceHolder[index];
      initTableData();
    };

    // 页长改变事件
		const onHandleSizeChange = (buttonIndex: number, val: number) => {
			state.tableData.param.page_size = val;
      state.tableData.param.page_num = 1;
      if (buttonIndex === 0) {
        getPageAirports(queryText.value,state.tableData.param.page_num,state.tableData.param.page_size);
      } else if (buttonIndex === 1) {
        getPageAirlines(queryText.value,state.tableData.param.page_num,state.tableData.param.page_size);
      }
		};

		// 页码改变事件
		const onHandleCurrentChange = (buttonIndex: number, page_num: number) => {
			state.tableData.param.page_num = page_num;
      const page_size = state.tableData.param.page_size;
      getPageAirports(queryText.value,page_num,page_size);
            if (buttonIndex === 0) {
        getPageAirports(queryText.value,page_num,page_size);
      } else if (buttonIndex === 1) {
        getPageAirlines(queryText.value,page_num,page_size);
      }
		};

    // 查询
		const onHandleQuery = (buttonIndex: number) => {
      console.log('==searching==',buttonIndex, queryText.value);
      initTableData();  // 初始化表格
      let query_text = queryText.value.trim()
      if (query_text != '') {
        if (buttonIndex === 0) {
          getPageAirports(query_text, 1, 10);
        }else if (buttonIndex ===1) {
          getPageAirlines(query_text, 1, 10);
        }else if (buttonIndex ===2 ) {

        }
      }
		};

    // 机场详细情况
    const onOpenDetailAirport = (row: object) => {
      console.log('==open==')
      detailAirportRef.value.openDialog(row);
    };

    // 航空公司详细情况
    const onOpenDetailAirline = (row: object) => {
      detailAirlineRef.value.openDialog(row);
    };
    onMounted(()=>{
      queryPlaceholder.value = state.queryTextPlaceHolder[0];
    })

    return {
      test,
      queryPlaceholder,
      queryButtonIndex,
      queryText,
      detailAirportRef,
      detailAirlineRef,
      // onHandleAirportCodeQuery,
      // onHandleAirlineCodeQuery,
      // onHandleCountryCodeQuery,
      onHandleButtonGroupClick,
      onHandleSizeChange,
      onHandleCurrentChange,
      onOpenDetailAirport,
      onOpenDetailAirline,
      onHandleQuery,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss">
  .active{
    color: red;
    background-color: #1BAEAE;
  }

  	//active {
    //  background: #409EFF;
    //}
    //active:hover {
    //  background: #66b1ff;
    //}

</style>