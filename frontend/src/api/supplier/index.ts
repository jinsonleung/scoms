import request from '/@/utils/request'

/**
 * @func：分页获取数据
 * @param params: {pageNum:pageNum,pageSize:pageSize}
 * @returns: 返回接口数据
 */
export function getPageSuppliers(params:any){
	return request({
		url: '/supplier/?pageNum=' + params.pageNum + '&pageSize=' + params.pageSize,
		method: 'GET',
		data: params,
	});
}

