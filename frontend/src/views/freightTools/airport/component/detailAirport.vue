<template>
  <div class="freightTools-airport-container">
    <div v-dialogdrag>
      <el-dialog title="机场详细情况" v-model="isShowDialog" width="800px">
        <el-descriptions
            class="margin-top"
            title=""
            :column="1"
            :size="size"
            border
        >
          <el-descriptions-item label-class-name="desc_label">
            <template #label>
              <div class="cell-item">IATA机场代码</div>
            </template>
            {{ruleForm.iata_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">ICAO机场代码</div>
            </template>
            {{ruleForm.icao_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">机场中文名称</div>
            </template>
            {{ruleForm.airport_chn_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">机场英文名称</div>
            </template>
              {{ruleForm.airport_eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">国家/地区代码</div>
            </template>
              {{ruleForm.country_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">国家/地区中文名称</div>
            </template>
              {{ruleForm.country_chn_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">国家/地区英文名称</div>
            </template>
              {{ruleForm.country_eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">城市中文名称</div>
            </template>
              {{ruleForm.city_chn_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">城市英文名称</div>
            </template>
              {{ruleForm.city_eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">机场描述</div>
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
import {reactive, toRefs, ref} from 'vue';

export default {
  name: 'freightToolsDetailAirport',
  setup() {
    // const ruleFormRef = ref(null);
    const state = reactive({
      isShowDialog: false,
      ruleForm: {
        iata_code: '', // IATA机场代码
        icao_code: '', // ICAO机场代码
        airport_chn_name: '', // 机场中文名称
        airport_eng_name: '', // 机场英文名称
        country_code: '', // 国家/地区代码
        country_chn_name: '', // 国家/地区中文名称
        country_eng_name: '', // 国家/地区英文名称
        city_chn_name: '',  // 城市中文名称
        city_eng_name: '', // 城市英文名称
        description: '', // 描述(起)
      },
    });
    // 打开弹窗
    const openDialog = (row: any) => {
      console.log('==openDialog.row1==', row);
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
    width: 150px;
  }
</style>