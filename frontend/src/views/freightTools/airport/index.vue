<template>
  <div class="freightTools-Airport-container">
    <el-card shadow="hover" header="机场代码查询">
      <el-input size="small" placeholder="输入机场代码/机场名称/国家(地区)/城市" style="max-width: 280px"> </el-input>
      <el-button type="primary" @click="" size="small">查询</el-button>
      <el-table :data="tableData" style="width: 100%">
				<el-table-column prop="a1" label="IATA"> </el-table-column>
				<el-table-column prop="a2" label="ICAO"> </el-table-column>
				<el-table-column prop="a3" label="机场名称"> </el-table-column>
				<el-table-column prop="a4" label="国家（地区）"> </el-table-column>
				<el-table-column prop="a5" label="城市"> </el-table-column>
			</el-table>
		</el-card>
  </div>
</template>

<script lang="ts">

export default {
  name: 'freightToolsAirport',
  components: {},
  setup() {

    return {
    };
  },
};
</script>