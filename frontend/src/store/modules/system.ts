/**
 * 状态管理--系统配置（刷新页面会消失，要兼容浏览器需要本地存一份）
 * @description 系统配置相关的数据全部存于该文件
 * @Author Jinson.Liang
 * @Date 2021-10-8
 */

import { Module } from 'vuex'
import  { UserInfosState, RootStateTypes } from "@/store/interface/index"

const homeItem = [{    // 首页条目
    name: 'Home',
    fullPath: '/home',
    title: '首页'
}]

const system:Module<UserInfosState, RootStateTypes> = {
    // namespace:true,
    state: { // 系统配置状态
        tagsList: [],   //菜单标签名称列表，用于菜单标签栏
        collapse: false,    //左边菜单是否折叠
    },
    getters: {  //获取State中的isCollcapse值
        collapse: (state: any) => {
            return state.collapse
        },
    },
    //同步修改状态
    mutations: {
        // 删除标签页
        delTagsItem(state: any, data: any) {
           console.log('==delTagsItem==', data)
            state.tagsList.splice(data.index, 1);
        },
        // 新增标签页
        setTagsItem(state: any, data: any) {
            console.log('==setTagsItem==', data)
            state.tagsList.push(data)
        },
        // 关闭所有（首页不可关闭）
        clearTags(state: any) {
            state.tagsList = [...homeItem]
        },
        // 关闭其他（首页不可关闭）
        closeTagsOther(state: any, data: any) {
            state.tagsList = [...homeItem]
            if (data[0].path !== homeItem[0].fullPath) {
                state.tagsList.push(data[0])
            }
        },
        // 关闭当前标签页
        closeCurrentTag(state: any, data: any) {
            for (let i = 0, len = state.tagsList.length; i < len; i++) {
                const item = state.tagsList[i];
                if (item.path === data.$route.fullPath) {
                    if (i < len - 1) {
                        data.$router.push(state.tagsList[i + 1].path);
                    } else if (i > 0) {
                        data.$router.push(state.tagsList[i - 1].path);
                    } else {
                        data.$router.push('/');
                    }
                    state.tagsList.splice(i, 1);
                    break;
                }
            }
        },
        // 侧边栏折叠
        hadndleCollapse(state: any, data: any) {
            state.collapse = data;
            // sessionStorage['collapse'] = data;
        },
        TOGGLE_SIDEBAR(state:any){  //左边菜单栏展开与折叠
            state.collapse = !state.collapse
        },

    },
    //通过mutaitons异步修改状态
    actions: {
        toggleSidebar(context: any, e: any) {
            console.log('>>>接受的值', e)  //接受的值
            context.commit('TOGGLE_SIDEBAR')
        },
        countAdd(context: any) {
            context.commit('COUNT_ADD')
        },
        countDel(context: any) {
            context.commit('COUNT_DEL')
        }
    }
}
export default system
