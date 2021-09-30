<template>
    <!-- 弹窗 -->
    <el-dialog
        width="500px"
        :title="attrs.status ? '修改' : '新增'"
        :before-close="handleCloseDialog">
        <el-form
            size="mini"
            :model="attrs.formData"
            :rules="rules"
            label-width="120px"
            ref="ruleForm"
            style="padding: 0 20px">
            <el-form-item :title="'商品名称'" :label="'商品名称'" prop="goodsName">
                <el-input
                    v-model="attrs.formData.goodsName"
                    :placeholder="'请输入商品名称'"
                ></el-input>
            </el-form-item>
            <el-form-item :title="'商品ID'" :label="'商品ID'" prop="id">
                <el-input v-model="attrs.formData.id" :placeholder="'请输入商品名称'"></el-input>
            </el-form-item>
            <el-form-item :title="'商品英文名称'" :label="'商品英文名称'" prop="englishName">
                <el-input
                    v-model="attrs.formData.englishName"
                    :placeholder="'请输入商品英文名称'"
                ></el-input>
            </el-form-item>
            <el-form-item :title="'商品简称'" :label="'商品简称'" prop="shortName">
                <el-input
                    v-model="attrs.formData.shortName"
                    :placeholder="'请输入商品简称'"
                ></el-input>
            </el-form-item>
            <el-form-item :title="'商品描述'" :label="'商品描述'" prop="goodsDesc">
                <el-input
                    v-model="attrs.formData.goodsDesc"
                    :placeholder="'请输入商品描述'"
                ></el-input>
            </el-form-item>
            <el-form-item :title="'商品品牌'" :label="'商品品牌'" prop="goodsbrand">
                <el-input
                    v-model="attrs.formData.goodsbrand"
                    :placeholder="'请输入商品品牌'"
                ></el-input>
            </el-form-item>
            <el-form-item :title="'商品规格'" :label="'商品规格'" prop="goodsSpec">
                <el-input
                    v-model="attrs.formData.goodsSpec"
                    :placeholder="'请输入商品规格'"
                ></el-input>
            </el-form-item>
        </el-form>
        <template #footer>
            <span class="dialog-footer">
                <el-button size="mini" @click="handleCloseDialog">取 消</el-button>
                <el-button type="primary" size="mini" @click="submitDialog">确 定</el-button>
            </span>
        </template>
    </el-dialog>
</template>
<script lang="ts">
import { ListQuery, TableList, DataList } from '@/type/goods/index'
import { defineComponent, computed, ref, reactive } from 'vue'
import { getList, deleteItem, addItem, updateItem } from '@/api/goods/goodsListApi'
import { ElMessage } from 'element-plus'
export default defineComponent({
    emits: ['handleCloseDialog', 'getDataList'],
    setup(props, context) {
        const ruleForm = ref<any>(null)
        const attrs: any = computed(() => {
            return context.attrs
        })
        // 提交表单
        const submitDialog = () => {
            ruleForm.value.validate((valid: boolean) => {
                if (!valid) return false
                if (attrs.status) {
                    updateData(attrs.formData)
                    context.emit('handleCloseDialog')
                } else {
                    context.emit('handleCloseDialog')
                    handleAdd(attrs.formData)
                }
            })
        }
        const rules = {
            id: [{ required: true, message: '请输入商品id', trigger: 'blur' }],
            goodsName: [{ required: true, message: '请输入商品名称', trigger: 'blur' }],
            englishName: [{ required: true, message: '请输入商品英文名称', trigger: 'blur' }],
            shortName: [{ required: true, message: '请输入商品简称', trigger: 'blur' }],
            goodsDesc: [{ required: true, message: '请输入商品描述', trigger: 'blur' }],
            goodsbrand: [{ required: true, message: '请输入商品品牌', trigger: 'blur' }],
            goodsSpec: [{ required: true, message: '请输入商品规格', trigger: 'blur' }],
        }
        const handleCloseDialog = () => {
            ruleForm.value.clearValidate()
            context.emit('handleCloseDialog')
        }
        const handleAdd = (val: TableList) => {
            addItem<DataList>(val).then(() => {
                ElMessage.success({
                    message: '添加成功',
                    type: 'success',
                })
                context.emit('getDataList')
            })
        }
        const updateData = (val: TableList) => {
            updateItem<DataList>(val).then(() => {
                ElMessage.success({
                    message: '修改成功',
                    type: 'success',
                })
                context.emit('getDataList')
            })
        }
        return {
            attrs,
            handleCloseDialog,
            ruleForm,
            submitDialog,
            updateData,
            rules,
            handleAdd,
        }
    },
})
</script>