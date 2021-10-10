/*
 * @Author: JinsonLiang
 * @Date: 2021-08-27 14:38:40
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-30 14:58:04
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\mock\goodList.ts
 */
import Mock from "mockjs";
import { MockMethod } from "vite-plugin-mock";
import "@/mock/goodList";
import { ListQuery } from "@/type/goods";

function createListData() {
  const count = 100;
  const listNo = 10;
  let goodsList: any = [];
  for (let i = 0; i < count; i++) {
    goodsList.push(
      Mock.mock({
        id: "@id",
        "goodsName|1": ["简约刷牙漱口杯", "创意漱口杯", "小黄人漱口杯"],
        "englishName|1": ["cup1", "cup2", "cup3"],
        "shortName|1": ["glass4", "glass5", "glass6"],
        "goodsDesc|1": ["商品描述1", "商品描述2", "商品描述3"],
        "goodsbrand|1": ["houya", "Edo", "CH"],
        "goodsSpec|1": ["大", "中", "小"],
      })
    );
  }
  return goodsList;
}

function getListData() {
  const listNo = 10;
  let long = 0;
  let list = [];
  let totalListData = createListData();
  let goodsName = '小'
  if (goodsName) {
    list = totalListData.filter((item: any) => {
      const goodsNames = item.goodsName;
      if (goodsNames.includes(goodsName)) {
        return item;
      }
    });
  }
  long = list.length;
  return {
    code: 200,
    msg: "后端返回的提示信息！",
    data: {
      list,
      totalCount: long,
      pageNo: 1,
      pageSize: listNo,
    },
  };
}

export { getListData };
