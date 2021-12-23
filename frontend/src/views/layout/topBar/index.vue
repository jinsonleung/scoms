<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-21 14:38:38
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-28 11:05:07
 * @Description:
 * @FilePath: \vue3-vite-ssis\src\views\layout\topBar\index1.vue
-->
<template>
  <div class="top-bar-container">
    <div class="header">
      <!--切换折叠/展开-->
      <div class="left">
        <Icon class="collapse-icon" :icon="isCollapse?'Expand':'Fold'" @click="toggleSidebar"></Icon>
      </div>
      <div class="right">
        <div class="header-user-con">
          <!-- 消息中心 -->
          <div class="btn-bell">
            <el-tooltip
                effect="dark"
                :content="message?`有${message}条未读消息`:`消息中心`"
                placement="bottom"
            >
              <router-link to="/">
                <i class="el-icon-bell"/>
              </router-link>
            </el-tooltip>
            <span
                v-if="message"
                class="btn-bell-badge"
            />
          </div>
          <!-- 用户头像 -->
          <div class="user-avator" style="height: 16px; width: 16px; overflow: auto" >
             <img :src="avator">
          </div>
          <!-- 用户名下拉菜单 -->
          <el-dropdown
              class="user-name"
              trigger="click"
              @command="handleCommand"
          >
					<span class="el-dropdown-link">
						{{ userInfo.nickName }}
						<i class="el-icon-caret-bottom"/>
					</span>
            <template #dropdown>
              <el-dropdown-menu>
                <a
                    href="https://github.com/lss5270/vue-manage-system-plus"
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
import {ref, toRefs, reactive, computed, defineComponent} from "vue";
import {useStore, mapGetters, mapActions} from "vuex";
import avator from '/favicon.ico'

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
      message: 2,
    })

    const userInfo =reactive({
      headimg: avator,
      nickName: 'Jinson'
    })

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

    const handleCommand = async (command:any) => {
			// if (command === 'loginout') {
			// 	const res = await store.dispatch('user/logout', {})
			// 	if (res){
			// 		router.push('/login');
			// 	}
			// }
		}
    return {
      avator,
      ...toRefs(state),
      toggleSidebar,
      userInfo,
      // ...mapActions(['toggleSidebar']) // 语法糖
      logout,
      back,
      handleCommand,
    };
  },
});
</script>

<style scoped>
.top-bar-container {

}

.header {
  height: 50px;
  border-bottom: 1px solid #e9e9e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
  /*background-color: #d8ffec;*/
}

.el-icon-back {
  border: 1px solid #e9e9e9;
  padding: 4px;
  border-radius: 50px;
  margin-right: 10px;
}

.left .collapse-icon {
  height: 20px;
  width: 20px;
}

.right > div > .icon {
  font-size: 18px;
  margin-right: 6px;
}

.header-user-con {
  display: flex;
  height: 70px;
  align-items: center;
}

.user-avator {
    margin-left: 20px;
	margin-right: 5px;
}

.btn-bell

.btn-bell .el-icon-bell {
    color: #fff;
}

.btn-bell-badge {
    position: absolute;
    right: 0;
    top: -2px;
    width: 8px;
    height: 8px;
    border-radius: 4px;
    background: #f56c6c;
    color: #fff;
}


.author {
  margin-left: 10px;
  cursor: pointer;
}
</style>
<style>
.popper-user-box {
  background: url('https://s.yezgea02.com/lingling-h5/static/account-banner-bg.png') 50% 50% no-repeat !important;
  background-size: cover !important;
  border-radius: 0 !important;
}

.popper-user-box .nickname {
  position: relative;
  color: #ffffff;
}

.popper-user-box .nickname .logout {
  position: absolute;
  right: 0;
  top: 0;
  cursor: pointer;
}
</style>