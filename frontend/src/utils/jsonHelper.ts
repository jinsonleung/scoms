/**
 * 遍历查找Json对象
 * @param: arr为json对象，obj为需要查找的对象
 * @return: 返回查询结果对象
 * @description: 调用方法 JsonQuery(json,{"id":"2"})[0].age
 * 参考：https://blog.csdn.net/winnershili/article/details/78720723
 */
export function JsonQuery(arr: Array<any>, obj: any): any {
    let _arr: any = [];
    for (let _jsonObj of arr) {
        let _b: boolean = true;
        for (let prop in obj) {
            if (_jsonObj[prop] != obj[prop]) {
                _b = false;
                break;
            }
        }
        if (_b) _arr.push(_jsonObj)
    }
    return _arr.length>0? _arr: null;
    // return _arr;
}