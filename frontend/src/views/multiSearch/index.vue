<template>
  <h3>==多条件查询==</h3>
  <h4>https://www.cnblogs.com/jyk/p/14841929.html</h4>
  <h4>https://www.cnblogs.com/wuhuacong/p/14035302.html</h4>
  <!--  查询条件区域-->
  <el-form ref="searchForm" :model="searchForm" label-width="80" :inline="true">
    <el-select v-model="value" clearable placeholder='请选择' style="width: 120px" @change="changeHandle">
      <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
      >
      </el-option>
    </el-select>
    <el-input v-model="searchValue" :placeholder=searchItem style="width: 180px" ref="search_content_input">
    </el-input>


    <el-button-group style="margin-left: 20px">
      <el-button type="primary" icon="el-icons-reset" round>查询</el-button>
      <el-button type="warning" icon="el-icons-reset">重置</el-button>
      <el-button type="primary" icon="el-icons-search" round>高级查询</el-button>
    </el-button-group>
  </el-form>


</template>
<script lang="ts">
import {ref, reactive, getCurrentInstance, onMounted, toRefs} from "vue"
import vPagination from '@/components/pagination.vue'
import {Search, Edit, ArrowLeft} from '@element-plus/icons'


export default {
  components: {
    vPagination,
    Search,
    Edit,
  },
  setup() {
    const value = ref('')
    const options = ref([
      {
        value: '公司账号',
        label: '公司账号',
      },
      {
        value: '公司名称',
        label: '公司名称',
      },
      {
        value: '服务类别',
        label: '服务类别',
      },
      {
        value: '是否生效',
        label: '是否生效',
      },
      {
        value: '有效期',
        label: '有效期',
      },
    ])
    const searchItem = ref('')
    const searchValue = ref('')
    const proxy = getCurrentInstance()
    const searchForm = reactive([])
    const changeHandle = ()=>{
      searchItem.value = '请输入' + value.value
       console.log(proxy)
    }




    return {
      value,
      options,
      searchItem,
      searchValue,
      changeHandle,
      searchForm,
    };
  }
}
</script>
