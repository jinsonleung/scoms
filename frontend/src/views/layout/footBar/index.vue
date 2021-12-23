<template>
  <div class="footer">
    <div class="left">Copyright © 2020-2021. All rights reserved.</div>
    <div class="right">
      <a target="_blank" href="#">OMS V3.0.0</a>
    </div>
  </div>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent ({
  name: 'Footer'
})
</script>

<style lang="scss" scoped>
  .footer {
    height: 50px;
    border-top: 1px solid #e9e9e9;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    background-color: #f0f0f0;
    .left {
      color: #97a8be;
    }
  }
</style>