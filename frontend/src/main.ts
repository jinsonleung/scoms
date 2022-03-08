import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { store, key } from './store';
import { directive } from '/@/utils/directive';
import { i18n } from '/@/i18n/index';
import other from '/@/utils/other';
// import moment from 'moment'; // 时间格式化
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import '/@/theme/index.scss';
import mitt from 'mitt';
import screenShort from 'vue-web-screen-shot';
import VueGridLayout from 'vue-grid-layout';
import dialogDrag from "/@/utils/directives/dialogDrag"  //引入二将封装的可拖拽自定义dialog指令
import realImage from "/@/utils/directives/imageIsExist" //用于判断当前图片是否能够加载成功自定义指令

const app = createApp(App);

directive(app);
other.elSvg(app);

app
	.use(router)
	.use(store, key)
	.use(ElementPlus, { i18n: i18n.global.t, size: other.globalComponentSize })
	.use(i18n)
	.use(screenShort, { enableWebRtc: false })
	.use(VueGridLayout)
	.use(dialogDrag) //注册自定义可拖拽dialog组件
	.mount('#app');

// 全局挂载组件
app.config.globalProperties.mittBus = mitt();