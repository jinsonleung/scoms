<template>
  <div class="universalCode-airportTable-container">
    <h1>====机场信息====</h1>
    来自父组件的值：{{queryText}}
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
        <template #default="scope">
          <country-flag :country='scope.row.country.iso2_code' size='small'/>
          {{ scope.row.country.chn_name }}
          <br/>{{ scope.row.country.eng_name }}
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
        v-model:current-page="tableData.param.pageNum"
        background
        v-model:page-size="tableData.param.pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="tableData.total"
    >
    </el-pagination>


    <!--机场详情弹窗-->
    <DetailAirport ref="detailAirportRef"/>
  </div>
</template>

<script lang="ts">
import {inject, reactive, toRefs} from "vue";
import DetailAirport from "/@/views/universalCode/component/detailAirport.vue";
import {queryAirports} from "/@/api/universalCode";
import CountryFlag from "vue-country-flag-next";

export default {
  name: 'freightToolsAirportTable',
  components: {CountryFlag,DetailAirport},
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
      console.log('onHandlePageNumChange', state.tableData.data.length)
    };

    // 详细情况弹窗
    const onOpenDetailDialog = (row: object) => {
      console.log('==dialog here==', row);
    };

    const getPageAirports = async (queryText: any, pageNum: number, pageSize: number) => {
      queryAirports({queryText, pageNum, pageSize}).then((res: any) => {
        console.log('==res==', res)
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };


    return {
      queryText,
      getPageAirports,
      onHandlePageSizeChange,
      onHandlePageNumChange,
      onOpenDetailDialog,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss">

</style>