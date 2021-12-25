<template>

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
      message: 2,
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
      // ...mapActions(['toggleSidebar']) // 语法糖
      logout,
      back,
      handleCommand,
    };
  },
});

</script>

<style scoped>

</style>