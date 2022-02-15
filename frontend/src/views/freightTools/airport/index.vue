<template>
  <div class="freightTools-Airport-container">
    <el-card shadow="hover" header="机场代码查询">
      <el-input v-model="queryText" size="small" placeholder="输入机场代码/机场名称/国家(地区)/城市" style="max-width: 280px"> </el-input>
      <el-button type="primary" @click="onQueryAirports" size="small">查询</el-button>
      <el-table :data="tableData.data" style="width: 100%">
				<el-table-column prop="iata_code" label="IATA"></el-table-column>
				<el-table-column prop="icao_code" label="ICAO"></el-table-column>
				<el-table-column prop="airport_chn_name" label="机场名称"></el-table-column>
				<el-table-column prop="country_chn_name" label="国家（地区）"></el-table-column>
				<el-table-column prop="city_chn_name" label="城市"></el-table-column>
			</el-table>
		</el-card>
  </div>
</template>

<script lang="ts">

import {reactive, ref, toRefs} from "vue";
import {queryAirports} from "/@/api/freightTools";

export default {
  name: 'freightToolsAirport',
  components: {},
  setup() {
    const queryText = ref('');
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
		const onQueryAirports = async () => {
      console.log('==airport search==', 'searching...',queryText.value);
      queryAirports({queryText: queryText.value}).then((res:any)=>{
        console.log('==queryAirports==', res);
        state.tableData.data = res.result_data;
      })
		};

    return {
      queryText,
      onQueryAirports,
      ...toRefs(state),
    };
  },
};
</script>