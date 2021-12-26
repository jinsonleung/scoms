<template>
  <div class="top-bar-container">
    <div class="header">
      <!--折叠/展开按钮-->
      <div class="header-left">
        <Icon class="collapse-btn" :icon="isCollapse?'Expand':'Fold'" @click="toggleSidebar"></Icon>
      </div>
      <div class="header-right">
        <div class="header-right-wrap">
          <!--全屏/正常屏切换按钮-->
          <div class="fullscreen-wrap">
            <el-tooltip
                effect="light"
                content="全屏/非全屏"
                placement="bottom"
            >
            <div class="fullscreen-btn">
              <Icon icon="FullScreen" @click="screenFullToggle"></Icon>
            </div>
            </el-tooltip>
          </div>
          <!--消息中心图标-->
          <div class="message-wrap">
            <el-tooltip
                  effect="light"
                  :content="messageCount?`有${messageCount}条未读消息`:`消息中心`"
                  placement="bottom"
              >
              <div class="bell-btn">
              <el-badge :value="messageCount" class="badge-wrap">
                <router-link to="/dashboard">
                  <Icon icon="Bell"></Icon>
                </router-link>
              </el-badge>
                </div>
              </el-tooltip>
          </div>
          <!-- 用户头像 -->
          <div class="avatar-wrap">
            <el-avatar
                :src="avatar"
                size="small"
            ></el-avatar>
          </div>
          <!-- 用户名下拉菜单 -->
          <div class="user-info-wrap">
            <el-dropdown
                class="user-name"
                trigger="click"
                @command="handleCommand"
            >
              <div class="nickName">
                {{ userInfo.nickName }}
                <Icon class="" icon="CaretBottom"></Icon>
              </div>
              <template #dropdown>
                <el-dropdown-menu>
                  <a href="#" arget="_blank">
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
  </div>
</template>

<script lang="ts">
import {ref, toRefs, reactive, computed, defineComponent} from "vue"
import {useStore, mapGetters, mapActions} from "vuex"
import ScreenFull from 'screenfull' //全屏切换

//import avator from '/favicon.ico'
import {ElMessage} from "element-plus"; //信息
import avatar from '@/assets/img/avatar-2.jpg'


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
  width: 100%;
  height: 50px;
  box-sizing: border-box;
  border-bottom: 1px solid #e9e9e9;
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
}

.header-left {
  display: flex;
  height: 100%;
  align-items: center;
  .collapse-btn {
    height: 30px;
    width: 30px;
    cursor: pointer;
  }
}

.header-right {
  display: flex;
  height: 100%;
  padding-right: 0px;
  .header-right-wrap {
    align-items: center;
    display: flex;
    height: 50px;
    align-items: center;
  }
}
.fullscreen-btn, .bell-btn, .avatar-wrap, .user-info-wrap {
  height: 100%;
  display: flex;
  align-items: center;
  cursor: pointer;
  margin: 0px 10px;
}

.badge-wrap{
  margin-top: 6px;
}

.user-info-wrap {
  .nickName {
    height: 100%;
    display: flex;
    align-items: center;
  }
  .el-dropdown svg {
    height: 16px;
    width: 16px;
  }
}

</style>
