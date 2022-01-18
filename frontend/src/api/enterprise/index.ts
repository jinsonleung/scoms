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
 * 分布查询企业记录
 * @param params 要传的参数值
 * @returns 返回接口数据
 */
export function getPageEnterprises(params: object){
	return request({
		url: '/enterprise/getpagelist?limit='+ params.limit + '&offset=' + params.offset,
		method: 'get',
		data: params,
	});
}