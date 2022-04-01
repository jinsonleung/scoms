import request from '/@/utils/request'
import header from "/@/layout/component/header.vue";

/**
 * @func：分页获取数据
 * @param： params格式为 {pageNum:pageNum,pageSize:pageSize}
 * @returns: 返回接口数据
 */
export function getPageSuppliers(params:any){
	return request({
		url: '/supplier/?pageNum=' + params.pageNum + '&pageSize=' + params.pageSize,
		method: 'GET',
		data: params,
	});
}

/**
 * @func: 模糊查找
 * @param: params格式为{queryText:queryText,pageNum:pageNum,pageSize:pageSize}
 * @returns: 返回接口数据
 */
export function queryPageSuppliers(params:any){
	return request({
		url: `/supplier/?queryText=${params.queryText}&pageNum=${params.pageNum}&pageSize=${params.pageSize}`,
		method: 'GET',
		data: params,
	});
}

/**
 * @func：修改企业记录
 * @param params: 如{id:id}}
 * @returns: 返回接口数据
 */
export function updateSupplier1(params: any){
	return request({
		url: `/supplier/${params.id}/`,
		method: 'PUT',
		data: params,
	});
}

export function updateSupplier(params: any){
	console.log('--params.id--', params.get('id'));
	return request({
		url: `/supplier/${params.id}/`,
		method: 'PUT',
		headers: {'content-type': 'multipart/form-data'},
		data: params,
	});
}
