<template>
  <div>
    <div class="container">
      <div class="searFormBox">
        <el-form ref="searchFormRef" :rules="searchFormRules" :model="searchForm" label-width="80px">
          <el-form-item label="质量标准" prop="quantity">
            <el-input v-model="searchForm.quantity" style="width: 180px"
                      ref="search_content_input" class="itemInput">
            </el-input>
          </el-form-item>

          <el-form-item label="快速查找" prop="quickSearchItemName">
            <el-select v-model="searchForm.quickSearchOptionValue" clearable placeholder='请选择' style="width: 120px;"
                       @change="changeHandle">
              <el-option
                  v-for="item in quickSearchOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
              >
              </el-option>
            </el-select>
            <el-input v-model="searchForm.searchValue" placeholder="请输入" style="width: 180px"
                      ref="search_content_input" class="itemInput">
            </el-input>
          </el-form-item>


          <el-form-item label="选择器" prop="region">
            <el-select v-model="searchForm.region" placeholder="请选择">
              <el-option key="bbk" label="步步高" value="bbk"></el-option>
              <el-option key="xtc" label="小天才" value="xtc"></el-option>
              <el-option key="imoo" label="imoo" value="imoo"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="日期时间">
            <el-col :span="11">
              <el-form-item prop="date1">
                <el-date-picker type="date" placeholder="选择日期" v-model="searchForm.date1"
                                style="width: 100%;"></el-date-picker>
              </el-form-item>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
              <el-form-item prop="date2">
                <el-time-picker placeholder="选择时间" v-model="searchForm.date2" style="width: 100%;">
                </el-time-picker>
              </el-form-item>
            </el-col>
          </el-form-item>
          <el-form-item label="选择开关" prop="delivery">
            <el-switch v-model="searchForm.delivery"></el-switch>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">表单提交</el-button>
            <el-button @click="onReset">重置表单</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import {reactive, ref} from "vue";
import {ElMessage} from "element-plus";

export default {
  name: "baseform",
  setup() {
    const options = [
      {
        value: "guangdong",
        label: "广东省",
        children: [
          {
            value: "guangzhou",
            label: "广州市",
            children: [
              {
                value: "tianhe",
                label: "天河区",
              },
              {
                value: "haizhu",
                label: "海珠区",
              },
            ],
          },
          {
            value: "dongguan",
            label: "东莞市",
            children: [
              {
                value: "changan",
                label: "长安镇",
              },
              {
                value: "humen",
                label: "虎门镇",
              },
            ],
          },
        ],
      },
      {
        value: "hunan",
        label: "湖南省",
        children: [
          {
            value: "changsha",
            label: "长沙市",
            children: [
              {
                value: "yuelu",
                label: "岳麓区",
              },
            ],
          },
        ],
      },
    ];
    const searchFormRef = ref(null);
    const searchForm = reactive({
      name: '',
      region: '',
      quantity,
      quickSearchOptionValue: '',
      searchValue: '',
    })
    const quickSearchOptions = ref([
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
      }])
    const searchFormRules = {};

    const changeHandle = () => {
      // searchItemPlaceholder.value = '请输入' + searchForm.quickSearchOptionValue
      // // searchForm.searchValue = ''
      // console.log(searchForm)
    }
    // 提交
    const onSubmit = () => {

    };
    // 重置
    const onReset = () => {

      searchFormRef.value.resetFields()
    };

    return {
      options,
      searchFormRules,
      searchFormRef,
      searchForm,
      quickSearchOptions,
      changeHandle,
      onSubmit,
      onReset,
    };
  },
};
</script>