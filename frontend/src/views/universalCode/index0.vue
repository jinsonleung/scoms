<template>
  <div class="universalCode-Airport-container">
    <el-card shadow="hover" header="机场代码查询">
      <div class="query-container">
        <!--查询选项（机场代码查询/航司代码查询/国家代码查询）-->
        <el-row style="margin-bottom: 10px">
          <el-radio-group v-model="tabPosition" size="small" type="warning" fill="orange"
                          @change="onHandleRadioGroupChange">
            <el-radio-button label=0>
              <el-icon>
                <elementLocationInformation/>
              </el-icon>
              机场代码查询
            </el-radio-button>
            <el-radio-button label=1>
              <el-icon>
                <elementPromotion/>
              </el-icon>
              航司代码查询
            </el-radio-button>
            <el-radio-button label=2>
              <el-icon>
                <elementFlag/>
              </el-icon>
              国家代码查询
            </el-radio-button>
          </el-radio-group>
        </el-row>
        <!--查询条件-->
        <el-row>
          <el-input v-model="queryText" size="small" :placeholder=queryPlaceholder clearable
                    style="max-width: 360px"></el-input>
          <el-button type="primary" @click="onHandleQuery(queryButtonIndex)" size="small" style="margin-left: 10px">
            <el-icon>
              <elementSearch/>
            </el-icon>
            查询
          </el-button>
        </el-row>
      </div>
      <!--查询结果表格数据展示-->
      <el-divider></el-divider>
      <!--机场代码查询列表-->
      <div v-if="isShow==0">
        <el-table :data="tableData.data" style="width:100%">
          <el-table-column type="index" label="No" min-width="40px"></el-table-column>
          <el-table-column prop="iata_code" label="IATA" min-width="60px"></el-table-column>
          <el-table-column prop="icao_code" label="ICAO" min-width="60px"></el-table-column>
          <el-table-column prop="chn_name" label="机场名称" min-width="120">
            <template #default="scope">
              {{ scope.row.chn_name }}<br/>{{ scope.row.eng_name }}
            </template>
          </el-table-column>
          <el-table-column prop="country.chn_name" label="国家/地区" min-width="120">
            <template #default="scope" >
              <country-flag :country='scope.row.country.iso2_code' size='small'/> {{scope.row.country.chn_name}}
              <br/>{{scope.row.country.eng_name}}
            </template>
          </el-table-column>
          <el-table-column prop="city_chn_name" label="城市名称" min-width="120">
            <template #default="scope">
              {{ scope.row.city_chn_name }}<br/>{{ scope.row.city_eng_name }}
            </template>
          </el-table-column>
          <el-table-column label="操作" show-overflow-tooltip width="140">
            <template #default="scope">
              <el-button
                  size="small"
                  type="warning"
                  @click="onOpenDetailDialog(scope.row)"
              >详情
              </el-button
              >
            </template>
          </el-table-column>
        </el-table>
        <!--分页导航栏-->
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
      </div>
      <!--航司代码查询列表-->
      <div v-else-if="isShow==1">
        <el-table :data="tableData.data" style="width:100%">
          <el-table-column type="index" label="No" min-width="40px"></el-table-column>
          <el-table-column prop="iata_code" label="IATA" min-width="60px"></el-table-column>
          <el-table-column prop="icao_code" label="ICAO" min-width="60px"></el-table-column>
          <el-table-column prop="airline_prefix_code" label="前缀代码" min-width="80px"></el-table-column>
          <el-table-column prop="chn_name" label="航司名称" min-width="140">
            <template #default="scope" >
            <!--如果航司Logo不存在，则使用默认Logo取代-->
              <img :src="getAssetsFile('images/airlinesLogo/_default1.png')" v-realimage="getAssetsFile(`images/airlinesLogo/${scope.row.iata_code}.png`)" style="width: 20px; height: 20px; " /> {{scope.row.chn_name}}<br/>{{scope.row.eng_name}}
            </template>
          </el-table-column>
          <el-table-column prop="country.chn_name" label="国家/地区" min-width="100">
            <template #default="scope" >
              <country-flag :country='scope.row.country_iso2_code' size='small'/> {{scope.row.country.chn_name}}<br/>{{scope.row.country.eng_name}}
            </template>
          </el-table-column>
          <el-table-column label="操作" show-overflow-tooltip width="120">
            <template #default="scope">
              <el-button
                  size="small"
                  type="warning"
                  @click="onOpenDetailDialog(scope.row)"
              >详情
              </el-button
              >
            </template>
          </el-table-column>
        </el-table>
        <!--分页导航栏-->
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
      </div>
      <!--国家代码查询列表-->
      <div v-else-if="isShow==2">
        <el-table :data="tableData.data" style="width:100%">
          <el-table-column type="index" label="No" min-width="40px"></el-table-column>
          <el-table-column prop="iso2_code" label="ISO2" min-width="60px"></el-table-column>
          <el-table-column prop="iso3_code" label="ISO3" min-width="60px"></el-table-column>
          <el-table-column prop="chn_name" label="国家名称" min-width="120px">
            <template #default="scope" >
              <country-flag :country='scope.row.iso2_code' size='small'/> {{scope.row.chn_name}}<br/>{{scope.row.full_eng_name}}
            </template>
          </el-table-column>
          <el-table-column prop="continent.chn_name" label="洲名" min-width="80">
            <template #default="scope">
              {{ scope.row.continent.chn_name }}<br/>{{ scope.row.continent.eng_name }}
            </template>
          </el-table-column>
          <el-table-column label="操作" show-overflow-tooltip width="120">
            <template #default="scope">
              <el-button
                  size="small"
                  type="warning"
                  @click="onOpenDetailDialog(scope.row)"
              >详情
              </el-button
              >
            </template>
          </el-table-column>
        </el-table>
        <!--分页导航栏-->
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
      </div>

    </el-card>
    <!--机场详情弹窗-->
    <DetailAirport ref="detailAirportRef"/>
    <!--航司详情弹窗-->
    <DetailAirline ref="detailAirlineRef"/>
  </div>
