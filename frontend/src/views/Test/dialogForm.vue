<template>
  <div>==Element-ui的dialog弹框的拖拽效果==</div>
  <el-dialog
      @close="resObjdia(index)"
      :close-on-press-escape="false"
      :close-on-click-modal="false"
      v-dialogDrag
      class="resObj"
      title="返回参数详情"
      :visible.sync="resObjdialog"
      width="40%">
    <pre class="pre" v-for="(i,index) in resObject" :key="index" v-show="indexBeforetableData == index">{{ i }}</pre>
    <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="resObjdialog = false">确 定</el-button>
      </span>
  </el-dialog>
</template>

<script lang="ts">
import {ref, defineComponent, reactive} from "vue";

export default defineComponent({
  name: "App",
  setup() {
    const indexBeforetableData = ref(0)
    const resObject = reactive({})
    const resObjdia = () => {
      return
    }

    const resObjdialog = () => {
      return
    }


    return {
      indexBeforetableData,
      resObject,
      resObjdia,
      resObjdialog,
    };
  },
});
</script>
<style></style>