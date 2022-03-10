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
        <AirportTable ref="airportTableRef" />
      </div>
      <!--航司代码查询列表-->
      <div v-else-if="isShow==1">
        <AirlineTable ref="airlineTableRef" />
      </div>
      <!--国家代码查询列表-->
      <div v-else-if="isShow==2">
        <CountryTable ref="countryTableRef" />
      </div>

    </el-card>
    <!--机场详情弹窗-->
    <DetailAirport ref="detailAirportRef"/>
    <!--航司详情弹窗-->
    <DetailAirline ref="detailAirlineRef"/>
  </div>
</template>

<script lang="ts">

import { provide, reactive, ref, toRefs} from "vue";
import DetailAirport from "/@/views/universalCode/component/detailAirport.vue";
import DetailAirline from "/@/views/universalCode/component/detailAirline.vue";
import AirportTable from "/@/views/universalCode/component/airportTable.vue";
import AirlineTable from "/@/views/universalCode/component/airlineTable.vue";
import CountryTable from "/@/views/universalCode/component/countryTable.vue";

import commonFunction from "/@/utils/commonFunction";


export default {
  name: 'freightToolsAirport',
  components: {DetailAirport, DetailAirline, AirportTable, AirlineTable, CountryTable},
  setup() {
    const isShow = ref(0);
    const tabPosition = ref(0);
    const queryLabels = ref([{icon: 'elementPosition', label: '机场代码查询'}, {
      icon: 'elementVan',
      label: '航司代码查询'
    }, {icon: 'elementPosition', label: '国家代码查询'}, {icon: 'elementPosition', label: '其他查询'},]);
    const queryButtonIndex = ref(0);
    const queryPlaceholder = ref('');
    const queryText = ref('');
    const detailAirportRef = ref();
    const detailAirlineRef = ref();
    const airportTableRef = ref();
    const airlineTableRef = ref();
    const countryTableRef = ref();

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

    provide("parentQueryText", queryText)   // 向子组件转值

    // 分类查询按钮单击事件
    const onHandleRadioGroupChange = (index: number) => {
      // console.log('==onHandleRadioGroupChange.index==', index)
      isShow.value = index;
      queryButtonIndex.value = index;
      queryPlaceholder.value = state.queryTextPlaceHolder[index];
    };

    // 查询
    const onHandleQuery = (index: number) => {
      let query_text = queryText.value.trim()
      if (query_text === '') return;
      airportTableRef.value.getPageAirports(query_text,1,10);
      // console.log('==onHandleQuery==', index);

    };


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
      airportTableRef,
      airlineTableRef,
      countryTableRef,
      onHandleRadioGroupChange,
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