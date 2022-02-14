
import request from '/@/utils/request'

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


/**
 * 查找企业记录
 * @param params 要传的参数值，如{account:xxx}或{'enterprise_name'}
 * @returns 返回接口数据
 */
export function searchAirport(params:any){
	return request({
		url: '/airport/search',
		method: 'post',
		data: params,
	});
}
