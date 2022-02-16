import request from '/@/utils/request'

/**
 * @func：分页查询
 * @param params: {page_num:page_num,page_size:page_size}
 * @returns: 返回接口数据
 */
export function getPageAirport(params:any){
	return request({
		url: '/enterprise/?page_num=' + params.page_num + '&page_size=' + params.page_size,
		method: 'GET',
		data: params,
	});
}

/**
 * @func：单查
 * @param params: {id:id}}
 * @returns: 返回接口数据
 */
export function getAirport(params:any){
	return request({
		url: `/enterprise/${params.id}`,
		method: 'GET',
		data: params,
	});
}

/**
 * 模糊查找
 * @param params 要传的参数值，如{queryText:queryText}
 * @returns 返回接口数据
 */
export function queryAirports(params:any){
	return request({
		url: `/airport/?query=${params.query_text}&page_num=${params.page_num}&page_size=${params.page_size}`,
		method: 'GET',
		data: params,
	});
}
