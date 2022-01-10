import Mock from "mockjs"

function loginMock(){
    const loginData = Mock.mock({
        userName: "@cname",
        userId: "@integer(10000,99999)",
        passward: /[a-z][A-Z][0-9][a-z][A-Z][0-9][a-z][A-Z][0-9]/,
        email: "@email()", // 随机生成email
    })
    return loginData
}

function checkLogin(req:any){
    //console.log("red",req)
    const {userName,passwordMd5} = JSON.parse(req.body)
    if (userName==='admin' && passwordMd5==='e10adc3949ba59abbe56e057f20f883e') {
        return {
            success: true
        }
    } else {
        return{
            success: false
        }
    }
}


export { loginMock, checkLogin}
