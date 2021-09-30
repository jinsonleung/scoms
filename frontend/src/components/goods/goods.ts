import { ref } from 'vue';
import { getList } from "@/api/goods/goodsListApi"
// import "@/mock/goodList"
import '@/mock/mockServer'
import http from '@/utils/http2';

/**
 * @author sunny
 * @desc 处理列表逻辑
 */
class ListClass {
    /**
     * @desc  构造方法
     * @param options {
     *     Api {
     *         ListApi         列表api
     *     }
     * }
     */
     listApi: any;
     pageNo: number;
     pageSize: number;
     pageTotal: number;
     loading : boolean;
     tableList: [];
     searchModel: {};

    constructor(Options = {}) {
        this.listApi = Options.Api.listApi || null;
        // 当前页码
        this.pageNo = 1;
        // 列表总数量
        this.pageTotal = 0;
        // 每页数量
        this.pageSize = 10;

        // 列表加载状态
        this.loading = false;
        // 列表数据
        this.tableList = [];
        // 列表搜索参数
        this.searchModel = [];
    }
    // 页码事件响应
    pageChange = (newPage:any) => {
        this.pageNo= newPage;
        this.getDataList();
    };
    /**
     * 搜索列表
     * @param searchParams {}  搜索参数
     */
    searchFn = (searchParams:any) => {
        //console.log(searchParams)   // test
        //console.log("searchParams: ", searchParams)
        this.pageNo = 1;
        this.searchModel = searchParams;
        this.getDataList();
    }
    /**
     * 获取列表前置操作  用于处理搜索参数
     * @param condition    发起请求前的搜索参数
     * @returns {*}        处理后的搜索参数  false则中断获取列表
     */
    beforeGetList (condition:any) {
        return condition;
    }
    /**
     * 加载列表
     * @param data       列表搜索参数
     */
    getDataList = (data = {}) => {
        //console.log(">>>>>",this.listApi)
        // if (!this.listApi) {
        //     throw new TypeError('请先配置Options.Api.listApi');
        // }
        this.loading = true;
        const condition = {
            pageNo: this.pageNo,
            pageSize: this.pageSize,
            ...this.searchModel,
            ...data
        };

        //console.log("conditions",condition)

        const conditionData = this.beforeGetList(JSON.parse(JSON.stringify(condition)));
        //console.log(conditionData)  // test
        if (conditionData === false) {
            return false;
        } else {
            //console.log("this.listApi(conditionData)>>>",this.listApi(conditionData))
            //this.listApi(conditionData).then((res:any) => {
            //getList(conditionData).then((res:any) => {
            //         //this.afterGetList(res);
            //         console.log(res.data)
            // }).finally((res:any) => {
            //     this.loading = false;
            // });
            console.log("conditionData>>>", conditionData)
            console.log("typeof>>",typeof(conditionData))
            http.get('/getList').then((res:any)=>{
                console.log(res.data)
            })

        }
    };

    /**
     * 获取列表成功回调，赋值
     * @param res   列表接口返回的数据
     */
    afterGetList (res:any) {
        if (+res.code === 200) {
            this.tableList = res.data.list;
            this.pageTotal = res.data.totalCount;
        }
    };
}

export { ListClass };
