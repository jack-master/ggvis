/*******************************

脚本功能：好医生刷课
作者：ggvis
时间：20240706

*******************************

[rewrite_local]
^http[s]?:\/\/weixin.haoyisheng.com\/wx\/getCourseInfo url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/haoyisheng.js

^http[s]?:\/\/weixin.haoyisheng.com\/wx\/getTestsNew  url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/haoyisheng.js

[mitm] 
hostname = weixin.haoyisheng.com


*******************************/

if ($response.body && $request.url.includes("getCourseInfo")) {
var body = $response.body.replace(/study_status":"0"/g,'study_status":"1"');
}

if ($response.body && $request.url.includes("getTestsNew")) {

var result = "123"

$notify(result, result);
}

$done({ body });
