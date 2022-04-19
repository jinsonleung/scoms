<template>
  <div class="supplier-detail-contact-container">
    <div v-dialogdrag>
      <el-dialog title="供应商详细情况" v-model="isShowDialog" width="800px">
        <el-descriptions
            class="margin-top"
            title=""
            :column="1"
            border
        >
          <el-descriptions-item label-align="right" class-name="desc" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">部门名称</div>
            </template>
            {{ ruleForm.department }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">职位</div>
            </template>
            {{ ruleForm.title }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">中文名</div>
            </template>
            {{ ruleForm.chn_name }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">英文名</div>
            </template>
            {{ ruleForm.eng_name }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">电话</div>
            </template>
            {{ ruleForm.tel }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">手机</div>
            </template>
            {{ ruleForm.phone }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">邮箱</div>
            </template>
            {{ ruleForm.email }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">微信号</div>
            </template>
            {{ ruleForm.wechat }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">QQ号</div>
            </template>
            {{ ruleForm.qq }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">其他社交账号</div>
            </template>
            {{ ruleForm.social_account }}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label>
              <div class="cell-item">备注</div>
            </template>
            {{ ruleForm.remark }}
          </el-descriptions-item>
        </el-descriptions>
        <template #footer>
					<span class="dialog-footer">
						<el-button @click="onCancel" size="small">取消</el-button>
					</span>
        </template>
      </el-dialog>
    </div>
  </div>
</template>

<script lang="ts">
import {reactive, toRefs} from 'vue';

export default {
  name: 'SupplierContactDetail',
  setup() {
    const state = reactive({
      isShowDialog: false,
      ruleForm: {}
    })
    const openDialog = (row: any) => {
      state.ruleForm = row;
      state.isShowDialog = true;
    };
    // 关闭弹窗
    const closeDialog = () => {
      state.isShowDialog = false;
    };
    // 取消
    const onCancel = () => {
      closeDialog();
    };

    return {
      openDialog,
      closeDialog,
      onCancel,
      ...toRefs(state),
    };
  },
};
</script>
<style lang="scss">
.desc_label {
  width: 120px;
}
</style>