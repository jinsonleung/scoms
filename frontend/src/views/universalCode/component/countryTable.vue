<template>
  <div class="universalCode-countryTable-container">
    <el-table :data="tableData.data" style="width:100%">
      <el-table-column type="index" label="No" min-width="40px"></el-table-column>
      <el-table-column prop="iso2_code" label="ISO2" min-width="60px"></el-table-column>
      <el-table-column prop="iso3_code" label="ISO3" min-width="60px"></el-table-column>
      <el-table-column prop="chn_name" label="国家名称" min-width="120px">
        <template #default="scope">
          <country-flag :country='scope.row.iso2_code' size='small'/>
          {{ scope.row.chn_name }}<br/>{{ scope.row.full_eng_name }}
        </template>
      </el-table-column>
      <el-table-column prop="continent.chn_name" label="洲名" min-width="80px">
        <template #default="scope">
          {{ scope.row.continent.chn_name }}<br/>{{ scope.row.continent.eng_name }}
        </template>
      </el-table-column>
      <el-table-column label="操作" show-overflow-tooltip width="120px">
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
    <CountryDetail ref="countryDetailRef"/>
  </div>
</template>

<script lang="ts">
import {inject, reactive, toRefs, ref} from "vue";
import CountryDetail from "/@/views/universalCode/component/countryDetail.vue";
import {queryCountries} from "/@/api/universalCode";
import CountryFlag from "vue-country-flag-next";
import commonFunction from "/@/utils/commonFunction";

export default {
  name: 'freightToolsCountryTable',
  components: {CountryFlag, CountryDetail},
  setup() {
    const countryDetailRef = ref();
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
      getPageCountries(queryText.value, 1, pageSize);
    };

    // 页码改变事件
    const onHandlePageNumChange = (pageNum: number) => {
      state.tableData.param.pageNum = pageNum;
      let pageSize = state.tableData.param.pageSize;
      getPageCountries(queryText.value, pageNum, pageSize);
      console.log('onHandlePageNumChange', state.tableData.data.length)
    };

    // 详细情况弹窗
    const onOpenDetailDialog = (row: object) => {
      countryDetailRef.value.openDialog(row);
    };

    const getPageCountries = async (queryText: any, pageNum: number, pageSize: number) => {
      queryCountries({queryText, pageNum, pageSize}).then((res: any) => {
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };


    return {
      queryText,
      countryDetailRef,
      getAssetsFile,
      getPageCountries,
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