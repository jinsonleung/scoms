<template>
  <div class="universalCode-Airport-container">
    <el-card shadow="hover" header="机场代码查询">
      <!--查询选项（机场代码查询/航司代码查询/国家代码查询）-->
      <div class="query-container">
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
      <!--分隔线-->
      <el-divider></el-divider>
      <!--机场代码查询列表-->
      <div v-if="isShow==0">
        <AirportTable ref="airportTableRef"/>
      </div>
      <!--航司代码查询列表-->
      <div v-else-if="isShow==1">
        <AirlineTable ref="airlineTableRef"/>
      </div>
      <!--国家代码查询列表-->
      <div v-else-if="isShow==2">
        <CountryTable ref="countryTableRef"/>
      </div>
    </el-card>
  </div>
</template>
<script lang="ts">

import {provide, reactive, ref} from "vue";
import AirportTable from "/@/views/universalCode/component/airportTable.vue";
import AirlineTable from "/@/views/universalCode/component/airlineTable.vue";
import CountryTable from "/@/views/universalCode/component/countryTable.vue";

export default {
  name: 'freightToolsAirport',
  components: {AirportTable, AirlineTable, CountryTable},
  setup() {
    const isShow = ref(0);
    const tabPosition = ref(0);
    const queryButtonIndex = ref(0);
    const queryText = ref('');
    const airportTableRef = ref();
    const airlineTableRef = ref();
    const countryTableRef = ref();
    const queryPlaceholders = reactive(['输入机场代码/机场名称/国家(地区)/城市', '输入航司代码/国家(地区)/城市', '输入国家代码']);
    const queryPlaceholder = ref(queryPlaceholders[0]);
    provide("parentQueryText", queryText)   // 向子组件转值

    // 分类查询按钮单击事件
    const onHandleRadioGroupChange = (index: number) => {
      isShow.value = index;
      queryButtonIndex.value = index;
      queryText.value = '';
      queryPlaceholder.value = queryPlaceholders[index];
    };

    // 查询
    const onHandleQuery = (index: number) => {
      let query_text = queryText.value.trim()
      if (query_text === '') return;
      if (index == 0) {
        airportTableRef.value.getPageAirports(query_text, 1, 10);
      } else if (index == 1) {
        airlineTableRef.value.getPageAirlines(query_text, 1, 10);
      } else if (index == 2) {
        countryTableRef.value.getPageCountries(query_text, 1, 10);
      }
    };

    return {
      isShow,
      tabPosition,
      queryPlaceholder,
      queryPlaceholders,
      queryButtonIndex,
      queryText,
      airportTableRef,
      airlineTableRef,
      countryTableRef,
      onHandleRadioGroupChange,
      onHandleQuery,
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

:deep(.el-table .cell img) {
  //display: table-cell;
  text-align: center;
}

</style>