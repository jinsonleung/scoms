import request from '/@/utils/request'
import header from "/@/layout/component/header.vue";


// ==============供应商接口=============
/**
 * @func：分页获取数据
 * @param: params 格式为 {pageNum:pageNum,pageSize:pageSize}
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
 * @param: params 格式为{queryText:queryText,pageNum:pageNum,pageSize:pageSize}
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
 * @func：更新
 * @param: params 如{id:id,...}}
 * @returns:
 */
export function updateSupplier(params: any){
	console.log('--params.pk--', params.get('id'));
	return request({
		url: `/supplier/${params.get('id')}/`,
		// url: `/supplier/${params.pk}/`,
		method: 'PUT',
		headers: {'content-type': 'multipart/form-data'},
		data: params,
	});
}

/**
 * @func：新增
 * @param: params 如{id:id,...}}
 * @returns:
 */
export function addSupplier(params: any){
	return request({
		url: '/supplier/',
		method: 'POST',
		//前端有图片文件，需要使用multipart/form-data请求头
		headers: {'content-type': 'multipart/form-data'},
		data: params,
	});
}

/**id
 * 删除（软删除）
 * @param: params 要传的参数值，如{id:id}
 * @returns:
 */
export function deleteSupplier(params:any){
	return request({
		url: `/supplier/${params.id}`,
		method: 'DELETE',
		data: params,
	});
}


// ==============供应商联系人接口=============
/**
 * @func：新增
 * @param: params 如{id:id,...}}
 * @returns:
 */
export function addSupplierContact(params: any){
	return request({
		url: '/supplierContact/',
		method: 'POST',
		data: params,
	});
}

/**
 * @func：更新
 * @param params: 如{id:id,...}}
 * @returns: 返回接口数据
 */
export function editSupplierContact(params: any){
	return request({
		url: `/supplierContact/${params.id}/`,
		method: 'PUT',
		data: params,
	});
}

/**id
 * 删除（软删除）
 * @param: params 要传的参数值，如{id:id}
 * @returns:
 */
export function deleteSupplierContact(params:any){
	return request({
		url: `/supplierContact/${params.id}/`,
		method: 'DELETE',
		// data: params,
	});
}