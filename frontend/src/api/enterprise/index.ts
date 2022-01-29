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
 * 添加企业
 * @param params 要传的参数值
 * @returns 返回接口数据
 */
export function addNewEnterprise(params: object){
	return request({
		url: '/enterprise/add',
		method: 'post',
		data: params,
	});
}

/**
 * 修改企业记录
 * @param params 要传的参数值
 * @returns 返回接口数据
 */
export function updateEnterprise(params: object){
	return request({
		// url: '/enterprise/update',
		url: '/enterprise/post',
		method: 'post',
		data: params,
	});
}

/**
 * 查询所有企业记录
 * @param params 要传的参数值
 * @returns 返回接口数据
 */
export function getAllEnterprises(params: object){
	return request({
		url: '/enterprise/getall',
		method: 'get',
		data: params,
	});
}

/**
 * 分页查询企业记录
 * @param params 要传的参数值
 * @returns 返回接口数据
 */
export function getPageEnterprises(params:any){
	return request({
		// url: '/enterprise/getpagelist?limit='+ params.limit + '&offset=' + params.offset,
		url: '/enterprise',
		method: 'get',
		data: params,
	});
}

/**
 * 删除企业记录，软删除
 * @param params 要传的参数值，如{id:xxx}
 * @returns 返回接口数据
 */
export function deleteEnterprises(params:any){
	return request({
		url: '/enterprise/delete',
		method: 'post',
		data: params,
	});
}

/**
 * 查找企业记录
 * @param params 要传的参数值，如{account:xxx}或{'enterprise_name'}
 * @returns 返回接口数据
 */
export function getEnterprises(params:any){
	return request({
		url: '/enterprise/search',
		method: 'post',
		data: params,
	});
}
