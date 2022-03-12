<template>
  <div class="universalCode-airportTable-container">
    <el-table :data="tableData.data" stripe>
      <el-table-column align="center" type="index" label="No" min-width="40px"></el-table-column>
      <el-table-column align="center" prop="iata_code" label="IATA" min-width="60px"></el-table-column>
      <el-table-column prop="icao_code" label="ICAO" min-width="60px"></el-table-column>
      <el-table-column prop="chn_name" label="机场名称" min-width="180px">
        <template #default="scope">
          <div class="countryFlag">
          {{ scope.row.chn_name }}<br/>{{ scope.row.eng_name }}
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="country.chn_name" label="国家/地区" min-width="150px">
        <template #default="scope">
          <div class="countryFlag">
          <country-flag :country='scope.row.country.iso2_code' size='normal' style="margin: -0.4em"/>
          {{ scope.row.country.chn_name }}
          <br/>{{ scope.row.country.eng_name }}
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="city_chn_name" label="城市名称" min-width="150px">
        <template #default="scope">
          <div class="countryFlag">
          {{ scope.row.city_chn_name }}<br/>{{ scope.row.city_eng_name }}
          </div>
        </template>
      </el-table-column>
      <el-table-column align="center" label="操作" min-width="120px">
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
        v-model:current-page="tableData.param.pageNum"
        background
        v-model:page-size="tableData.param.pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="tableData.total"
    >
    </el-pagination>
    <!--机场详情弹窗-->
    <AirportDetail ref="airportDetailRef"/>
  </div>
</template>

<script lang="ts">
import {inject, reactive, ref, toRefs} from "vue";
import AirportDetail from "/@/views/universalCode/component/airportDetail.vue";
import {queryAirports} from "/@/api/universalCode";
import CountryFlag from "vue-country-flag-next";

export default {
  name: 'freightToolsAirportTable',
  components: {CountryFlag, AirportDetail},
  setup() {
    const airportDetailRef = ref();
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
    });
    //注入父组件的转过来的查询字符串
    const queryText = inject("parentQueryText");

    // 页长改变事件
    const onHandlePageSizeChange = (pageSize: number) => {
      state.tableData.param.pageSize = pageSize;
      state.tableData.param.pageNum = 1;
      getPageAirports(queryText.value, 1, pageSize);
    };

    // 页码改变事件
    const onHandlePageNumChange = (pageNum: number) => {
      state.tableData.param.pageNum = pageNum;
      let pageSize = state.tableData.param.pageSize;
      getPageAirports(queryText.value, pageNum, pageSize);
    };

    // 详细情况弹窗
    const onOpenDetailDialog = (row: object) => {
      airportDetailRef.value.openDialog(row);
    };

    const getPageAirports = async (queryText: any, pageNum: number, pageSize: number) => {
      queryAirports({queryText, pageNum, pageSize}).then((res: any) => {
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };

    return {
      queryText,
      airportDetailRef,
      getPageAirports,
      onHandlePageSizeChange,
      onHandlePageNumChange,
      onOpenDetailDialog,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss" scoped>
:deep(.countryFlag) { //图片垂直居中
  display: flex;
  align-items: center;
  line-height: 1.2; //行矩
  vertical-align: center;
  horiz-align: center;
  img {
  }
}


</style>