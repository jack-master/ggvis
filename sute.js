/*
功能：解锁sute生活会员，这是一个用来观看颜色链接的在线磁力播放工具。
作者：ggvis
时间：2024年03月23日
下载地址：https://sute.life/download

[rewrite_local]
^https:\/\/sute\.life\/api\/user\/getInfo url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/sute.js

[mitm]
hostname = sute.life
*/ 

let obj = JSON.parse($response.body);

obj.data.vip_type = 1;
obj.data.due_time = "2345-03-08 23:19:03";
obj.data.vip_label = "年会员";
obj.data.cloud_size_label = ": 9999.99 TB";

$done({body:JSON.stringify(obj)});
