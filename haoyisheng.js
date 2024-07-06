/*******************************

脚本功能：好医生刷课
作者：ggvis
时间：20240706

*******************************

[rewrite_local]
^http[s]?:\/\/weixin.haoyisheng.com\/wx\/getCourseInfo url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/haoyisheng.js

[mitm] 
hostname = weixin.haoyisheng.com

*******************************/

if ($response.body && $request.url.includes("getCourseInfo")) {
var body = $response.body.replace(/study_status":"\d"/g,'is_free_watch":"1"');
}

$done({ body });
