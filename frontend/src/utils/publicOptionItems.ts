import { SelectOptionTypes } from '/@/store/interface';



// 公司类型
export const CompanyTypes: Array<SelectOptionTypes> = [
    {
        value: '0',
        label: '外商投资企业',
    },
    {
        value: '1',
        label: '股份制企业',
    },
    {
        value: '2',
        label: '私营企业',
    },
    {
        value: '3',
        label: '其他',
    }
];

// 企业体系结构类别
export const CompanyArchitectureTypes: Array<SelectOptionTypes> = [
    {
        value: '0',
        label: '总公司',
    },
    {
        value: '1',
        label: '子公司',
    },
    {
        value: '2',
        label: '办事处',
    },
    {
        value: '3',
        label: '其他',
    }
];

// 供应商类别
export const SupplierServiceTypes: Array<SelectOptionTypes> = [
    {
        value: '0',
        label: '综合物流',
    },
    {
        value: '1',
        label: '物流运输',
    },
    {
        value: '2',
        label: '物流配送',
    },
    {
        value: '3',
        label: '物流仓储',
    },
    {
        value: '4',
        label: '设备|材料',
    },
    {
        value: '5',
        label: '咨询|管理',
    },
    {
        value: '6',
        label: '报关报检',
    },
    {
        value: '7',
        label: '人力外包',
    },
    {
        value: '8',
        label: 'IT服务',
    },
    {
        value: '9',
        label: '其他',
    },
];

/**
 * 根据键值获取选项对象数组的值
 * @param options：选项对象数组
 * @param value：选项值
 */
export function getOptionsLabel(options:Array<SelectOptionTypes>, value: string): string {
    const ret = options.find(item => item.value === value);
    if (ret) return ret.label;
    return '';
}




