/**
 * 将对象转formdata格式，应用场景如VUE表单对象数据转为formData格式
 * @param data:对象
 * return: 返回formData格式
 */
export const objectToFormData=(data:any)=>{
    let formData = new FormData();
    let obj = data;
    let arrayKey = data.arrayKey;
    for (let i in obj) {
        if (Array.isArray(obj[i])){
            obj[i].map((item:any) => {
                if (!arrayKey) {
                    formData.append(i, item)
                } else {
                    formData.append(i + '[]', item)
                }
            })
        } else if (obj[i] instanceof FileList) {
            //filelist 文件类型的处理
            for (var fileItem = 0; fileItem < obj[i].length; fileItem++) {
                if (!arrayKey) {
                    formData.append(i, obj[i].item(fileItem))
                } else {
                    formData.append(i + '[]', obj[i].item(fileItem))
                }
            }
        } else {
            formData.append(i, obj[i])
        }
    }
    return formData;
}