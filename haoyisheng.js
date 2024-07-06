/*******************************

脚本功能：好医生刷课
作者：ggvis
时间：20240706

*******************************

[rewrite_local]
^https?:\/\/weixin.haoyisheng.com\/wx\/getCourseInfo url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/haoyisheng.js

^https?:\/\/weixin.haoyisheng.com\/wx\/getTestsNew url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/haoyisheng.js

[mitm] 
hostname = weixin.haoyisheng.com

*******************************/

if ($response.body && $request.url.includes("getCourseInfo")) {
var body = $response.body.replace(/study_status":"0"/g,'study_status":"1"');
}

if ($response.body && $request.url.includes("getTestsNew")) {

var body = JSON.parse($response.body);
var result = "";
var simple_result = "";

body.tests.forEach(test => {
  result += `${test.answer} -- ${test.questionTitle}\n`;
  simple_result += test.answer;
});

simple_result = "答案：" + simple_result + "长按查看详情";
$notify(simple_result, result);
}
$done({ body });
