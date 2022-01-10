<template>
    <div>
        <div class="project-header">
            <el-row>
                <el-col :span="7"></el-col>
                <el-col :span="7">
                    <el-input
                        size="medium"
                        class="project-input"
                        v-model="listQuery.goodsName"
                        clearable
                        @keyup.enter="searchFn(listQuery)"
                        placeholder="请输入商品名称搜索">
                    </el-input>
                </el-col>
                <el-button type="primary" size="medium" @click="searchFn(listQuery)"
                    >查 询</el-button>
                <el-button type="primary" size="medium" @click="addData">新 建</el-button>
            </el-row>
        </div>
        <el-table v-loading="loading" :data="tableList" align="center" class="table-box">
            <el-table-column align="center" label="商品名称" prop="goodsName"> </el-table-column>
            <el-table-column align="center" label="商品英文名称" prop="englishName">
            </el-table-column>
            <el-table-column align="center" label="商品简称" prop="shortName"> </el-table-column>
            <el-table-column align="center" label="商品描述" prop="goodsDesc"> </el-table-column>
            <el-table-column align="center" label="商品品牌" prop="goodsBrand"> </el-table-column>
            <el-table-column align="center" label="商品规格" prop="goodsSpec"> </el-table-column>
            <!-- 操作列 -->
            <el-table-column label="操作" align="center">
                <template v-slot="scope">
                    <el-button type="text" icon="el-icon-remove" @click="handleDelete(scope.row.id)"
                        >删除</el-button
                    >
                    <el-button type="text" icon="el-icon-edit" @click="handleEdit(scope.row)"
                        >编辑</el-button
                    >
                </template>
            </el-table-column>
        </el-table>
        <div class="page-footer-box">
            <el-pagination
                class="text-right"
                background
                @current-change="pageChange"
                layout="prev, pager, next"
                :pageTotal="pageTotal"
                :current-page="pageNo">
            </el-pagination>
        </div>
        <edit-dialog
            ref="editDialogRef"
            :status="status"
            @handleCloseDialog="handleCloseDialog"
            @getDataList="getDataList"
            :formData="formData"
            v-model="visible">
        </edit-dialog>
    </div>
</template>
<script lang="ts">
import { getList, deleteItem, addItem, updateItem } from '@/api/goods/goodsListApi'
import { defineComponent, onMounted, ref, reactive } from 'vue'
import { ElMessage } from 'element-plus'
import { ListQuery, TableList, DataList } from '@/type/goods/index'
import EditDialog from './EditDialog.vue'
import { ListClass } from '@/components/goods/goods'

export default defineComponent({
    name: 'goodlist',
    components: {
        EditDialog,
    },
    props: {
        msg: {
            required: true,
            default: () => '',
            type: String,
        },
    },
    setup(props) {
        const status = ref(false)
        const formData = reactive<TableList>({
            id: '',
            goodsName: '',
            englishName: '',
            shortName: '',
            goodsDesc: '',
            goodsBrand: '',
            goodsSpec: '',
        })
        const visible = ref(false)
        const addData = () => {
            visible.value = true
            status.value = false
            formData.id = ''
            formData.goodsName = ''
            formData.englishName = ''
            formData.shortName = ''
            formData.goodsDesc = ''
            formData.goodsBrand = ''
            formData.goodsSpec = ''
        }
        const handleEdit = (row: TableList) => {
            visible.value = true
            status.value = true
            formData.id = row.id
            formData.goodsName = row.goodsName
            formData.englishName = row.englishName
            formData.shortName = row.shortName
            formData.goodsDesc = row.goodsDesc
            formData.goodsBrand = row.goodsBrand
            formData.goodsSpec = row.goodsSpec
        }
        const handleCloseDialog = () => {
            formData.id = ''
            formData.goodsName = ''
            formData.englishName = ''
            formData.shortName = ''
            formData.goodsDesc = ''
            formData.goodsBrand = ''
            formData.goodsSpec = ''
            visible.value = false
        }
        // const pageNo = ref<number>(1)
        // const loading = ref<boolean>(false)
        // const pageTotal = ref<number>(1)
        // const tableList = ref<TableList[]>([
        //     {
        //         id: '',
        //         goodsName: '',
        //         englishName: '',
        //         shortName: '',
        //         goodsDesc: '',
        //         goodsbrand: '',
        //         goodsSpec: '',
        //     },
        // ])
        const listQuery = reactive<ListQuery>({
            pageNo: 1, // 当前页码
            pageSize: 10, // 单页显示数量
            goodsName: '', // 项目名称
        })
        class TableClass extends ListClass { }
        // 列表类
        const {
            searchFn,
            getDataList,
            pageNo,
            pageSize,
            pageChange,
            loading,
            tableList,
            pageTotal,
        } = new TableClass({
            Api: {
                listApi: getList,
            }
        })

        // const getDataList = () => {
        //     getList<DataList>(listQuery)
        //         .then((res) => {
        //             tableList.value = res.data.list
        //             pageTotal.value = res.data.totalCount
        //         })
        //         .finally(() => {
        //             loading.value = false
        //         })
        // }
        const handleDelete = (val: string) => {
            deleteItem<DataList>({ id: val }).then(() => {
                ElMessage.success({
                    message: '删除成功',
                    type: 'success',
                })
                getDataList()
            })
        }
        onMounted(() => {
            loading: true
            console.log(props.msg, 444)
            getDataList()
        })
        // const searchFn = () => {
        //     getDataList()
        // }
        // const pageChange = (val: number) => {
        //     listQuery.pageNo = val
        //     getDataList()
        // }

        return {
            status,
            visible,
            pageNo,
            pageSize,
            tableList,
            formData,
            listQuery,
            getDataList,
            pageChange,
            searchFn,
            loading,
            pageTotal,
            handleDelete,
            handleEdit,
            handleCloseDialog,
            addData,
        }
    },
})
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
