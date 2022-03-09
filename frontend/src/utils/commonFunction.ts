// 通用函数
import useClipboard from 'vue-clipboard3';
import { ElMessage } from 'element-plus';
import { formatDate } from '/@/utils/formatTime';
import { useI18n } from 'vue-i18n';

export default function () {
	const { t } = useI18n();
	const { toClipboard } = useClipboard();
	//百分比格式化
	const percentFormat = (row: any, column: number, cellValue: any) => {
		return cellValue ? `${cellValue}%` : '-';
	};
	//列表日期时间格式化
	const dateFormatYMD = (row: any, column: number, cellValue: any) => {
		if (!cellValue) return '-';
		return formatDate(new Date(cellValue), 'YYYY-mm-dd');
	};
	//列表日期时间格式化
	const dateFormatYMDHMS = (row: any, column: number, cellValue: any) => {
		if (!cellValue) return '-';
		return formatDate(new Date(cellValue), 'YYYY-mm-dd HH:MM:SS');
	};
	//列表日期时间格式化
	const dateFormatHMS = (row: any, column: number, cellValue: any) => {
		if (!cellValue) return '-';
		let time = 0;
		if (typeof row === 'number') time = row;
		if (typeof cellValue === 'number') time = cellValue;
		return formatDate(new Date(time * 1000), 'HH:MM:SS');
	};
	// 小数格式化
	const scaleFormat = (value: any = 0, scale: number = 4) => {
		return Number.parseFloat(value).toFixed(scale);
	};
	// 小数格式化
	const scale2Format = (value: any = 0) => {
		return Number.parseFloat(value).toFixed(2);
	};
	// 点击复制文本
	const copyText = (text: string) => {
		return new Promise((resolve, reject) => {
			try {
				//复制
				toClipboard(text);
				//下面可以设置复制成功的提示框等操作
				ElMessage.success(t('message.layout.copyTextSuccess'));
				resolve(text);
			} catch (e) {
				//复制失败
				ElMessage.error(t('message.layout.copyTextError'));
				reject(e);
			}
		});
	};

	/**
	 * 获取静态资源（如图片文件）
	 * @param url: 如 src/assets/下的路径，如"images/airlinesLogo/ca.png"
	 * @returns {*|string}
	 */
	const getAssetsFile = (url: string) => {
		return new URL(`/src/assets/${url}`, import.meta.url).href;
	};

	return {
		percentFormat,
		dateFormatYMD,
		dateFormatYMDHMS,
		dateFormatHMS,
		scaleFormat,
		scale2Format,
		copyText,
		getAssetsFile,
	};
}
