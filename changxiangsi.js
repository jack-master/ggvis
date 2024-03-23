/*******************************

脚本功能：长相思解锁会员
作者：ggvis
时间：20240323
下载链接：https://apps.apple.com/app/id1600622338

*******************************

[rewrite_local]

^http[s]?:\/\/poetry\.nanxiani\.cn\/api\/User\/loginUserInfo url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/changxiangsi.js

[mitm] 

hostname = poetry.nanxiani.cn

*******************************/

let obj = JSON.parse($response.body);

obj.data.had_vip = true;
obj.data.is_device_user = true;
obj.data.vip_type = "permanent";
obj.data.vip_expire = "2099-12-02 14:09:32";

$done({body:JSON.stringify(obj)});
