/*******************************

脚本功能：显示微信小程序“一朵云上住”的房源更详细的信息，主要是微信号和手机号，显示在通知中。
作者：ggvis
时间：20240323

*******************************

[rewrite_local]

^http[s]?:\/\/api.yajiji.cc\/api\/\s+\?hid url script-response-body https://jack-master.github.io/ggvis/zufang.js


[mitm] 

hostname = apis.yajiji.cc

*******************************/



var body = JSON.parse($response.body);
var data = body.data;
var title = data.title
var contact_way = data.contact_way;
var phone = data.phone;
var min_price = data.min_price;
var max_price = data.max_price;
var basic_information = data.basic_information;
var source_detail = data.source_detail
var result = "" 

result = "长按查看详情❗️ 微信：" + contact_way + "，手机号："+ phone + "，价格："+ max_price + "，最低价：" + min_price + '\n' + basic_information + source_detail

$notify(title, result);


$done({})
