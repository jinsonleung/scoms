<template>
  <div class="universalCode-Airport-container">
    <el-card shadow="hover">
      <!--1.查询框-->
      <div class="query-container">
        <el-row>
          <el-input v-model="queryText" size="small" placeholder="请输入供应商账号/公司名" clearable
                    style="max-width: 360px"></el-input>
          <el-button type="primary" @change="onHandleQuery()" size="small" style="margin-left: 10px">
            <el-icon><elementSearch/></el-icon>查询
          </el-button>
          <el-button type="primary" size="small" @click="onOpenAddDialog"><el-icon><elementStar/></el-icon>新增供应商</el-button>
        </el-row>
      </div>
      <!--全球国家省市区级联-->
      <div>
        <el-row>
							<el-select v-model="linkage.country" placeholder="请选择国家" size="small" clearable @change="onCountryChange" class="w100">
								<el-option v-for="(v, k) in linkage.countryList" :key="k" :label="v.chn_name" :value="v.chn_name">
                      <span style="float: left">{{ v.chn_name }}</span>
                      <span style="float: right; color: var(--el-text-color-secondary);font-size: 13px;">{{ v.eng_name }}</span>
                </el-option>
							</el-select>
							<el-select v-model="linkage.province" placeholder="请选择省(洲)" size="small" clearable @change="onProvinceChange" class="w100">
								<el-option v-for="(v, k) in linkage.provinceList" :key="k" :label="v.chn_name" :value="v.chn_name">
                        <span style="float: left">{{ v.chn_name }}</span>
                        <span
                          style="
                            float: right;
                            color: var(--el-text-color-secondary);
                            font-size: 13px;
                          "
                          >{{ v.eng_name }}</span
                        >
                </el-option>
							</el-select>
							<el-select v-model="linkage.city" placeholder="请选择省(洲)" size="small" clearable @change="onCityChange" class="w100">
								<el-option v-for="(v, k) in linkage.cityList" :key="k" :label="v.chn_name" :value="v.chn_name">
                        <span style="float: left">{{ v.chn_name }}</span>
                        <span
                          style="
                            float: right;
                            color: var(--el-text-color-secondary);
                            font-size: 13px;
                          "
                          >{{ v.eng_name }}</span
                        >
                </el-option>
							</el-select>
							<el-select v-model="linkage.district" placeholder="请选择省(洲)" size="small" clearable @change="onDistrictChange" class="w100">
								<el-option v-for="(v, k) in linkage.districtList" :key="k" :label="v.chn_name" :value="v.chn_name">
                        <span style="float: left">{{ v.chn_name }}</span>
                        <span
                          style="
                            float: right;
                            color: var(--el-text-color-secondary);
                            font-size: 13px;
                          "
                          >{{ v.eng_name }}</span
                        >
                </el-option>
							</el-select>
        </el-row>
      </div>
      <!--2.表单-->
      <el-table :data="tableData.data" stripe row-key="id" style="width: 100%">
        <!--1.1嵌套子表：供应商联系人-->
        <el-table-column type="expand" label="E/C" min-width="20px">
          <template #default="scope">
            <el-table class="child-table" :data="scope.row.contact" stripe style="width: 100%">
              <el-table-column align="center" label="供应商联系方式">
                <el-table-column align="center" show-overflow-tooltip type="index" label="№"
                                 min-width="20px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="department" label="部门"
                                 min-width="40px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="title" label="职位"
                                 min-width="40px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="chn_name" label="中文名"
                                 min-width="40px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="eng_name" label="英文名"
                                 min-width="60px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="tel" label="电话"
                                 min-width="60px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="phone" label="手机"
                                 min-width="60px"></el-table-column>
                <el-table-column align="center" show-overflow-tooltip prop="email" label="邮箱"
                                 min-width="100px"></el-table-column>
                <el-table-column align="center" label="操作" show-overflow-tooltip width="180px">
                  <template #header>
                    <el-button-group>
                      <el-tooltip>操作</el-tooltip>
                        <el-button class="th-head-button" type="primary" @click="onOpenAddSupplierContactDialog(scope.row.id)">新建</el-button>
                    </el-button-group>
                  </template>
                  <template #default="scope">
                    <el-button class="tr-button" type="text" plain :icon="ZoomIn" title="详情"
                               @click="onOpenSupplierContactDetailDialog(scope.row)"></el-button>
                    <el-button class="tr-button" type="text" plain :icon="Edit" title="编辑"
                               @click="onOpenEditSupplierContactDialog(scope.row)"></el-button>
                    <el-button class="tr-button" type="text" plain :icon="Delete" title="删除"
                               @click="onDeleteSupplierContactRow(scope.row)"></el-button>
                  </template>
                </el-table-column>
              </el-table-column>
            </el-table>
          </template>
        </el-table-column>
        <!--1.2主表：供应商信息表-->
        <el-table-column align="center" show-overflow-tooltip type="index" label="№" min-width="10px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="account" label="账号"
                         min-width="80px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="abbreviation_name" label="简称"
                         min-width="100px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="full_name" label="全称"
                         min-width="180px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="office_address" label="办公地址"
                         min-width="150px"></el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="service_type" label="服务类型"
                         min-width="80px">
          <template #default="scope">
            {{getOptionsLabel(SupplierServiceTypes,scope.row.service_type)}}
          </template>
        </el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="status_label" label="使用状态" min-width="70px">
          <template #default="scope">
            <el-tag :type="tagType[scope.row.status_label]" size="mini" effect="dark">{{scope.row.status_label}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="status_label" label="营业状态" min-width="70px">
          <template #default="scope">
            <el-tag :type="effectiveStatus[getEffectiveStatus(scope.row.effective_end_date)]" size="mini" effect="dark">{{getEffectiveStatus(scope.row.effective_end_date)}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column align="center" show-overflow-tooltip prop="status_label" label="执照上传" min-width="70px">
          <template #default="scope">
            <el-tag :type="scope.row.business_licence_image? 'success':'danger'" size="mini" effect="dark">{{scope.row.business_licence_image? "已传":"未传"}}</el-tag>
          </template>
        </el-table-column>
        <el-table-column align="center" label="操作" show-overflow-tooltip width="80px">
          <template #default="scope">
            <el-button class="tr-button" type="text" plain :icon="ZoomIn" title="详情" @click="onOpenDetailDialog(scope.row)"></el-button>
            <el-button class="tr-button" type="text" plain :icon="Edit" title="编辑" @click="onOpenEditDialog(scope.row)"></el-button>
            <el-button class="tr-button" type="text" plain :icon="Delete" title="删除" @click="onDeleteRow(scope.row)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <!--3.分页导航栏-->
      <el-pagination
          @size-change="onHandlePageSizeChange"
          @current-change="onHandlePageNumChange"
          class="mt15"
          :pager-count="5"
          :page-sizes="[10, 20, 30]"
          v-model:current-page="tableData.param.page_num"
          background
          small
          v-model:page-size="tableData.param.page_size"
          layout="total, sizes, prev, pager, next, jumper"
          :total="tableData.total"
      >
      </el-pagination>
    </el-card>
    <!--4.子组件-->
    <SupplierDetail ref="supplierDetailRef"/>
    <EditSupplier ref="editSupplierRef"/>
    <AddSupplier ref="addSupplierRef"/>
    <AddSupplierContact ref="addContactRef"/>
    <EditSupplierContact ref="editContactRef"/>
    <SupplierContactDetail ref="contactDetailRef"/>
  </div>
</template>
<script lang="ts">

import {computed, onMounted, reactive, ref, toRefs} from "vue";
import {queryPageSuppliers, deleteSupplier, deleteSupplierContact} from '/@/api/supplier/index';
import SupplierDetail from '/@/views/supplier/supplierInfo/component/supplierDetail.vue';
import EditSupplier from '/@/views/supplier/supplierInfo/component/editSupplier.vue';
import AddSupplier from '/@/views/supplier/supplierInfo/component/addSupplier.vue';
import AddSupplierContact from '/@/views/supplier/supplierInfo/component/addSupplierContact.vue';
import EditSupplierContact from '/@/views/supplier/supplierInfo/component/editSupplierContact.vue';
import SupplierContactDetail from '/@/views/supplier/supplierInfo/component/supplierContactDetail.vue';
import {ZoomIn, Edit, Delete,} from '@element-plus/icons-vue';
import {ElMessage, ElMessageBox} from "element-plus";
import { SupplierServiceTypes, getOptionsLabel} from '/@/utils/publicOptionItems'
import moment from "moment";
// import CHNGlobal4LevelLinkJson from '/@/mock/global4LevelLink_CHN.json';
// import GlobalCountry4LevelLinkageJson from '/@/mock/globalCountry4LevelLinkage.json';
import {get4LinkageList}from '/@/utils/globalCountry4LevelLinkage';

// 嵌套表参考 https://blog.csdn.net/qq_34310906/article/details/98962682


export default {
  name: 'supplierSupplierInfo',
  components: {SupplierDetail,EditSupplier,AddSupplier,AddSupplierContact,EditSupplierContact,SupplierContactDetail,},
  setup() {
    const queryText = ref('');
    const supplierDetailRef = ref();
    const editSupplierRef = ref();
    const addSupplierRef = ref();
    const addContactRef= ref();
    const editContactRef= ref();
    const contactDetailRef = ref();
    const state = reactive({
      tableData: {
        data: [] as Array<any>,
        total: 0,
        loading: false,
        param: {
          pageNum: 1,
          pageSize: 10,
        },
      },
      childTable: [],
      global4LevelLink: '',
      global4LevelLinkList: [],
      linkage: {
        country: '',
        province: '',
        city: '',
        district: '',
        countryList: [], // 国家
        provinceList: [], // 省
        cityList: [], // 市
        districtList: [], // 区
      },
    });

    // 供应商状态类型字典
    const tagType:{[key:string]: string} = {
      "新建": "info",
      "启用": "success",
      "禁用": "danger",
    };

    // 营业有效期状态字典
    const effectiveStatus: {[key:string]: string} ={
      "生效中": "success",
      "将失效": "warning",
      "已失效": "danger",
    }

    //获取分页数据
    const getPageData = async (queryText: any, pageNum: number, pageSize: number) => {
      queryPageSuppliers({queryText, pageNum, pageSize}).then((res: any) => {
        // console.log('==res==', res)
        state.tableData.data = res.result_data.data;
        state.tableData.total = res.result_data.count;
      })
    };

    // 初始化表格数据
    const initTableData = () => {
      getPageData(queryText.value, state.tableData.param.pageNum,state.tableData.param.pageSize);
    };

    // 页长改变事件
    const onHandlePageSizeChange = (pageSize: number) => {
      state.tableData.param.pageSize = pageSize;
      state.tableData.param.pageNum = 1;
      let pageNum =1;
      getPageData(queryText.value, pageNum, pageSize)
    };

    // 页码改变事件
    const onHandlePageNumChange = (pageNum: number) => {
      state.tableData.param.pageNum = pageNum;
      let pageSize = state.tableData.param.pageSize;
      getPageData(queryText.value, pageNum, pageSize)
    };

    // 查询事件
    const onHandleQuery = () => {
      let pageNum= state.tableData.param.pageNum;
      let pageSize = state.tableData.param.pageSize;
      getPageData(queryText.value.trim(), pageNum, pageSize)
    };

    // 打开供应商详细情况对话框
    const onOpenDetailDialog = (row: object) => {
      supplierDetailRef.value.openDialog(row);
    };
    // 打开编辑供应商情况对话框
    const onOpenEditDialog = (row: object) => {
      editSupplierRef.value.openDialog(row);
    };

    // 删除供应商
    const onDeleteRow = async (row: any) => {
      ElMessageBox.confirm(`删除账号：${row.account} 的供应商, 是否继续?`, '提示', {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(()=>{
        return deleteSupplier({id: row.id});
      }).then((res) => {
        console.log('==delete res==', res)
        state.tableData.data = [];
        initTableData();
        ElMessage.success('删除成功。');
      })
    };

    // 打开新增供应商对话框
    const onOpenAddDialog = () => {
      addSupplierRef.value.openDialog();
    }

    // 打开新增联系人对话框
    const onOpenAddSupplierContactDialog = (supplierId: number) => {
      addContactRef.value.openDialog(supplierId);
    }

    // 打开编辑联系人对话框
    const onOpenEditSupplierContactDialog = (row: object) => {
      // console.log('==row==', row)
      editContactRef.value.openDialog(row);
    }
    // 打开联系人详情对话框
    const onOpenSupplierContactDetailDialog = (row: object) => {
      // console.log('==row==', row)
      contactDetailRef.value.openDialog(row);
    }

    // 删除联系人
    const onDeleteSupplierContactRow = async (row: any) => {
      ElMessageBox.confirm(`删除姓名为：${row.chn_name} 联系人, 是否继续?`, '提示', {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(() => {
        return deleteSupplierContact({id: row.id});
      }).then((res) => {
        // console.log('==delete res==', res)
        state.tableData.data = [];
        initTableData();
        ElMessage.success('删除成功。');
      })
    };


    // 判断营业执照结束日期是否失效
    const getEffectiveStatus = (end_date: string)=>{
      if (!end_date) return "无日期";
      // 获取并格式化当前日期
      const current_date = moment().format('YYYY-MM-DD')
      // 当前日期与营业执照结束日期天数之差
      const date_diff = moment(end_date).diff(current_date)/(60*60*1000*24)
      if (date_diff < 0) {
        return "已失效";
      }else if (date_diff>0 && date_diff<=30) { // 营业执照1个月之内过期
        return "将失效";
      }else if (date_diff > 30) {
        return "生效中";
      }
    };


    // 初始化国家省市区数据
		const init4LevelLinkData = () => {
			// state.global4LevelLinkList = GlobalCountry4LevelLinkageJson;
      // state.linkage.countryList = GlobalCountry4LevelLinkageJson.filter((item)=> item.levels === 0);
      state.linkage.countryList = get4LinkageList(0)
      // console.log('=====state.linkage.countryList', state.linkage.countryList)
		};

    // 国家下拉事件
		const onCountryChange = (selVal: string) => {
      // // 获取国家的区域编号
      // let obj = state.global4LevelLinkList.find((item)=> item.chn_name===selVal);
      // let areaCode = obj.area_code;
      // state.linkage.provinceList = state.global4LevelLinkList.filter((item)=> item.levels === 1 && item.area_code.includes(areaCode));
			state.linkage.provinceList = get4LinkageList(1, selVal);
      state.linkage.province = '';
			state.linkage.city = '';
			state.linkage.district = '';
			state.linkage.cityList = [];
			state.linkage.districtList = [];
		};

    // 省（洲）下拉事件
    const onProvinceChange = (selVal: any) => {
      // 获取省（洲）的区域编号
      // let obj = state.global4LevelLinkList.find((item)=> item.chn_name===selVal);
      // let areaCode = obj.area_code;
      // state.linkage.cityList = state.global4LevelLinkList.filter((item)=> item.levels === 2 && item.area_code.includes(areaCode));
			state.linkage.cityList = get4LinkageList(2, selVal);
      state.linkage.city = '';
			state.linkage.district = '';
			state.linkage.districtList = [];
    }

    // 市下拉事件
    const onCityChange = (selVal: any) => {
      // 获取市的区域编号
      // let obj = state.global4LevelLinkList.find((item)=> item.chn_name===selVal);
      // let areaCode = obj.area_code;
      // state.linkage.districtList = state.global4LevelLinkList.filter((item)=> item.levels === 3 && item.area_code.includes(areaCode));
      state.linkage.districtList = get4LinkageList(3, selVal);
      state.linkage.district = '';
    }

    // 区（县）下拉事件
    const onDistrictChange = (selVal: any) => {
      // 获取市的区域编号
      console.log('district==', selVal)
    }

    // 钩子函数，获取第1页数据
    onMounted(()=>{
      init4LevelLinkData();
      getPageData(queryText.value, 1, 10);
    });

    return {
      ZoomIn,
      Edit,
      Delete,
      SupplierServiceTypes,
      queryText,
      supplierDetailRef,
      editSupplierRef,
      addSupplierRef,
      addContactRef,
      editContactRef,
      contactDetailRef,
      tagType,
      effectiveStatus,
      GlobalCountry4LevelLinkageJson,
      ...toRefs(state),
      getPageData,
      onHandleQuery,
      onHandlePageSizeChange,
      onHandlePageNumChange,
      onOpenDetailDialog,
      onOpenEditDialog,
      onDeleteRow,
      onOpenAddDialog,
      onOpenAddSupplierContactDialog,
      onOpenEditSupplierContactDialog,
      onOpenSupplierContactDetailDialog,
      onDeleteSupplierContactRow,
      getEffectiveStatus,
      getOptionsLabel,
      init4LevelLinkData,
      onCountryChange,
      onProvinceChange,
      onCityChange,
      onDistrictChange,
    };
  },
};
</script>

<style lang="scss" scoped>
@import "/@/theme/public/eltable.scss";
//@import "/@/theme/public/element-ui-reset.scss";

.query-container{
  margin-bottom: 10px;
}
:deep(.el-tag--small){
    height: 24px;
    line-height: 22px;
}

//:deep(.child-table th.el-table__cell>.cell) {
//  //color: red;
//  background-color: yellowgreen;
//
//}
</style>