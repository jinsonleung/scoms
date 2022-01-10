/**
 * 状态管理--系统配置（刷新页面会消失，要兼容浏览器需要本地存一份）
 * @description 系统配置相关的数据全部存于该文件
 * @Author Jinson.Liang
 * @Date 2021-10-8
 */

const homeItem = [{    // 首页条目
    name: 'Home',
    path: '/home',
    title: '首页'
}]

const system = {
    state: { // 系统配置状态
        tagsList: [],   //菜单标签名称列表，用于菜单标签栏
        collapse: false,    //左边菜单是否折叠
    },
    getters: {  //获取State中的isCollcapse值
        collapse: (state: any) => {
            return state.collapse
        },
    },
    mutations: { //同步修改状态
        // 删除标签页
        delTagsItem(state, data) {
            state.tagsList.splice(data.index, 1);
        },
        // 新增标签页
        setTagsItem(state, data) {
            state.tagsList.push(data)
        },
        // 关闭所有（首页不可关闭）
        clearTags(state) {
            state.tagsList = [...homeItem]
        },
        // 关闭其他（首页不可关闭）
        closeTagsOther(state, data) {
            state.tagsList = [...homeItem]
            if (data[0].path !== homeItem[0].path) {
                state.tagsList.push(data[0])
            }
        },
        // 关闭当前标签页
        closeCurrentTag(state, data) {
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
        hadndleCollapse(state, data) {
            state.collapse = data;
            // sessionStorage['collapse'] = data;
        }
    },
    actions: {  //通过mutaitons异步修改状态

    }
}
export default system
