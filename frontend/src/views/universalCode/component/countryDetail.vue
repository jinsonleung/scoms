<template>
  <div class="universalCode-airport-container">
    <div v-dialogdrag>
      <el-dialog title="国家详细情况" v-model="isShowDialog" width="800px">
        <el-descriptions
            class="margin-top"
            title=""
            :column="1"
            border
        >
          <el-descriptions-item label-class-name="desc_label">
            <template #label>
              <div class="cell-item">ISO2代码</div>
            </template>
            {{ruleForm.iso2_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">ISO3代码</div>
            </template>
            {{ruleForm.iso3_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">国家/地区全称</div>
            </template>
            {{ruleForm.chn_name}} {{ruleForm.full_eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">首都</div>
            </template>
              {{ruleForm.capital_chn_name}} {{ruleForm.capital_eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">货币代码</div>
            </template>
              {{ruleForm.currency}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">所在洲名称</div>
            </template>
              {{ruleForm.continent.chn_name}} {{ruleForm.continent.eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">使用语言</div>
            </template>
              {{ruleForm.language}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">国际电话区号</div>
            </template>
              {{ruleForm.phone_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">国家描述</div>
            </template>
              {{ruleForm.description}}
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
import CountryFlag from "vue-country-flag-next";

export default {
  name: 'freightToolsCountryDetail',
  components: {CountryFlag},
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
    width: 130px;
  }
</style>