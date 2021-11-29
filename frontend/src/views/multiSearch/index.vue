<template>
  <h3>==多条件查询==</h3>
  <h4>https://www.cnblogs.com/jyk/p/14841929.html</h4>
  <h4>https://www.cnblogs.com/wuhuacong/p/14035302.html</h4>
  <!--  查询条件区域-->
  <el-form ref="searchForm" :model="searchForm" label-width="80" :inline="true">
    <el-select v-model="value" clearable placeholder='请选择' >
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    >
    </el-option>

  </el-select>
    <el-input placeholder="请输入内容"  style="width: 180px" >
  </el-input>



    <el-form-item style="width:100px">
      <el-dropdown size="small">
        <el-button type="primary">
          快捷查询<i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item
                v-for="(item, key) in searchItems"
                :key="'quick_' + key"
                @click="quickClick(key)"
            >
              {{ item }}
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>

    </el-form-item>
    <el-form-item style="margin-left: 20px">
      <el-input v-model="searchForm.account" :placeholder=searchItem></el-input>
    </el-form-item>

    <!--  展开更多区域-->
    <template v-if="expandMore">
      <el-form-item label="公司账号">
        <el-input v-model="searchForm.account" placeholder="公司账号"></el-input>
      </el-form-item>
      <el-form-item label="公司名称">
        <el-input v-model="searchForm.name" placeholder="公司名称"></el-input>
      </el-form-item>
      <el-form-item label="服务等级">
        <el-select v-model="searchForm.account" placeholder="公司名称">
          <el-option label="男" value="male"></el-option>
          <el-option label="女" value="femal"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>

        <div class="demo-date-picker">
          <div class="block">
            <span class="demonstration">Default</span>
            <el-date-picker
                v-model="value1"
                type="daterange"
                range-separator="To"
                start-placeholder="Start date"
                end-placeholder="End date"
            >
            </el-date-picker>
          </div>
        </div>
      </el-form-item>
      <el-button type="primary">查询</el-button>
    </template>
  </el-form>

  <el-button-group>
    <el-button type="round">Previous Page</el-button>
    <el-button type="round">
      Next Page
      <el-icon class="el-icon--right">
        <ArrowRight/>
      </el-icon>
    </el-button>
  </el-button-group>
  <el-button :icon="expandMore ?'el-icon-arrow-up':'el-icon-arrow-down'" type="text" @click="expandMore =!expandMore">
    {{ expandMore ? '收起' : '展开' }}
  </el-button>
  <el-button-group>
    <el-button type="primary" round>上一页</el-button>
    <el-button type="">当前页</el-button>
    <el-button type="primary" round>下一页</el-button>
  </el-button-group>


</template>
<script>
import {ref, reactive, getCurrentInstance, onMounted, toRefs} from "vue"
import vPagination from '@/components/pagination.vue'
import http from '@/utils/http2/index'
import '@/mock/mockServer'


export default {
  components: {
    vPagination,
  },
  setup() {
    const expandMore = ref(false) //表格数据列表
    const searchForm = reactive({//配置对应的查询参数
      account: '',
      name: '',
      serviceLevel: '',
    })

    const editForm = reactive({//配置对应的查询参数
      nationality: '',
      education: '',
      marriage: '',
      star: '',
    })
    const searchItem = ref('')  //查询条件名称
    const searchItems = ['公司账号', '公司名称', '服务等级']
    // const searchItems = reactive({ '公司账号', '公司名称', '服务等级']})

    const state = reactive({
      shortcuts: [
        {
          text: 'Last week',
          value: () => {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7)
            return [start, end]
          },
        },
        {
          text: 'Last month',
          value: () => {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30)
            return [start, end]
          },
        },
        {
          text: 'Last 3 months',
          value: () => {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 90)
            return [start, end]
          },
        },
      ],
      value1: '',
      value2: '',
    })

    const quickClick = (key) => {
      // console.log(searchItems[key])
      searchItem.value = searchItems[key]
      console.log(searchItem)
    }

    const getlist = () => { // 列表数据获取
      var param = { // 构造常规的分页查询条件
        // 分页条件
        // SkipCount: (this.pageinfo.pageindex - 1) * this.pageinfo.pagesize,
        // MaxResultCount: this.pageinfo.pagesize,

        // 查询过滤条件
        Name: this.searchForm.name,
        Sex: this.searchForm.name,
        State: this.searchForm.name
      };
      // 使用日期范围选择控件，在查询对象增加开始日期CreationTimeStart、结束日期CreationTimeEnd
      // this.addDateRange(param, this.searchForm.creationTime)
      //
      // // 获取列表，绑定到模型上，并修改分页数量
      // this.listLoading = true
      // testUser.GetAll(param).then(data => {
      //   this.list = data.result.items
      //   this.pageinfo.total = data.result.totalCount
      //   this.listLoading = false
      // })
    }

    return {
      searchItem,
      searchItems,
      expandMore,
      searchForm,
      getlist,
      editForm,
      quickClick,
      ...toRefs(state)
    };
  }
}
</script>
