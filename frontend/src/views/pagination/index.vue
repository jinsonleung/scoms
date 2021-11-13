<template>
  <el-table :data="tableData" height="600" style="width: 100%">
    <el-table-column prop="id" label="id" width="80"/>
    <el-table-column prop="company_account" label="公司账号" width="180"/>
    <el-table-column prop="company_name" label="公司名称" width="180"/>
    <el-table-column prop="company_abbreviation_name" label="公司简称" width="180"/>
    <el-table-column prop="company_address" label="公司地址" width="180"/>
    <el-table-column prop="city" label="所在城市" width="180"/>
    <el-table-column prop="license_no" label="营业执照号码" width="180"/>
    <el-table-column prop="license_image" label="营业执照图片" width="180"/>
    <el-table-column prop="registration_capital" label="注册资金" width="180"/>
    <el-table-column prop="registration_date" label="注册日期" width="180"/>
    <el-table-column prop="registration_effect_start" label="有效期开始日期" width="180"/>
    <el-table-column prop="registration_effect_end" label="有效期结束日期" width="180"/>
    <el-table-column prop="industry" label="所在行业" width="180"/>
    <el-table-column prop="contact_name" label="联系人姓名" width="180"/>
    <el-table-column prop="contact_tel" label="联系人电话" width="180"/>
    <el-table-column prop="contact_phone" label="联系人手机号码" width="180"/>
    <el-table-column prop="is_available" label="是否启用" width="180"/>
    <el-table-column prop="service_level" label="服务类别" width="180"/>
    <el-table-column prop="remark" label="备注" width="180"/>
    <el-table-column prop="is_delete" label="删除标志" width="180"/>
    <el-table-column prop="create_datetime" label="创建记录日期" width="180"/>
    <el-table-column prop="create_user" label="创建人" width="180"/>
    <el-table-column prop="update_datetime" label="更新记录日期" width="180"/>
    <el-table-column prop="update_user" label="更新人" width="180"/>
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
import '@/mock/mockServer'


export default {
  components: {
    vPagination,
  },
  setup() {
    const tableData = ref([]),//表格数据
        pageTotal = ref(0),//总条数
        query = reactive({//配置对应的查询参数
          appTimeStart: 'tt',
          appTimeEnd: 'aaaa',
          page: 1,
          limit: 10,//page第几页,limit是一页几个
        });
    // 获取表格数据
    const getData = () => {
      console.log('==query.page==', query.page)  //当前页
      console.log('==query.limit==', query.limit)  //分页页长
      let params = {
        page_limit: query.limit, // 页长
        offset: (query.page-1)  // 偏移量
      }
      console.log('==params==',params)

      http.get('/mockcustomer/getpage?limit='+query.limit + '&offset='+(query.page-1)).then(res => {  // 正确，分页带参请求
        console.log('==res==', res.data.customerList)
        let customer_list = res.data.customerList
        tableData.value = customer_list // 记录集
      })

      // http.get('/mockcustomer/getall').then(res => {  // 正确
      //   console.log('==res==', res.data.data.customerList)
      //   let customer_list = res.data.data.customerList
      //   console.log('==customer_list.length==', customer_list.length)
      //   tableData.value = customer_list // 记录集
      //   pageTotal.value = customer_list.length  // 记录总条数
      // })
    }
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
