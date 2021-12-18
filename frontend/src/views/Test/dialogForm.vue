<template>
  <div>==Element-ui的dialog弹框的拖拽效果(成功！)==</div>
  <el-button type="primary" @click="dialogFormVisible = true">弹出对话框</el-button>

  <!--  <div v-dialog-drag>-->
  <div v-dialogdrag>

    <!--  dialog confirm-->
<!--    <el-dialog v-model="centerDialogVisible" title="Warning" width="30%" center>-->
<!--    <span-->
<!--    >It should be noted that the content will not be aligned in center by-->
<!--      default</span-->
<!--    >-->
<!--      <template #footer>-->
<!--      <span class="dialog-footer">-->
<!--        <el-button @click="centerDialogVisible = false">Cancel</el-button>-->
<!--        <el-button type="primary" @click="centerDialogVisible = false"-->
<!--        >Confirm</el-button-->
<!--        >-->
<!--      </span>-->
<!--      </template>-->
<!--    </el-dialog>-->


    <!-- dialog Form -->
    <el-dialog v-model="dialogFormVisible" title="Shipping address">
      <el-form :model="form">
        <el-form-item label="Promotion name" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Zones" :label-width="formLabelWidth">
          <el-select v-model="form.region" placeholder="Please select a zone">
            <el-option label="Zone No.1" value="shanghai"></el-option>
            <el-option label="Zone No.2" value="beijing"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogFormVisible = false"
        >Confirm</el-button
        >
      </span>
      </template>
    </el-dialog>


  </div>
</template>

<script lang="ts">
import {ref, defineComponent, reactive, toRefs} from "vue";

export default defineComponent({
  name: "App",
  setup() {
    const state = reactive({
      centerDialogVisible: false,
      dialogTableVisible: false,
      dialogFormVisible: false,
      formLabelWidth: '120px',
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: '',
      }
    })


    return {
      ...toRefs(state)
    };
  },
});
</script>
<style></style>