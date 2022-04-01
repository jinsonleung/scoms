import { SelectOptionTypes } from '/@/store/interface';


/**
 * 公司类型
 */
export const CompanyTypes: Array<SelectOptionTypes> = [
    {
        value: '1',
        label: '外商投资企业',
    },
    {
        value: '2',
        label: '股份制企业',
    },
    {
        value: '3',
        label: '私营企业',
    },
    {
        value: '4',
        label: '其他',
    }
];

// 企业体系结构选项对象数组
export const Architectures: Array<SelectOptionTypes> = [
    {
        value: '1',
        label: '总公司',
    },
    {
        value: '2',
        label: '子公司',
    },
    {
        value: '3',
        label: '办事处',
    },
    {
        value: '4',
        label: '其他',
    }
];

// 行业选项
export const Industries: Array<SelectOptionTypes> = [
    {
        value: '1',
        label: '物流运输',
    },
    {
        value: '2',
        label: '国际贸易',
    },
    {
        value: '3',
        label: '跨境电商',
    },
    {
        value: '4',
        label: '其他',
    }
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




