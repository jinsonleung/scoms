// export const upload = data => request({
//     url:'https://up-z1.qiniup.com',
//     method:"post",
//     data
// })

import http from '@/utils/http2/index'

export const upload = () => {
    console.log('===upload....==')
    // http.get('http://127.0.0.1:8000/books/getall').then((res: any) => {
    // http.post('https://jsonplaceholder.typicode.com/posts/').then((res: any) => { //正确，target: 'https://jsonplaceholder.typicode.com'
    // http.post('http://127.0.0.1:8000/books/addbook2',{name:'《新方法论2》',author:'刘奥鹏2'}).then((res: any) => {   //正确
    http.post('http://dict.youdao.com/suggest',{q:'love',num:3,doctype:'json'}).then((res: any) => {
        console.log('======调用啦=======',res.data)
    })
}


