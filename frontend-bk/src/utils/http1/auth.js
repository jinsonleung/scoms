import config from './config'

let CACHE_TOKEN = config.CACHE_TOKEN

// token
const getToken = ()=> window.localStorage.getItem(CACHE_TOKEN)
const setToken = (token) => window.localStorage.setItem(CACHE_TOKEN, token)
const removeToken =()=> window.localStorage.removeItem(CACHE_TOKEN)

const reLogin = ()=>{}
export {
    getToken,
    setToken,
    removeToken,
    reLogin
}