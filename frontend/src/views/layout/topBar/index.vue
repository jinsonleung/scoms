<template>
  <div class="top-bar-container">
    <div class="header">
      <!--切换折叠/展开-->
      <div class="header-left" @click="toggleSidebar">
        <Icon class="header-icon" :icon="isCollapse?'Expand':'Fold'"></Icon>
      </div>
      <div class="header-right">
        <div class="header-right-user">
          <!--全屏/正常屏切换图标-->
          <el-tooltip
              effect="light"
              content="全屏/非全屏"
              placement="bottom"
          >
          <span class="header-icon" @click="screenFullToggle">
            <Icon icon="FullScreen"></Icon>
          </span>
          </el-tooltip>
          <!--消息中心图标-->
          <el-badge :value="messageCount" class="item">
            <el-tooltip
                effect="light"
                :content="messageCount?`有${messageCount}条未读消息`:`消息中心`"
                placement="bottom"
            >
              <router-link to="/dashboard">
                <Icon icon="Bell" style="width: 20px; height: 20px; margin-left: 20px"></Icon>
              </router-link>
            </el-tooltip>
          </el-badge>
          <!-- 用户头像 -->
          <el-avatar
              class="user-avator"
              :src="avatar"
              size="small"
              style="margin-left: 20px; overflow: auto"
          ></el-avatar>
          <!-- 用户名下拉菜单 -->
          <el-dropdown
              class="user-name"
              trigger="click"
              @command="handleCommand"
          >
            <span class="header-left" @click="">
              {{ userInfo.nickName }}
              <Icon class="" icon="CaretBottom"></Icon>
            </span>
            <template #dropdown>
              <el-dropdown-menu>
                <a
                    href="#"
                    target="_blank"
                >
                  <el-dropdown-item>项目仓库</el-dropdown-item>
                </a>
                <el-dropdown-item
                    divided
                    command="loginout"
                >
                  退出登录
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {ref, toRefs, reactive, computed, defineComponent} from "vue"
import {useStore, mapGetters, mapActions} from "vuex"
import ScreenFull from 'screenfull' //全屏切换

//import avator from '/favicon.ico'
import {ElMessage} from "element-plus"; //信息
import avatar from '@/assets/img/avatar-1.jpeg'


export default defineComponent({
  name: "index",
  computed: {
    ...mapGetters(["isCollapse"]), // 语法糖
  },
  setup(props: any, context: any) {
    const state = reactive({
      name: 'aaa',
      userInfo: null,
      hasBack: false,
      fullscreen: false,
      messageCount: 2,
    })

    const userInfo = reactive({
      headimg: avatar,
      nickName: 'Jinson'
    })

    // 全屏/非全屏切换
    const screenFullToggle = () => {
      ScreenFull.toggle()
          .then(() => {
          })
          .catch(() => {
            ElMessage ({
              showClose: true,
              message: "你的浏览器不支持全屏！",
              type: "warning"
            });
          });
    }
    const store = useStore()
    // const isCollapse = computed(() => store.getters.isCollapse); //getters
    const toggleSidebar = () => { //isCollapse状态
      store.dispatch("toggleSidebar", '折叠/展开') //actions, 第2个参数可以是随便字符串
      // iconName.value = isCollapse.value? 'Expand': 'Fold' //切换折叠/展开图标
    }

    const logout = () => {
      // axios.delete('/logout').then(() => {
      //   localRemove('token')
      //   window.location.reload()
      // })
    }
    const back = () => {
      // router.back()
    }

    const handleCommand = async (command: any) => {
      // if (command === 'loginout') {
      // 	const res = await store.dispatch('user/logout', {})
      // 	if (res){
      // 		router.push('/login');
      // 	}
      // }
    }
    return {
      avatar,
      screenFullToggle,
      ...toRefs(state),
      toggleSidebar,
      userInfo,
      logout,
      back,
      handleCommand,
    };
  },
});









</script>

<style lang="scss" scoped>
.top-bar-container {

}

.header {
  height: 50px;
  border-bottom: 1px solid #e9e9e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;

  .header-icon {
    cursor: pointer;
  }
}

.header-left {
  display: flex;
  height: 100%;
  align-items: center;
  .header-icon {
    height: 30px;
    width: 30px;
    cursor: pointer;
  }
}

.header-right {
  display: flex;
  height: 100%;

  .header-right-user {
    display: flex;
    align-items: center;

    .user-avator {
      margin: 0px 20px;
    }
  }
}

</style>
