/*
 * @Author: JinsonLiang
 * @Date: 2021-08-27 14:38:40
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-30 14:58:04
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\mock\goodList.ts
 */
import Mock from "mockjs";
import {pageHeaderEmits} from "element-plus";

function createCustomerList() {
    const count = 279;
    let customerList: any = [];
    for (let i = 0; i < count; i++) {
        customerList.push(
            Mock.mock({
                'id|+1': 1,
                "company_account": "@integer(10000000, 99999999)",
                "company_name": "@ctitle(5,10)" + "公司",
                "company_abbreviation_name": "@ctitle(3,6)",
                "company_address": "@county(true)",
                "city": "@city(true)",
                "license_no": '@integer(10000000,99999999)'+'@string("upper", 3, 3)'+'@integer(100000,999999)',
                "license_image": " ",
                "registration_capital": '@float(50, 10000, 2, 2)',
                "registration_date": '@date(yyyy-MM-dd hh:mm:ss)',
                "registration_effect_start": '@date(yyyy-MM-dd hh:mm:ss)',
                "registration_effect_end": '@date(yyyy-MM-dd hh:mm:ss)',
                "industry|1": ["电子数码", "生物健康", "环境保护", "汽车行业", "大数据", "物流快递"],
                "contact_name": "@name",
                "contact_tel": "020-" + Mock.mock(/\d{8}/),
                "contact_phone": "138" + Mock.mock(/\d{8}/),
                "is_available|1": true,
                "service_level|1": [1, 2, 3, 4, 5],
                "remark": "@ctitle(20)",
                "is_delete|1": true,
                "create_datetime": '@date(yyyy-MM-dd hh:mm:ss)',
                "create_user|1": ['user01', 'user02'],
                "update_datetime": '@date(yyyy-MM-dd hh:mm:ss)',
                "update_user|1": ['user01', 'user02'],
            })
        );
    }
    return customerList;
}


function getAllCustomer() {
    let listLength = 0;
    let customerList = createCustomerList();
    listLength = customerList.length;
    return {
        code: 200,
        msg: "后端返回的提示信息！",
        data: {
            customerList,
            totalCount: listLength,
        },
    };
}


function getPageCustomer(res:any) {
    let url = res.url
    let params_str = url.split("?")[1] // 得到url的?之后的参数列表
    let params = params_str.split("&")
    let pagesize = params[0].split("=")[1] // 页长
    let offet = params[1].split("=")[1] // 偏移量
    console.log("==getPageCustomer->offet/pagesize:",offet,pagesize)
    let customers = createCustomerList();
    // console.log('==customer==',customers)
    let customerList = customers.slice(offet*pagesize,(offet+1)*pagesize)

    return {
        code: 200,
        customerList: customerList, //分页数据
        length: customers.length,   //总记录数
        msg: "后端返回的提示信息！",
    };
}

export {getAllCustomer, getPageCustomer};
