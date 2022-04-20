/*
* 全球国家、省（洲）、市、区（县）4级联动
*/
import GlobalCountry4LevelLinkageJson from '/@/mock/globalCountry4LevelLinkage.json';

export const get4LinkageList = (levels: number, val?: string) => {
    let linkageList = []
    // 获取国家数组
    if (levels===0){
        linkageList = GlobalCountry4LevelLinkageJson.filter((item:any)=> item.levels === 0);
    // 根据当前级中文名获取它的下一级的数组，如根据国家获取省（洲）
    }else if (levels>0){
        let obj = GlobalCountry4LevelLinkageJson.find((item:any)=> item.chn_name===val);
        let areaCode = obj.area_code;
        linkageList = GlobalCountry4LevelLinkageJson.filter((item:any)=> item.levels === levels && item.area_code.includes(areaCode));
    }
    return linkageList;
}