import { Module } from 'vuex'
import { Session } from "@/utils/store"
import  { UserInfosState, RootStateTypes } from "@/store/interface/index"

// 用户信息全局状态
const userInfosModule: Module<UserInfosState, RootStateTypes> = {
    namespaced: true,
    state: {
        userInfos: {}
    },
    mutations: {
        // 设置用户信息
        setUserInfos (state: any,data: object) {
            state.userInfos = data
        }
    },
    actions: {
        // 异步设置用户信息
        async SET_USER_INFOS({commit}, data: object) {
            if (data) {
                commit('setUserInfos', data)
            } else {
                if(Session.get('userInfo')) commit('setUserInfos', Session.get('userInfo'))
            }
        }
    }

}

export default userInfosModule

