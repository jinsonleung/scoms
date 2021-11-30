<template>
  <h3>==分页，正确==</h3>
  <h3>==获取MYSQL分页表格数据==</h3>
  <el-table :data="table_data" height="600" style="width: 100%">
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
      :total="total_counts"
      :options="query"
      :render="getPageData">
  </v-pagination>
</template>
<script>
import {ref, reactive, getCurrentInstance, onMounted} from "vue"
import vPagination from '@/components/pagination.vue'
import http from '@/utils/http2/index'
import '@/mock/mockServer'


export default {
  components: {
    vPagination,
  },
  setup() {
    const table_data = ref([]),//表格数据列表
        total_counts = ref(0),//总条目数，总记录数
        query = reactive({//配置对应的查询参数
          appTimeStart: 'tt',
          appTimeEnd: 'aaaa',
          page: 1,
          limit: 10,//page第几页,limit是一页几个
        });
    onMounted(() => { //页面挂载钩子函数
      getPageData();
    })
    // 获取MYSQL分页表格数据
    const getPageData = () => {
      http.get('customer/getpagelist?limit=' + query.limit + '&offset=' + (query.page - 1)).then(res => {  // 正确，分页带参请求
        console.log('==res==', res)
        total_counts.value = res.data.length  //总记录条数

        let customer_list = res.data.customerList
        console.log("===customer_list==>>>>>>>", customer_list)
        table_data.value = customer_list // 分页数据列表
      })
    }

    // 获取MOCKJS分页表格数据
    const getPageData333 = () => {
      http.get('/mockcustomer/getpage?limit=' + query.limit + '&offset=' + (query.page - 1)).then(res => {  // 正确，分页带参请求
        // console.log('==res==', res.data.length)
        console.log('==res.data.customerList==', res.data.customerList)
        total_counts.value = res.data.length  //总记录条数
        let customer_list = res.data.customerList
        table_data.value = customer_list // 分页数据列表
      })
    }
    // 获取MOCKJS分页表格数据
    const getPageData2 = () => {  // 获取MOCKJS全部记录
      http.get('/mockcustomer/getall').then(res => {  // 正确
        console.log('==res==', res.data.data.customerList)
        let customer_list = res.data.data.customerList
        console.log('==customer_list.length==', customer_list.length)
        total_counts.value = customer_list.length  // 总记录条数
        table_data.value = customer_list // 分页数据列表
      })
    }

    return {
      query,
      // shortcuts,
      table_data,
      total_counts,
      getPageData
    };
  }
}
</script>
