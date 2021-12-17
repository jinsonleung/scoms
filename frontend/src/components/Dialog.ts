// 组件扩展
// Dialog.ts
// 参考：https://www.jianshu.com/p/5c35a9595905
// 需要说明的是：这个指令是不能直接添加在ElDialog上的,需要使用一个div包裹下的，同时需要注意如果
// appendToBody为true直接添加到body上，指令是没有办法找到拖动元素的 也是不行的。




import { ElDialog } from 'element-plus';
import dialogDrag from '@/utils/directives/dialogDrag';
import { h, withDirectives } from 'vue';

const Dialog = (__props, context) => {
  return withDirectives(
    h(
      'div',
      h(
        ElDialog,
        {
          appendToBody: false,
          closeOnClickModal: false,
          ...context.attrs,
        },
        context.slots
      )
    ),
    [[dialogDrag]]
  );
};

export default Dialog;
