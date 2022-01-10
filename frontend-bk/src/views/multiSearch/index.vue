<template>
  <h3>==多条件查询==</h3>
  <h4>https://www.cnblogs.com/jyk/p/14841929.html</h4>
  <h4>https://www.cnblogs.com/wuhuacong/p/14035302.html</h4>
  <!--查询条件区域-->
  <el-form ref="searchFormRef" :model="searchForm" :rules="rules" label-width="80" :inline="true" class="searchForm">
    <el-form-item label="快速查询" prop="quickSearchValue">
      <el-select v-model="searchForm.quickSearchValue" clearable placeholder='请选择' style="width: 120px;"
                 @change="changeHandle">
        <el-option
            v-for="item in searchForm.quickSearchOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
        >
        </el-option>
      </el-select>
      <el-input v-model="searchForm.searchValue" :placeholder=searchItemPlaceholder style="width: 180px"
                ref="search_content_input" class="itemInput">
      </el-input>
    </el-form-item>

    <!--展开更多条件-->
    <div v-if="expandMore">
      <el-form-item label="所在城市" prop="cityName">
        <el-input class="itemInput" v-model="searchForm.cityName"></el-input>
      </el-form-item>
      <el-form-item label="是否生效" prop="isActivate">
        <el-select v-model="searchForm.isActivate" placeholder="请选择">
          <el-option
              v-for="item in searchForm.isActivateOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="服务类别" prop="serviceLevel">
        <el-select v-model="searchForm.serviceLevel" placeholder="请选择">
          <el-option
              v-for="item in searchForm.serviceLevelOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>
    </div>
    <!--收起/展开按钮-->
    <el-button :icon="expandMore ?'el-icon-arrow-up':'el-icon-arrow-down'" type="text" @click="expandMore =!expandMore">
      {{ expandMore ? '收起' : '展开' }}
    </el-button>

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
// import {Search, Edit, ArrowLeft} from '@element-plus/icons'
import {ElMessage} from "element-plus";


export default {
  components: {
    vPagination,
    Search,
    Edit,
  },
  setup() {
    const searchFormRef = ref(null)
    const searchForm = reactive({
      quickSearchValue: '',
      searchValue: '',
      cityName: '',
      quickSearchOptions: [
        {
          value: 'companyAccount',
          label: '公司账号',
        },
        {
          value: 'companyName',
          label: '公司名称',
        },
        {
          value: 'serverLevel',
          label: '服务类别',
        },
        {
          value: 'isActivate',
          label: '是否生效',
        },
        {
          value: 'EffectiveDate',
          label: '有效期',
        }],
      isActivate: '',
      isActivateOptions: [
        {
          value: 'yes',
          label: '是',
        },
        {
          value: 'not',
          label: '否',
        }
      ],
      serviceLevel: '',
      serviceLevelOptions: [
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
      ],
    })
    const rules = {}
    const expandMore = ref(false)
    const searchItemPlaceholder = ref('请输入')
    const proxy = getCurrentInstance()
    const changeHandle = () => {
        searchForm.searchValue = ''

      // searchItemPlaceholder.value = '请输入' + searchForm.quickSearchValue

      console.log('quick search value:',searchForm.quickSearchValue)
    }

    // 表单校验
    // searchFormRef.value.validate((valid) => {
    //   if (valid) {
    //     console.log(form);
    //     ElMessage.success("提交成功！");
    //   } else {
    //     return false;
    //   }
    // })

    const searchHandle = () => {
      // if (!quickSearchOptionValue.value || !searchValue.value) return
      // console.log('==search.key & searchvalue==', quickSearchOptionValue.value, searchValue.value)
    }
    const resetHandle = () => {
      searchForm.searchValue = ''
      searchFormRef.value.resetFields() //type断言机制报错，不要紧
    }
    const advanceSearchHandle = () => {

    }


    return {
      rules,
      expandMore,
      searchItemPlaceholder,
      changeHandle,
      searchForm,
      searchFormRef,
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
