import store from "@/store"
import axios, {AxiosRequestConfig, AxiosResponse} from "axios"
import {ElNotification, ElLoading} from "element-plus"

// 是否加载动画
let loading: { close(): void }


// 1、创建axios实例
const http = axios.create({
    // @ts-ignore
    //baseURL: process.env.VUE_API_BASE_URL | undefined,
    baseURL: 'http://127.0.0.1:8000', //url
    timeout: 5000,   //请求超时
    withCredentials: true,   //true:允许跨域
    headers: {
        'Content-Type': 'application/json'  // axios发送数 据时使用json格式})
        // 'Content-Type': 'application/x-www-form-urlencoded'
    },
})


// 2、异常拦截处理器
const errorHandler = ((error: { message: string }) => {
    loading.close() //关闭动画加载
    console.log(`err${error}`)  //控制台输出错误信息
    ElNotification({    //element-plus通知提示组件
        title: '请求失败',
        message: error.message,
        type: 'error'
    })
    return Promise.reject(error)    //返回Promise错误
})


//3、request 拦截处理器
http.interceptors.request.use((config: AxiosRequestConfig) => {
    console.log("==请求拦截器起作用==");
    loading = ElLoading.service({   //加载动画
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.4)'
    });
    // 将 post 请求的参数 JOSN 化处理
    // if(config.method == 'post') {
    //     config.data = JSON.stringify(config.data);
    // }
    // console.log('config.data',config.data)

    // token
    let token = store.getters && store.getters.token && store.getters.token ? store.getters.token : ''
    //如果token存在
    //让每个请求携带自定义token,可根据实际情况自行修改
    if (token) {
        //config.headers['Authorization'] = getlocalToken().
    }
    console.log(config)
    return config
}, errorHandler)


// 4、response 响应拦截处理器
http.interceptors.response.use((response: AxiosResponse<any>) => {
    loading.close() //关闭加载动画
    console.log("==响应拦截器起作用==");
    //console.log(response.data)  //控制台输出
    // console.log(response.status)  //测试
    if (response.status !== 200) {
        //console.log(response.data)
        if (401 === response.status) {
            localStorage.clear()
            ElNotification({
                title: '身份认证失败',
                message: response.data.message,
                type: 'error'
            })
            return Promise.reject(new Error(response.data.message || 'Error'))
        }
    } else {
        return response
    }
    return response
}, (error: AxiosResponse<any>) => {
    console.log(error.status) //测试
    loading.close()
    if (400 === error.status) {
        ElNotification({
            message: error.data.message || 'Error',
            type: 'error',
            duration: 5 * 1000
        })
        return error
    } else if (401 === error.status) {
        localStorage.clear()
        ElNotification({
            title: '身份认证失败',
            message: error.data.message || 'Error',
            type: 'error',
            duration: 5 * 1000
        })
        return Promise.reject(new Error(error.data.message || 'Error'))
    } else if (404 === error.status) {
        ElNotification({
            title: '路径不存在',
            message: '路径不存在',
            type: 'error',
            duration: 5 * 1000
        })
        return Promise.reject(new Error('路径不存在'))
    } else if (401 < error.status) {
        ElNotification({
            message: error.data.message || 'Error',
            type: 'error',
            duration: 5 * 1000
        })
        return error
    } else if (400 > error.status) {
        if (error.statusText == 'Network Error') {
            ElNotification({
                message: '网络异常！',
                type: 'error',
                duration: 5 * 1000
            })
        } else {
            ElNotification({
                message: error.data.message || 'Error',
                type: 'error',
                duration: 5 * 1000
            })
        }
    }
    return Promise.reject(error)
})


export default http



