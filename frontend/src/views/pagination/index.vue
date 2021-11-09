<template>
    <el-table :data="tableData" height="250" style="width: 100%">
    <el-table-column prop="date" label="Date" width="180" />
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column prop="address" label="Address" />
  </el-table>

  <v-pagination
      :pagesize="query.limit"
      :total="pageTotal"
      :options="query"
      :render="getData">
  </v-pagination>
</template>
<script>
import {ref, reactive, getCurrentInstance} from "vue"
import vPagination from '@/components/pagination.vue'
import http from '@/utils/http2/index'


export default {
  components: {
    vPagination,
  },
  setup() {
    const tableData = ref([]),//表格数据
        pageTotal = ref(0),//总条数
        query = reactive({//配置对应的查询参数
          appTimeStart: '',
          appTimeEnd: '',
          page: 1,
          limit: 10,//page第几页,limit是一页几个
        });
    // 获取表格数据
    const getData = () => {
      console.log('==getData==')

      http.get('/books/getall').then(res => {
        console.log('==res==', res.data.list)
        console.log('==res.data.list.count==', res.data.list.count)

        // pageTotal.value = res.data.list.count;
        // tableData.value = res.data.list;
      })
    }
    //  proxy.$request({
    //   url: 'api/getList',
    //   method: 'POST',
    //   data:query
    // }).then(res => {
    // 	pageTotal.value = res.count;
    // 	tableData.value = res.data;
    // })
    getData();
    return {
      query,
      // shortcuts,
      tableData,
      pageTotal,
      getData
    };
  }
}
</script>
