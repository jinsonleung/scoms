<template>
  <div class="universalCode-Airport-container">
    <el-table
        :data="tableData"
        style="width: 100%; margin-bottom: 20px"
        row-key="id"
        border
    >
      <el-table-column prop="date" label="date" sortable width="180"/>
      <el-table-column prop="name" label="Name" sortable width="180"/>
    </el-table>
  </div>
</template>
<script lang="ts">

import {} from "vue";

interface User {
  id: number
  date: string
  name: string
  hasChildren?: boolean
  children?: User[]
}

// 嵌套表参考 https://blog.csdn.net/qq_34310906/article/details/98962682


export default {
  name: 'supplierSupplierInfo',
  components: {},
  setup() {
    const tableData: User[] = [
      {
        id: 1,
        date: '2016-05-02',
        name: 'wangxiaohu',
      },
      {
        id: 2,
        date: '2016-05-04',
        name: 'wangxiaohu',
      },
      {
        id: 3,
        date: '2016-05-01',
        name: 'wangxiaohu',
        children: [
          {
            id: 31,
            date: '2016-05-01',
            name: 'wangxiaohu',
          },
          {
            id: 32,
            date: '2016-05-01',
            name: 'wangxiaohu',
          },
        ],
      },
      {
        id: 4,
        date: '2016-05-03',
        name: 'wangxiaohu',
      },
    ]

    return {
      tableData,
    };
  },
};
</script>
<style lang="scss" scoped>

</style>