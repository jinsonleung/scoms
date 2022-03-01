<template>
  <div class="freightTools-airline-container">
    <div v-dialogdrag>
      <el-dialog title="航空公司详细情况" v-model="isShowDialog" width="800px">
        <el-descriptions
            class="margin-top"
            title=""
            :column="1"
            border
        >
          <el-descriptions-item label-class-name="desc_label">
            <template #label>
              <div class="cell-item">IATA代码</div>
            </template>
            {{ruleForm.iata_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">ICAO代码</div>
            </template>
            {{ruleForm.icao_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">航空公司名称</div>
            </template>
            {{ruleForm.chn_name}}，{{ruleForm.eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">国家/地区代码</div>
            </template>
              {{ruleForm.country.iso2_code}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">国家/地区名称</div>
            </template>
              {{ruleForm.country.chn_name}}，{{ruleForm.country.eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">城市名称</div>
            </template>
              {{ruleForm.city.chn_name}}，{{ruleForm.city.eng_name}}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">航空公司描述</div>
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

export default {
  name: 'freightToolsDetailAirline',
  setup() {
    // const ruleFormRef = ref(null);
    const state = reactive({
      isShowDialog: false,
      ruleForm: {}
    })
    // const state1 = reactive({
    //   isShowDialog: false,
    //   ruleForm: {
    //     iata_code: '', // IATA机场代码
    //     icao_code: '', // ICAO机场代码
    //     chn_name: '', // 机场中文名称
    //     eng_name: '', // 机场英文名称
    //     country:{
    //       iso2_code: '', // 国家二字代码
    //       chn_name: '', // 国家中文名称
    //       eng_name: '', // 国家英文名称
    //     },
    //     city_chn_name: '',  // 城市中文名称
    //     city_eng_name: '', // 城市英文名称
    //     elevation: '', // 海拨高度
    //     longitude: '', // 经度
    //     latitude: '', // 纬度
    //     time_zone: '', // 时区
    //     utc: '', // UTC时差
    //     description: '', // 机场描述
    //   },
    // });
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
    width: 130px;
  }
</style>