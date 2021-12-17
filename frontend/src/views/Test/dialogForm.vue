<template>
  <div>==Element-ui的dialog弹框的拖拽效果==</div>
  <div>
    <el-dialog>

    </el-dialog>
  </div>
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