</template>

<script lang="ts">

import { onMounted, reactive, ref, toRefs} from "vue";
import {queryAirports, queryAirlines, queryCountries} from "/@/api/universalCode";
import DetailAirport from "/@/views/universalCode/component/airportDetail.vue";
import DetailAirline from "/@/views/universalCode/component/airlineDetail.vue";
import CountryFlag from "vue-country-flag-next";
import commonFunction from "/@/utils/commonFunction";

export default {
  name: 'freightToolsAirport',
  components: {DetailAirport, DetailAirline,CountryFlag},
  setup() {
    const isShow = ref(0);
    const tabPosition = ref(0);
    const queryLabels = ref([{icon: 'elementPosition', label: '机场代码查询'}, {
      icon: 'elementVan',
      label: '航司代码查询'
    }, {icon: 'elementPosition', label: '国家代码查询'}, {icon: 'elementPosition', label: '其他查询'},]);
    const queryButtonIndex = ref(0);
    const queryPlaceholder = ref('');
    // const queryTextPlaceHolder = reactive(['输入机场代码/机场名称/国家(地区)/城市','输入航司代码/国家(地区)/城市','输入国家代码']);
    const queryText = ref('');
    const detailAirportRef = ref();
    const detailAirlineRef = ref();
    const { getAssetsFile } = commonFunction();
    const state = reactive({
      queryTextPlaceHolder: ['输入机场代码/机场名称/国家(地区)/城市', '输入航司代码/国家(地区)/城市', '输入国家代码'],
      tableData: {
        data: [] as Array<any>,
        total: 0,
        loading: false,
        param: {
          page_num: 1,
          page_size: 10,
        },
      },
      tableHeader: [] as Array<any>,
      tableHeaders: [
        [
          {prop: 'iata_code', label: 'IATA'},
          {prop: 'icao_code', label: 'ICAO'},
          {prop: 'chn_name', label: '机场名称'},
          {prop: 'country.chn_name', label: '国家（地区）'},
          {prop: 'city_chn_name', label: '城市'},
        ],
        [
          {prop: 'iata_code', label: 'IATA'},
          {prop: 'icao_code', label: 'ICAO'},
          {prop: 'chn_name', label: '航司名称'},
          {prop: 'country.chn_name', label: '国家（地区）'},
          {prop: 'city.chn_name', label: '城市'},
        ]
      ],
    });

    // 初始化表格
    const initTableData = async () => {
      queryText.value = '';
      state.tableData.data = [];   // 清空数据
      state.tableData.param.page_num = 1;
      state.tableData.param.page_size = 10;
      state.tableData.total = 0;
    };

    // 获取机场查询结果，以分页方式返回
    const getPageAirports = async (query_text: string, page_num: number, page_size: number) => {
      queryAirports({query_text, page_num, page_size}).then((res: any) => {
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };

    // 获取航司查询结果，以分页方式返回
    const getPageAirlines = async (query_text: string, page_num: number, page_size: number) => {
      queryAirlines({query_text, page_num, page_size}).then((res: any) => {
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };

    // 获取国家查询结果，以分页方式返回
    const getPageCountries = async (query_text: string, page_num: number, page_size: number) => {
      queryCountries({query_text, page_num, page_size}).then((res: any) => {
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };

    // 分类查询按钮单击事件
    const onHandleRadioGroupChange = (index: number) => {
      // console.log('==onHandleRadioGroupChange.index==', index)
      isShow.value = index;
      queryButtonIndex.value = index;
      queryPlaceholder.value = state.queryTextPlaceHolder[index];
      initTableData();
    };

    // 页长改变事件
    const onHandlePageSizeChange = (page_size: number) => {
      state.tableData.param.page_size = page_size;
      state.tableData.param.page_num = 1;
      let idx = Number(queryButtonIndex.value);
      if (idx === 0) {
        getPageAirports(queryText.value, 1, page_size);
      } else if (idx === 1) {
        getPageAirlines(queryText.value, 1, page_size);
      } else if (idx === 2) {
        getPageCountries(queryText.value, 1, page_size);
      }

    };

    // 页码改变事件
    const onHandlePageNumChange = (page_num: number) => {
      state.tableData.param.page_num = page_num;
      let page_size = state.tableData.param.page_size;
      let idx = Number(queryButtonIndex.value);
      if (idx === 0) {
        getPageAirports(queryText.value, page_num, page_size);
      } else if (idx === 1) {
        getPageAirlines(queryText.value, page_num, page_size);
      }else if (idx === 2) {
        getPageCountries(queryText.value, page_num, page_size);
      }
    };

    // 查询
    const onHandleQuery = (idx: number) => {
      let query_text = queryText.value.trim()
      if (query_text === '') return;
      idx = Number(idx);
      if (idx === 0) {
        getPageAirports(query_text, 1, 10);
      } else if (idx === 1) {
        getPageAirlines(query_text, 1, 10);
      } else {
        getPageCountries(query_text, 1, 10);
      }
      state.tableHeader = state.tableHeaders[idx]
    };

    // 详细情况弹窗
    const onOpenDetailDialog = (row: object) => {
      let idx = Number(queryButtonIndex.value);
      if (idx === 0) {
        detailAirportRef.value.openDialog(row);
      } else if (idx === 1) {
        detailAirlineRef.value.openDialog(row);
      }
    };

    // 航空公司详细情况
    const onOpenDetailAirline = (row: object) => {
      detailAirlineRef.value.openDialog(row);
    };
    onMounted(() => {
      queryPlaceholder.value = state.queryTextPlaceHolder[0];
      // initTableData();
    });

    return {
      getAssetsFile,
      isShow,
      tabPosition,
      queryLabels,
      queryPlaceholder,
      queryButtonIndex,
      queryText,
      detailAirportRef,
      detailAirlineRef,
      onHandleRadioGroupChange,
      onHandlePageSizeChange,
      onHandlePageNumChange,
      onOpenDetailDialog,
      onOpenDetailAirline,
      onHandleQuery,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss" scoped>
//深度修改第1个被选中el-radio-button背景
:deep(.el-radio-button__original-radio:checked+.el-radio-button__inner) {
  background: orange;
  border-color: orange;
}

//深度iconfont图标字体以适应el-radio-button type="small"大小
:deep(.iconfont) {
  font-size: 14px
}

:deep(.el-table .cell img){
  //display: table-cell;
  text-align: center;
}

</style>