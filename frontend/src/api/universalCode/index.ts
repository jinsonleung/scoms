import request from '/@/utils/request'

/**
 * @func：分页查询
 * @param params: {pageNum:pageNum,pageSize:pageSize}
 * @returns: 返回接口数据
 */
export function getPageAirport(params:any){
	return request({
		url: '/enterprise/?pageNum=' + params.pageNum + '&pageSize=' + params.pageSize,
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
		url: `/airport/?queryText=${params.queryText}&pageNum=${params.pageNum}&pageSize=${params.pageSize}`,
		method: 'GET',
		data: params,
	});
}


/**
 * 模糊查找
 * @param params 要传的参数值，如{queryText:queryText}
 * @returns 返回接口数据
 */
export function queryAirlines(params:any){
	return request({
		url: `/airline/?queryText=${params.queryText}&pageNum=${params.pageNum}&pageSize=${params.pageSize}`,
		method: 'GET',
		data: params,
	});
}

/**
 * 模糊查找
 * @param params 要传的参数值，如{queryText:queryText}
 * @returns 返回接口数据
 */
export function queryCountries(params:any){
	return request({
		url: `/country/?queryText=${params.queryText}&pageNum=${params.pageNum}&pageSize=${params.pageSize}`,
		method: 'GET',
		data: params,
	});
}