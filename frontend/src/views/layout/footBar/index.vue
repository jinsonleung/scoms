<!--
 * @Author: JinsonLiang
 * @Date: 2021-07-02 17:43:09
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-28 11:10:56
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\views\layout\footBar\index.vue
-->

<template>
  <div class=footer-container>
    <div class = "footer">
      <h5 style="color:gray">Copyright @2021 </h5>
    </div>
    </div>
</template>

<script lang="ts">
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "FootBar",
  setup() {
    const refData = ref(0);
    return {
      refData,
    };
  },
});
</script>
<style lang="scss" scoped>
  .footer-container {
    width: 100%;
    height: 50px;
    background-color: #fff;
    //background-color: rgb(219, 211, 211);
    .footer {
      height: 50px;
      line-height: 50px;
      box-shadow: 0 1px 4px rgb(0 21 41 / 8%);
      position: relative;
      .toggle-btn {
        line-height: 50px;
        height: 100%;
        float: left;
        cursor: pointer;
        transition: background 0.3s;
        :hover {
          background: rgba(0, 0, 0, 0.025);
          display: inline-block;
        }
      }
    }
    .is-active {
      transform: rotate(180deg);
    }
  }
  </style>
