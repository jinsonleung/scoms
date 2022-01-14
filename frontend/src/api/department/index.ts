/*
 * @Author: Jinosn.Liang
 * @Date: 2022-01-14 21:37:44
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2022-01-14 21:42:41
 * @Description: 部门api接口
 * @FilePath: /frontend/src/api/department/index.ts
 */

import request from '/@/utils/request'

/**
 * 添加部门
 * @param params 要传的参数值
 * @returns 返回接口数据
 */
export function addNewDepartment(params: object){
	return request({
		url: '/depatment/add',
		method: 'post',
		data: params,
	});
}

/**
 * 修改部门
 * @param params 要传的参数值
 * @returns 返回接口数据
 */
export function editDepartment(params: object){
	return request({
		url: '/depatment/edit',
		method: 'post',
		data: params,
	});
}




