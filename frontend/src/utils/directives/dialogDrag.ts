/**
 * element-plus 的 dialog 的拖拽方法，二次封装,https://www.jianshu.com/p/5c35a9595905
 * 使用方法：
 *  1）在main.js中引入指令import dialogDrag from "/@/utils/directives/dialogDrag"
 *  2）在<el-dialog></el-dialog>外面包裹一层<div v-dialogdrag></div> 如：
 * <div v-dialogdrag>
 *     <el-dialog ...>...</el-dialog>
 * </div>
 */

import {DirectiveBinding} from "vue";

const dialogDrag = (app: any, options: any) => {
    app.directive('dialogdrag', {
        mounted(el: any, binding: DirectiveBinding<any>) {
            const dialogHeaderEl = el.querySelector('.el-dialog__header');

            const dragDom = binding.value && binding.value.dragSelf ? el : el.querySelector('.el-dialog');
            dialogHeaderEl.style = 'cursor:move;';

            // 获取原有属性 ie dom元素.currentStyle 火狐谷歌 window.getComputedStyle(dom元素, null);
            const sty = dragDom.currentStyle || window.getComputedStyle(dragDom, null);
            dialogHeaderEl.onmousedown = (e: MouseEvent) => {
                // 鼠标按下，计算当前元素距离可视区的距离
                const disX = e.clientX - dialogHeaderEl.offsetLeft;
                const disY = e.clientY - dialogHeaderEl.offsetTop;
                // 获取到的值带px 正则匹配替换
                let styL: any, styT: any;
                if (sty.left.includes('%')) {
                    styL = +document.body.clientWidth * (+sty.left.replace(/\%/g, '') / 100);
                    styT = +document.body.clientHeight * (+sty.top.replace(/\%/g, '') / 100);
                } else {
                    styL = +sty.left.replace(/\px/g, '');
                    styT = +sty.top.replace(/\px/g, '');
                }

                document.onmousemove = (e: MouseEvent) => {
                    // 通过事件委托，计算移动的距离
                    const l = e.clientX - disX;
                    const t = e.clientY - disY;

                    // 移动当前元素
                    dragDom.style.left = `${l + styL}px`;
                    dragDom.style.top = `${t + styT}px`;
                };

                document.onmouseup = () => {
                    document.onmousemove = null;
                    document.onmouseup = null;
                };
            };
        },
    })
}

export default dialogDrag

