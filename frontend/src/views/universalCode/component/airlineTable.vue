<template>
  <div class="universalCode-airportTable-container">
    <el-table :data="tableData.data" stripe>
      <el-table-column align="center" type="index" label="No" min-width="40px"></el-table-column>
      <el-table-column align="center" prop="iata_code" label="IATA" min-width="60px"></el-table-column>
      <el-table-column align="center" prop="icao_code" label="ICAO" min-width="60px"></el-table-column>
      <el-table-column prop="airline_prefix_code" label="前缀代码" min-width="80px"></el-table-column>
      <el-table-column prop="chn_name" label="航司名称" min-width="250px">
        <template #default="scope">
          <!--如果航司Logo不存在，则使用默认Logo取代-->
          <div class="countryFlag">
            <img v-realimage="getAssetsFile(`images/airlinesLogo/${scope.row.iata_code}.png`)" :default-image="getAssetsFile('images/airlinesLogo/_default1.png')"
            alt=""/>{{ scope.row.chn_name }}<br/>{{ scope.row.eng_name }}
          </div>
        </template>
      </el-table-column>
      <el-table-column prop="country.chn_name" label="国家/地区" min-width="150px">
        <template #default="scope">
          <div class="countryFlag">
            <country-flag :country='scope.row.country_iso2_code' size='normal' style="margin: -0.4em"/>
            {{ scope.row.country.chn_name }}<br/>{{ scope.row.country.eng_name }}
          </div>
        </template>
      </el-table-column>
      <el-table-column align="center" label="操作" show-overflow-tooltip width="120px">
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
    <!--机场详情弹窗-->
    <AirlineDetail ref="airlineDetailRef"/>
  </div>
</template>

<script lang="ts">
import {inject, reactive, toRefs, ref} from "vue";
import AirlineDetail from "/@/views/universalCode/component/airlineDetail.vue";
import {queryAirlines} from "/@/api/universalCode";
import CountryFlag from "vue-country-flag-next";
import commonFunction from "/@/utils/commonFunction";

export default {
  name: 'freightToolsAirlineTable',
  components: {CountryFlag, AirlineDetail},
  setup() {
    const airlineDetailRef = ref();
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
    const {getAssetsFile} = commonFunction();
    // 页长改变事件
    const onHandlePageSizeChange = (pageSize: number) => {
      state.tableData.param.pageSize = pageSize;
      state.tableData.param.pageNum = 1;
      getPageAirlines(queryText.value, 1, pageSize);
    };

    // 页码改变事件
    const onHandlePageNumChange = (pageNum: number) => {
      state.tableData.param.pageNum = pageNum;
      let pageSize = state.tableData.param.pageSize;
      getPageAirlines(queryText.value, pageNum, pageSize);
    };

    // 详细情况弹窗
    const onOpenDetailDialog = (row: object) => {
      airlineDetailRef.value.openDialog(row);
    };

    const getPageAirlines = async (queryText: any, pageNum: number, pageSize: number) => {
      queryAirlines({queryText, pageNum, pageSize}).then((res: any) => {
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };
    
    return {
      queryText,
      airlineDetailRef,
      getAssetsFile,
      getPageAirlines,
      onHandlePageSizeChange,
      onHandlePageNumChange,
      onOpenDetailDialog,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss" scoped>
.countryFlag { //图片垂直居中
  display: flex;
  align-items: center;
  line-height: 1.2; //行矩
  img {
    width: 40px;
    height: 40px;
  }
}
</style>