<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-30 11:28:04
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-30 17:32:32
 * @Description:
 * @FilePath: \vue3-vite-ssis\src\components\goods\List.vue
-->
<template>
    <div>
        <h1>==table data list==</h1>
        <button @click="getListData">get data</button>
        <button @click="getListData2">get data2</button>
        <ul>
            <li v-for="item in tableData" :key="item.id">{{item.name}}</li>
        </ul>
    </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive } from "vue";
// import { ElMessage } from 'element-plus'
import EditDialog from "./EditDialog.vue";
import "@/mock/mockServer";
import http from "@/utils/http2/index";
import { TableList } from '@/type/goods/index'

export default defineComponent({
  name: "goodlist",
  components: {
    EditDialog,
  },
  props: {},
  setup(props) {
    const status = ref(false);
    const state = reactive({
        catName: [],
        formData: [],
        tableData: [{
          id: '12987125',
          name: '王小虎',
          amount1: '621',
          amount2: '2.2',
          amount3: 17
        }, {
          id: '12987126',
          name: '王小虎',
          amount1: '539',
          amount2: '4.1',
          amount3: 15
        }]
    })
    const formData1 = reactive<TableList>({
        id: '',
        goodsName: '',
        englishName: '',
        shortName: '',
        goodsDesc: '',
        goodsBrand: '',
        goodsSpec: '',
    })

    onMounted(() => {
        //state.catName =
        getListData()
    });

    const getListData = () => {
        http.get("/getlistdata").then((res: any) => {

          state.formData = res.data.data.list
          console.log("type1:", typeof(res.data.data.list))
        console.log("res.data>>>", res.data);
        console.log("formData>>>", state.formData);
      });
    };

    const getListData2 =()=>{
          console.log("type2:", typeof( state.tableData))

        console.log("tableData>>>", state.tableData);
        console.log("formData>>>", state.formData);
    }

    return {
      getListData,
      getListData2,
      ...state,
    };
  },
});
</script>
<style scoped>
.table-box {
  height: 640px;
  overflow: auto;
}
.page-footer-box {
  text-align: right;
  margin-top: 15px;
}
</style>
