<template>
  <div class="tags" v-if="showTags">
    <ul>
      <li class="tags-li" v-for="(item,index) in tagsList" :class="{'active': isActive(item.path)}" :key="index">
        <router-link :to="item.path" class="tags-li-title">{{ item.title }}</router-link>
        <span class="tags-li-icon" @click="closeTags(index)">
                  <Icon icon="Close" style=""></Icon>
                </span>
      </li>
    </ul>
    <div class="tags-close-box">
      <el-dropdown @command="handleTags">
        <el-button size="mini" type="default">
          标签选项
          <i class="el-icon-arrow-down el-icon--right"></i>
        </el-button>
        <template #dropdown>
          <el-dropdown-menu size="small">
            <el-dropdown-item command="other">关闭其他</el-dropdown-item>
            <el-dropdown-item command="all">关闭所有</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script lang="ts">
import {ref, computed, defineComponent, watch, onBeforeMount,} from "vue"
import {useStore} from "vuex"
import {onBeforeRouteUpdate, useRoute, useRouter} from "vue-router"


export default defineComponent({
  name: "TopTags",
  setup(props,context) {
    const route = useRoute()
    const store = useStore()
    // 当前路由全称，如'/home'
    const isActive = (path:any) => { return path === route.fullPath }
    // ====计算属性，返回响应式对象===
    // tagsList：获取标签栏列表信息
    const tagsList = computed(()=>{
      return store.state.system.tagsList
    })
    //showTags：判断tagsList是否为空
    const showTags = computed(()=>{
      // console.log('==store.state.system.tagsList.length==', store.state.system.tagsList.length)
      // return store.state.system.tagsList.length>0
    })

    // ===监听路由变化===
    onBeforeRouteUpdate((to)=>{
      //setTags(to)
      console.log('==onBeforeRouteUpdate==', to)
    })

    //===onBeforeMount：hooks函数，创建实例后被立即调用===
    onBeforeMount(()=>{
      console.log('==topTags/index.vue onBeforeMount==', route.name,route.fullPath)
      setTags(route) // route.fullPath是返回当前路由对象
    })


    // ===方法===
    // setTags: 保存路由到状态中
    const setTags = (route:any)=>{
      // tagsList是否存在当前路由
      const isExistFullPath = true
      // const isExistFullPath =  tagsList.value.some((item:any)=>{ return item.fullPath === route.fullPath })
      // const isExistFullPath =  tagsList.value((item:any)=>{ return item.fullPath === route.fullPath })
      if(!isExistFullPath) {
        //当前路由超过10个时，将删除第1个路由，第0个路由为首页路由不删除
        if (tagsList.value.length>=10) {
          //删除tagsList中的第1个路由
          store.commit('system/delTagsItem',{index:1})
        }
        //保存当前路由
        // store.state.system.commit('system/setTagsItem', {
        //   name: route.name,
        //   fullPath: route.fullPath,
        //   title: route.meta.title,
        // })
      }
    }



    return{
      isActive,
      tagsList,
      showTags,
    }



  }
});
</script>

<style lang="scss">
.tags {
  position: relative;
  height: 30px;
  overflow: hidden;
  background: #fff;
  /*background-color: #1BAEAE;*/
  padding-right: 120px;
  box-shadow: 0 5px 10px #ddd;
}

.tags ul {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.tags-li {
  float: left;
  margin: 3px 5px 2px 3px;
  border-radius: 3px;
  font-size: 12px;
  overflow: hidden;
  cursor: pointer;
  height: 23px;
  line-height: 23px;
  border: 1px solid #e9eaec;
  background: #fff;
  padding: 0 5px 0 12px;
  vertical-align: middle;
  color: #666;
  -webkit-transition: all 0.3s ease-in;
  -moz-transition: all 0.3s ease-in;
  transition: all 0.3s ease-in;

  svg {
    width: 12px;
    height: 12px;
    //padding-top:5px
    margin-top: 5px;
  }
}

.tags-li:not(.active):hover {
  background-color: #c9ffd3;
}

.tags-li.active {
  background-color: #409eff;
  color: #fff;

  svg {
    color: #fff;
  }
}

.tags-li-title {
  float: left;
  max-width: 80px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin-right: 5px;
  color: #666;
}

.tags-li.active .tags-li-title {
  color: #fff;

}

.tags-close-box {
  position: absolute;
  right: 0;
  top: 0;
  box-sizing: border-box;
  padding-top: 1px;
  text-align: center;
  width: 90px;
  height: 30px;
  box-shadow: -3px 0 15px 3px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

svg {


}
</style>


