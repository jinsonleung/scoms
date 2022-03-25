<template>
  <div class="universalCode-airline-container">
    <div v-dialogdrag>
      <el-dialog title="供应商详细情况" v-model="isShowDialog" width="800px">
        <el-descriptions
            class="margin-top"
            title=""
            :column="1"
            border
        >
          <el-descriptions-item label-align="right" class-name="desc" label-class-name="desc_label">
            <template #label><div class="cell-item">供应商账号</div></template>{{ruleForm.account}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">供应商简称</div></template>{{ruleForm.abbreviation_name}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">供应商全称</div></template>{{ruleForm.full_name}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">体系结构</div></template>{{ruleForm.architecture}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">统一社会信用代码</div></template>{{ruleForm.unified_social_credit_code}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">照业执照图片</div></template>{{ruleForm.business_licence_image}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">注册资本</div></template>{{ruleForm.registered_capital}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">注册地址</div></template>{{ruleForm.registered_address}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">成立日期</div></template>{{ruleForm.established_date}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">营业期限(起)</div></template>{{ruleForm.effective_start_date}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">营业期限(止)</div></template>{{ruleForm.effective_end_date}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">办公地址</div></template>{{ruleForm.office_address}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">经营范围</div></template>{{ruleForm.business_scope}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">所在国家</div></template>{{ruleForm.country}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">所在省/洲</div></template>{{ruleForm.province}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">所在城市</div></template>{{ruleForm.city}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">所在区/县</div></template>{{ruleForm.district}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">经营范围</div></template>{{ruleForm.business_scope}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">所在行业</div></template>{{ruleForm.industry}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">企业网站</div></template>{{ruleForm.website}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">法人姓名</div></template>{{ruleForm.legal_person_name}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">法人电话</div></template>{{ruleForm.legal_person_phone}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">法人邮箱</div></template>{{ruleForm.legal_person_email}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">银行对公账户</div></template>{{ruleForm.banking_account_info}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">企业描述</div></template>{{ruleForm.description}}
          </el-descriptions-item>
          <el-descriptions-item label-align="right" label-class-name="desc_label">
            <template #label><div class="cell-item">是否启用</div></template>{{ruleForm.is_available}}
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
  name: 'supplierSupplierInfoSupplierDetail',
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
  //:deep(.desc) {
  //  color: red;
  //  padding:0;
  //  text-align: center;
  //  height: 20px
  //}
  .desc_label {
    width: 140px;
  }
</style>