<template>
  <h3>==多条件查询==</h3>
  <h4>https://www.cnblogs.com/jyk/p/14841929.html</h4>
  <h4>https://www.cnblogs.com/wuhuacong/p/14035302.html</h4>
  <!--查询条件区域-->
  <el-form ref="searchForm" :model="searchForm" label-width="80" :inline="true" class="searchForm">
    <el-form-item>
      <el-select v-model="optionKey" clearable placeholder='请选择' style="width: 120px;" @change="changeHandle">
        <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        >
        </el-option>
      </el-select>
      <el-input v-model="searchValue" :placeholder=searchItemPlaceholder style="width: 180px"
                ref="search_content_input" class="itemInput">
      </el-input>
    </el-form-item>
    <!--展开/收起-->
    <el-button :icon="expandMore ?'el-icon-arrow-up':'el-icon-arrow-down'" type="text" @click="expandMore =!expandMore">
      {{ expandMore ? '收起' : '展开' }}
    </el-button>
    <!--展开更多条件-->
    <div ref="searchMoreForm" v-if="expandMore">
      <el-form-item label="所在城市">
        <el-input class="itemInput" v-model="city"></el-input>
      </el-form-item>
      <el-form-item label="是否生效">
        <el-select v-model="isActivateValue" placeholder="请选择">
          <el-option
              v-for="item in isActivateOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="服务类别">
        <el-select v-model="serviceLevelValue" placeholder="请选择">
          <el-option
              v-for="item in serviceLevelOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>
    </div>


    <!--查询按钮-->
    <el-button-group style="margin-left: 20px">
      <el-button type="primary" icon="el-icons-reset" round @click="searchHandle">查询</el-button>
      <el-button type="warning" icon="el-icons-reset" @click="resetHandle">重置</el-button>
      <el-button type="primary" icon="el-icons-search" round @click="advanceSearchHandle">高级查询</el-button>
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
    const expandMore = ref(false)
    const optionKey = ref('')
    const city = ref('')
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
    const isActivateOptions = ref([
      {
        value: '是',
        label: '是',
      },
      {
        value: '否',
        label: '否',
      },
    ])
    const serviceLevelOptions = ref([
      {
        value: '1',
        label: '1',
      },
      {
        value: '2',
        label: '2',
      },
      {
        value: '3',
        label: '3',
      },
      {
        value: '4',
        label: '4',
      },
      {
        value: '5',
        label: '5',
      },
    ])

    const searchItemPlaceholder = ref('')
    const searchValue = ref('')
    const isActivateValue = ref('')
    const serviceLevelValue = ref('')
    const proxy = getCurrentInstance()
    const searchForm = reactive([])

    const changeHandle = () => {
      searchItemPlaceholder.value = '请输入' + optionKey.value
      searchValue.value = ''
      console.log(proxy)
    }


    const searchHandle = () => {
      if (!optionKey.value || !searchValue.value) return
      console.log('==search.key & searchvalue==', optionKey.value, searchValue.value)
    }
    const resetHandle = () => {
      optionKey.value = ''
      searchValue.value = ''
      searchItemPlaceholder.value = ''
    }
    const advanceSearchHandle = () => {

    }


    return {
      expandMore,
      optionKey,
      options,
      city,
      isActivateOptions,
      serviceLevelOptions,
      isActivateValue,
      serviceLevelValue,
      searchItemPlaceholder,
      searchValue,
      changeHandle,
      searchForm,
      searchHandle,
      resetHandle,
      advanceSearchHandle,
    };
  }
}
</script>

<style>
.itemInput {
  width: 150px;
}
</style>
