/*
 * @Author: Jinosn.Liang
 * @Date: 2022-01-14 21:37:44
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2022-01-14 21:42:41
 * @Description: 企业API接口，使用restfull风格
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
 * @func：修改企业记录
 * @param params: 如{id:id}}
 * @returns: 返回接口数据
 */
export function updateEnterprise(params: any){
	return request({
		url: `/enterprise/${params.id}/`,
		method: 'PUT',
		data: params,
	});
}


/**
 * @func：分页查询企业记录
 * @param params: {page_num:page_num,page_size:page_size}
 * @returns: 返回接口数据
 */
export function getPageEnterprises(params:any){
	return request({
		url: '/enterprise/?page_num=' + params.page_num + '&page_size=' + params.page_size,
		method: 'GET',
		data: params,
	});
}

/**id
 * 删除企业记录，软删除
 * @param params 要传的参数值，如{id:id}
 * @returns 返回接口数据
 */
export function deleteEnterprises(params:any){
	return request({
		url: `/enterprise/${params.id}/`,
		method: 'DELETE',
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
