// export const upload = data => request({
//     url:'https://up-z1.qiniup.com',
//     method:"post",
//     data
// })

import http from '@/utils/http2/index'

export const upload = () => {
    console.log('===upload....==')
    // http.get('http://127.0.0.1:8000/books/getall').then((res: any) => {
    //http.post('https://jsonplaceholder.typicode.com/posts/').then((res: any) => { //正确
    http.post('http://127.0.0.1:8000/books/addbook',{name:'《新方法论1》',author:'刘奥鹏'}).then((res: any) => {
        console.log('======调用啦=======',res.data)
    })
}


